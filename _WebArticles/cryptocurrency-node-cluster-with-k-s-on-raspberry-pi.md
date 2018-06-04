# Cryptocurrency Node Cluster with K8s on Raspberry Pi

_Captured: 2018-06-01 at 20:21 from [www.hackster.io](https://www.hackster.io/pjdecarlo/cryptocurrency-node-cluster-with-k8s-on-raspberry-pi-696933?utm_source=Hackster.io+newsletter&utm_campaign=9a75e5ec5d-EMAIL_CAMPAIGN_2018_05_23_COPY_01&utm_medium=email&utm_term=0_6ff81e3e5b-9a75e5ec5d-141949901&mc_cid=9a75e5ec5d&mc_eid=1c68da4188)_

![Cryptocurrency Node Cluster with K8s on Raspberry Pi](https://hackster.imgix.net/uploads/attachments/492389/20180530_150752_\(1\)_R0rzcq5gxp.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)

Cryptocurrencies operate on the concept of P2P communication to distribute information about the state of the "ledger" or accepted transaction history on the network at large. This ledger contains all transactions which have ever occurred in the history of the network, as agreed upon by a consensus of nodes which notify each other of their respective transaction histories.

Let's hypothetically assume that you want to create your own cryptocurrency and are in need of deploying a network of nodes to facilitate this operation. With the adoption of Kubernetes (k8s), we can deploy a scalable, reliable, distributed network of nodes to ensure uptime on our theoretical network. k8s accomplishes this feat by deploying Docker containers based on hosted images to meet a desired state configuration. This allows us to describe what a deployment should look like in a simple configuration file and the k8s orchestrator takes care of the rest. Furthermore, we can take advantage of the fact that ARM compatible binaries of k8s exist run this network on a cluster of Raspberry Pis.

We can go even further and host these nodes behind a load-balancer within our k8s cluster to ensure that we have a resilient network capable of handling whatever the max theoretical limit of our network and combined computational powers of our Raspberry Pis can handle.

This article will focus on using a Litecoin-based cryptocurrency which was created in a [previous hackster article](https://www.hackster.io/pjdecarlo/how-to-make-a-cryptocurrency-using-litecoin-v0-15-source-fb5e82) known as [faithcoin](http://faithco.in/). You can follow the instructions in the link to create your own, or you can use the scripts provided here to get up and running with faithcoin. Adapting to pretty much any other cryptocurrency is possible so long as an ARM compatible binary of the node exists.

A rough diagram of what we intend to build is shown below:

![](https://hackster.imgix.net/uploads/attachments/492413/diagram_DcHXgkBgtb.png?auto=compress%2Cformat&w=680&h=510&fit=max)

In the diagram above, the k8s cluster is controlled by a k8s master node which supplies k8s-node1, k8s-node2, and k8s-node3 with a deployment of the faithcoin-arm docker image. In addition, a single node (k8s-node2 in this case) receives a deployment of the nginx-ingress controller. When a faithcoin client attempts to connect to the faithcoin node domain ip / port, the request will be routed to the nginx-ingress-controller and round-robin'd to one of k8s-node1, k8s-node2, or k8s-node3 where it will be handled by the faithcoin-arm instance running on that node. Once a single request has been made, the node itself will become aware of the faithcoin client ip and add it as a peer, allowing the node to make a P2P connection back to the faithcoin client.

To begin, you will need to have k8s installed on a Raspberry Pi cluster. Instructions are available in a variety of places but be aware that not all locations provide information that is up to date or confirmed working. I can confirm that success is achievable by following the instructions @ <https://github.com/aaronkjones/rpi-k8s-node-prep>

You will also need administrator access to the network that the cluster will be running on. This will be required to port forward incoming connections directly to the nginx-ingress-controller.

We will begin by deploying the faithcoin-arm docker image to our cluster. Afterward, we will configure a few options to obtain outbound internet access and enforce resource limits. You will need to run these commands from a shell session on the k8s-master.

Start by copying the following and save it to ' faithcoin-deployment.yaml'
    
    
    #---Deployment--#
    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: faithcoin
    spec:
    replicas: 3
    selector:
      matchLabels:
        app: faithcoin
    template:
      metadata:
        labels:
          app: faithcoin
          version: v0.15
      spec:
        containers:
        - name: faithcoin
          image: toolboc/faithcoin-arm
          readinessProbe:
            tcpSocket:
              port: 9666
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:
            tcpSocket:
              port: 9666
            initialDelaySeconds: 15
            periodSeconds: 20
        restartPolicy: Always
        hostNetwork: false
        dnsPolicy: "Default"
    ---
    #---Service---#
    kind: Service
    apiVersion: v1
    metadata:
    name: faithcoin
    spec:
    type: ClusterIP
    selector:
      app: faithcoin
    ports:
    - protocol: TCP
      port: 9666
      targetPort: 9666
    

Let's take a minute to grok what this file specifies. We are creating a deployment (i.e. a persistent desired state of the k8s infrastructure) that will create 3 running instances (replicas) of the faithcoin-arm docker image available from [https://hub.docker.com/r/toolboc/faithcoin-arm/.](https://hub.docker.com/r/toolboc/faithcoin-arm/) Upon starting an instance toolboc/faithcoin-arm a readiness probe is sent to verify that the container is running and monitored with a liveness probe which will signal a restart of the container on failure. Each of these instances will get an internal ip of their own which listens on it's own port 9666 which is the Faithcoin P2P protocol initiation port. We then expose a k8s Service which will route to the internal port 9666 of our container instances.

On the k8s master node, you can apply this deployment with:
    
    
    kubectl apply -f faithcoin-deployment.yaml
    

You will probably want to monitor the status of the deployment in the k8s dashboard. You will likely notice at this point that the image is spinning up successfully, but the logs indicate that the container does not have proper DNS configured to access the external network. This is because kube-dns does not have proper upstream nameservers configured. We will fix this by creating a new file named 'kube-dns-config-map.yaml' and paste in the following:
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
     name: kube-dns
     namespace: kube-system
     labels:
       addonmanager.kubernetes.io/mode: EnsureExists
    data:
     upstreamNameservers: |-
       ["8.8.8.8", "8.8.4.4"]
    

This will allow us to configure kube-dns to use the Google DNS resolvers available at [8.8.8.8](http://8.8.8.8/) and [8.8.4.4](http://8.8.4.4/) to obtain access to external services.

We will apply similar to above with:
    
    
    kubectl apply -f kube-dns-config-map.yaml
    

You should be able to verify in the Kubernetes Dashboard that block height is now propogating to the node via the default nodes present in [faithcoin.conf](http://faithcoin.conf/) which ships in the faithcoin-arm image:

![](https://hackster.imgix.net/uploads/attachments/492420/logs_2ZCSCa89UV.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)

Optionally, you may wish to apply resource limits within your cluster. This will ensure that no single container exceeds a defined amount of CPU or memory. To do this, create a new file named "resource_defaults.yaml" and paste in the following:
    
    
     apiVersion: v1
    kind: LimitRange
    metadata:
     name: cpu-limit-range
    spec:
     limits:
     - default:
         cpu: 1
         memory: 512Mi
       defaultRequest:
         cpu: 0.5
         memory: 256Mi
       type: Container
    

This will enforce that any container in the cluster is not allowed to exceed usage of 1 full cpu core (Rpi2 & Rpi3 both ship with 4 available cores) and no more than half of the available RAM (512Mi). In addition, each container will be granted half of 1 cpu core and 256Mi on startup. You may modify to fit your needs, then apply the configuration with:
    
    
    kubectl apply -f resource_defaults.yaml
    

_**A**_ _**short**_** t**_**heoretical**_** c**_**oncept**_ _**regarding**_ _**containerized**_ _**nodes:**_

You may recall that we setup the service using type ClusterIP and did not expose any host ports in our deployment configuration. Due to this, we can spin up multiple container instances on single k8s node (i.e. multiple instances of the cryptocurrency node on a single raspberry pi) as each instance will have it's own virtual port 9666. This can allow us to run theoretically as many cryptocurrency nodes as our hardware can support with regard to resource limits. Consider that Bitcoin runs an estimated [10,000 reachable nodes](https://bitnodes.earn.com/). With enough container instances, you could possibly live-fork an existing network, especially if it is a much smaller cryptocurrency. This of course assumes you have enough trust from the network at large and expose each container instance as a specific node on the main network of the cryptocurrency in question.

Here is an example of this in action, you will notice 9 total faithcoin nodes running on 3 raspberry pi physical nodes in kubernetes:

![](https://hackster.imgix.net/uploads/attachments/492948/nodes_r20b4tvS9b.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)

k8s does not handle loadbalancing by itself, it requires an external service on a supported host to do so, although nothing stops you from deploying your own loadbalancer into the k8s cluster itself. There are a variety of ingress services available for k8s, but most are only capable of handling http traffic (i.e. [traefik](https://traefik.io/)). That is nice, as the k8s model typically abstracts services away in an internal network and exposes only the front-end on the external network. In our case, we need to forward raw TCP traffic and there is only one service which allows at this time, that is the [nginx ingress controller](https://github.com/nginxinc/kubernetes-ingress). For some reason, k8s supplies a build script for producing ARM builds of the nginx ingress controller but does not host them anywhere that I could find. In addition, the [ARM build leaves out an important dependency](https://github.com/kubernetes/ingress-nginx/issues/2547) that causes a crash even if one were to exist. I have supplied a fix and published a pubic image to dockerhub to get around these issues @ <https://hub.docker.com/r/toolboc/nginx-ingress-controller-arm/>

We will begin deploying the nginx-ingress-controller by creating a new file named "ingress-nginx-deployment.yaml" with the following contents:
    
    
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
     name: ingress-nginx
    ---
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
     name: default-http-backend
     labels:
       app: default-http-backend
     namespace: ingress-nginx
    spec:
     replicas: 1
     selector:
       matchLabels:
         app: default-http-backend
     template:
       metadata:
         labels:
           app: default-http-backend
       spec:
         terminationGracePeriodSeconds: 60
         containers:
         - name: default-http-backend
           # Any image is permissible as long as:
           # 1. It serves a 404 page at /
           # 2. It serves 200 on a /healthz endpoint
           image: gcr.io/google_containers/defaultbackend-arm:1.4
           livenessProbe:
             httpGet:
               path: /healthz
               port: 8080
               scheme: HTTP
             initialDelaySeconds: 30
             timeoutSeconds: 5
           ports:
           - containerPort: 8080
           resources:
             limits:
               cpu: 10m
               memory: 20Mi
             requests:
               cpu: 10m
               memory: 20Mi
    ---
    apiVersion: v1
    kind: Service
    metadata:
     name: default-http-backend
     namespace: ingress-nginx
     labels:
       app: default-http-backend
    spec:
     ports:
     - port: 80
       targetPort: 8080
     selector:
       app: default-http-backend
    ---
    kind: ConfigMap
    apiVersion: v1
    metadata:
     name: nginx-configuration
     namespace: ingress-nginx
     labels:
       app: ingress-nginx
    ---
    kind: ConfigMap
    apiVersion: v1
    metadata:
     name: tcp-services
     namespace: ingress-nginx
    ---
    kind: ConfigMap
    apiVersion: v1
    metadata:
     name: udp-services
     namespace: ingress-nginx
    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
     name: nginx-ingress-serviceaccount
     namespace: ingress-nginx
    ---
    apiVersion: rbac.authorization.k8s.io/v1beta1
    kind: ClusterRole
    metadata:
     name: nginx-ingress-clusterrole
    rules:
     - apiGroups:
         - ""
       resources:
         - configmaps
         - endpoints
         - nodes
         - pods
         - secrets
       verbs:
         - list
         - watch
     - apiGroups:
         - ""
       resources:
         - nodes
       verbs:
         - get
     - apiGroups:
         - ""
       resources:
         - services
       verbs:
         - get
         - list
         - watch
     - apiGroups:
         - "extensions"
       resources:
         - ingresses
       verbs:
         - get
         - list
         - watch
     - apiGroups:
         - ""
       resources:
           - events
       verbs:
           - create
           - patch
     - apiGroups:
         - "extensions"
       resources:
         - ingresses/status
       verbs:
         - update
    ---
    apiVersion: rbac.authorization.k8s.io/v1beta1
    kind: Role
    metadata:
     name: nginx-ingress-role
     namespace: ingress-nginx
    rules:
     - apiGroups:
         - ""
       resources:
         - configmaps
         - pods
         - secrets
         - namespaces
       verbs:
         - get
     - apiGroups:
         - ""
       resources:
         - configmaps
       resourceNames:
         # Defaults to "<election-id>-<ingress-class>"
         # Here: "<ingress-controller-leader>-<nginx>"
         # This has to be adapted if you change either parameter
         # when launching the nginx-ingress-controller.
         - "ingress-controller-leader-nginx"
       verbs:
         - get
         - update
     - apiGroups:
         - ""
       resources:
         - configmaps
       verbs:
         - create
     - apiGroups:
         - ""
       resources:
         - endpoints
       verbs:
         - get
    ---
    apiVersion: rbac.authorization.k8s.io/v1beta1
    kind: RoleBinding
    metadata:
     name: nginx-ingress-role-nisa-binding
     namespace: ingress-nginx
    roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: nginx-ingress-role
    subjects:
     - kind: ServiceAccount
       name: nginx-ingress-serviceaccount
       namespace: ingress-nginx
    ---
    apiVersion: rbac.authorization.k8s.io/v1beta1
    kind: ClusterRoleBinding
    metadata:
     name: nginx-ingress-clusterrole-nisa-binding
    roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: ClusterRole
     name: nginx-ingress-clusterrole
    subjects:
     - kind: ServiceAccount
       name: nginx-ingress-serviceaccount
       namespace: ingress-nginx
    ---
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
     name: nginx-ingress-controller
     namespace: ingress-nginx
    spec:
     replicas: 1
     selector:
       matchLabels:
         app: ingress-nginx
     template:
       metadata:
         labels:
           app: ingress-nginx
         annotations:
           prometheus.io/port: '10254'
           prometheus.io/scrape: 'true'
       spec:
         nodeSelector:
             nginx-controller: nginx-ingress-controller
         serviceAccountName: nginx-ingress-serviceaccount
         containers:
           - name: nginx-ingress-controller
             image: toolboc/nginx-ingress-controller-arm:0.15.0
             args:
               - /nginx-ingress-controller
               - --default-backend-service=$(POD_NAMESPACE)/default-http-backend
               - --configmap=$(POD_NAMESPACE)/nginx-configuration
               - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
               - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
               - --publish-service=$(POD_NAMESPACE)/ingress-nginx
               - --annotations-prefix=nginx.ingress.kubernetes.io
             env:
               - name: POD_NAME
                 valueFrom:
                   fieldRef:
                     fieldPath: metadata.name
               - name: POD_NAMESPACE
                 valueFrom:
                   fieldRef:
                     fieldPath: metadata.namespace
             ports:
             - name: http
               containerPort: 80
             - name: https
               containerPort: 443
             - containerPort: 9667
               hostPort: 9667
           # we expose 18080 to access nginx stats in url /nginx-status
           # this is optional
             - containerPort: 18080
               hostPort: 18080
    #          livenessProbe:
    #            failureThreshold: 3
    #            httpGet:
    #              path: /healthz
    #              port: 10254
    #              scheme: HTTP
    #            initialDelaySeconds: 10
    #            periodSeconds: 10
    #            successThreshold: 1
    #            timeoutSeconds: 1
    #          readinessProbe:
    #            failureThreshold: 3
    #            httpGet:
    #              path: /healthz
    #              port: 10254
    #              scheme: HTTP
    #            periodSeconds: 10
    #            successThreshold: 1
    #            timeoutSeconds: 1
             securityContext:
               runAsNonRoot: false
    

This is a large config that deploys the default backend required by nginx along with an accompanying service. It then creates the necessary roles required for the nginx-ingress-controller (i.e. ability to read configmaps), then creates the configmaps that are used by the controller for internal configuration of nginx. These configmaps allow us to use a k8s mechanism to drive updates to the controller and configure the underlying nginx instance within the associated container. Finally, we deploy the nginx-ingress-controller itself and make sure to open port 9667 (technically this can be any arbitrary port, but this is important to note as it is reused in subsequent instructions). We will use this to listen for TCP requests to be forwarded to our faithcoin nodes within the k8s cluster in a load-balanced fashion.

Now, we want to be very specific as to which node ends up running the nginx-ingress-controller. This is controlled by whether the label "nginx-controller=nginx-ingress-controller" is present or not on the node. To assign a node the ability to accept the deployment, run:
    
    
    kubectl label nodes <NameOfIntendedNode> nginx-controller=nginx-ingress-controller
    

Next up, we will deploy the accompanying service for the nginx-ingress-controller. To do this, create a file named "ingress-nginx-service.yaml" and paste in the following:
    
    
    apiVersion: v1
    kind: Service
    metadata:
     name: ingress-nginx
     namespace: ingress-nginx
    spec:
     type: NodePort
     ports:
     - name: http
       port: 80
       targetPort: 80
       protocol: TCP
     - name: https
       port: 443
       targetPort: 443
       protocol: TCP
     - name: faithcoin-ingress
       port: 9667
       targetPort: 9667
       protocol: TCP
     selector:
       app: ingress-nginx
    

Now apply the service with:
    
    
    kubectl apply -f ingress-nginx-service.yaml
    

Take note of the specification to use a nodePort for port 9667 again. This will allow us to access the port externally using a randomly assigned port in the 30000-32767 range.

To obtain this port, run:
    
    
    kubectl get --all-namespaces services
    

You will receive an output similar to the following:

In my case, port 9667 is assigned to NodePort 32736.

Now, remember how I mentioned that configmaps are used to update the underlying nginx service? We are going to use a special configmap to forward all TCP traffic on port 9667 of the nginx-ingress-controller to an available faithcoin service on port 9666.

To accomplish this, create a file named "ingress-nginx-configmap-tcp-services.yaml" and paste in the following:
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
     name: tcp-services
     namespace: ingress-nginx
    data:
     9667: "default/faithcoin:9666"
    

Now apply with:
    
    
    kubectl apply -f ingress-nginx-configmap-tcp-services.yaml
    

At this point, the only thing left to do is route all incoming faithcoin traffic on the external network to the nginx-ingress-controller.

To do this, we need to obtain the internal ip address (not the cluster address) of the node running the ingress-ngninx service.

I used the kube dashboard to obtain this, but there is probably a more programmatic way:

![](https://hackster.imgix.net/uploads/attachments/492431/ip_iMEkFQeWqO.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)

In my example, the nginx-ingress-controller is running on k8s-node3 which is assigned an internal ip of 192.168.1.83.

With this information, we can login to our router and forward all traffic on port 9666 to this ip and direct it to the previously obtained NodePort value. In my case, I will forward all traffic from 9666 to 192.168.1.83:32736. This essentially means that all faithcoin traffic now flows directly to the nginx-ingress-controller where it is round robin'd to one of the available faithcoin-arm instances in the cluster.
    
    
    addnode=home.pjdecarlo.com:9666
    

This domain (home.pjdecarlo.com) points to the network where my pi cluster is running. I then launched the faithcoin-qt client and selected '_Help => Debug Windows => Peers_' to verify that I am connecting to something at [home.pjdecarlo.com:9666](http://home.pjdecarlo.com:9666/)

![](https://hackster.imgix.net/uploads/attachments/492433/peers_NyChi8wGk4.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)

If you view the logs of the nginx-ingress-controller, you will notice a bunch of TCP connections, indicating that ingress is properly forwarding the TCP traffic.

![](https://hackster.imgix.net/uploads/attachments/492434/logs2_rqxgD12i9a.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)

And there you have it! The world's first cryptocurrency that is supported by a majority of nodes running in a k8s Raspberry Pi cluster!

k8s is awesome and there is no better way to learn it than with a baremetal deployment in my opinion. Upon learning about how k8s attempts to solve the issue of scalable, reliable, distributed services; I could not help but look for some sort of problem that would be great to solve with it. While k8s does this extremely well, there are some issues around the elegance of certain things that should be supported better, i.e. load-balancing of traffic that is not HTTP.

As a result of this exercise, my personal cryptocurrency [faithcoin](http://faithco.in/) now runs on an in-house cluster of load-balanced Raspberry Pis. This means a scalable, reliable, distributed network of decentralized cryptographic transactions is always buzzing along somewhere in my office. To me, that's just awesome.

If you would like to learn more about faithcoin, you can check out the [GitHub repo](https://github.com/toolboc/faithcoin),[ download a wallet and start mining](http://faithco.in/get-started/), or watch the [block explorer](http://blockchain.faithco.in/insight/) accumulate blocks in real-time (34,000+ and counting at this time!).

Let us know what you think in the comments, and give a shout out if you are able to successfully reproduce.

Until next time... happy hacking!

![Diagram 6ii8pb0yoy](https://hackster.imgix.net/uploads/attachments/492440/diagram_6Ii8pb0yOY.png)

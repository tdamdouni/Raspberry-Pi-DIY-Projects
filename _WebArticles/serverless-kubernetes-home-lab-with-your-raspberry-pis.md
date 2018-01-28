# Serverless Kubernetes home-lab with your Raspberry Pis

_Captured: 2017-12-28 at 05:34 from [blog.alexellis.io](https://blog.alexellis.io/serverless-kubernetes-on-raspberry-pi/)_

This guide shows how to build your own Serverless Kubernetes cluster with Raspberry Pi and [OpenFaaS](https://www.openfaas.com/). This post is the third in a series on building a cheap and scalable Serverless Raspberry Pi cluster. Scale by adding more $35 Raspberry Pis.

> [OpenFaaS](https://www.openfaas.com/) is a serverless framework for Docker and Kubernetes that is easy to use, deploy and built with care by a growing community of hackers.

![](https://pbs.twimg.com/media/DKGfQ7bWkAAkGb9.jpg)

_Raw materials: Raspberry Pi 2 or 3_

## The series so far

If you're one of the many people who are new to this space, read the introduction of our first post to find out what Serverless is and what it can do for you.

### Part 1: Swarm

In Part 1 of the series we introduced Serverless and what it is being used for. We then built out a cluster using Docker Swarm.

### Part 2: Monitoring

Part 2 focuses on monitoring the cluster for disk space, CPU usage and network I/O.

### Part 3: Kubernetes

In this part we build a Kubernetes cluster with Raspberry Pis and deploy OpenFaaS to test it. You'll have access to `kubectl` \- so once you've finished the tutorial you can keep learning.

## Build your cluster

**The way it was meant to be**

This guide will show you how to install Kubernetes directly on top of Raspbian - the way it was meant to be. We won't need to flash any custom images or spend time learning how to configure a new OS.

Follow the step-by-step instructions over on my Gist:

  * [Install your Kubernetes cluster (Gist)](https://gist.github.com/alexellis/fdbc90de7691a1b9edb545c17da2d975)
![Kube](https://coreos.com/assets/images/svg/logos/kubernetes.svg)

### Deploy OpenFaaS

Now deploy [OpenFaaS](https://github.com/openfaas/faas). OpenFaaS stands for Functions as a Service - a hot and emerging technology which lets you focus on writing small, reusable functions. Just put together a few lines of code, say what dependencies you need - then use our CLI to build it into a Docker image and deploy it to your cluster - OpenFaaS will do the rest.

You then get full metrics made available through Prometheus and this data is used by the cluster to auto-scale your function as demand increases.

Watch my OpenFaaS introduction and demos from Cloud Native London meetup in HD on Vimeo: [FaaS and Furious - 0 to Serverless in 60 seconds, anywhere](https://skillsmatter.com/skillscasts/10813-faas-and-furious-0-to-serverless-in-60-seconds-anywhere).

Let's clone the GitHub repository and use `kubectl` to deploy. A Helm chart is also available in the repository for if you want to deploy OpenFaaS to a cloud or your laptop.
    
    
    $ git clone https://github.com/openfaas/faas-netes && \
      cd faas-netes 
    $ kubectl apply -f faas.armhf.yml,rbac.yml,monitoring.armhf.yml
    

> Note: The Kubernetes controller for OpenFaaS is called faas-netes. 

That's it.

Now get the IP address of your master node in the cluster (i.e. 192.168.0.100) and open up the FaaS UI in a web-browser:

<http://192.168.0.100:31112/>

> We're using the NodePort concept in Kubernetes, but you can add an IngressController and a software load balancer such as Nginx or Traefik if you want to use a privileged port like 80.

### Try the OpenFaaS CLI

You can get the CLI for OpenFaaS by typing in:
    
    
    $ curl -SL https://cli.openfaas.com/ | sudo sh
    
    armv7l  
    Getting package https://github.com/alexellis/faas-cli/releases/download/0.4.14/faas-cli-armhf  
    Attemping to move faas-cli to /usr/local/bin  
    New version of faas-cli installed to /usr/local/bin  
    

> We build the CLI for Windows, Linux, Linux ARM and MacOS.

You can get help from the CLI at any time or check its version with:
    
    
    $ faas-cli --help
    $ faas-cli <command> --help
    $ faas-cli version
    

**Patch your function templates for ARM**

Clone the CLI samples and patch the templates for ARM:
    
    
    $ git clone https://github.com/alexellis/faas-cli && \
      cd faas-cli
    
    $ cp template/node-armhf/Dockerfile template/node/ && \
      cp template/python-armhf/Dockerfile template/python/ && \
      cp template/go-armhf/Dockerfile template/go/
    

Now you can go ahead and create your first function in Python:
    
    
    $ faas-cli new --lang python --name http-ping
    
    Folder: http-ping created.  
    Function created in folder: http-ping  
    Stack file written: http-ping.yml  
    

This will create an empty hello-world style function. Let's check it out.

You'll see that the CLI created three files:
    
    
    http-ping.yml  
    http-ping/handler.py  
    http-ping/requirements.txt  
    

Edit http-ping.yml and replace `image: http-ping` with your Docker Hub account like: `image: alexellis2/http-ping`.

Since we are on Kubernetes we also need to edit the gateway port from `gateway: http://localhost:8080` to `gateway: http://localhost:31112`.

Now let's build, deploy and invoke the function:
    
    
    $ faas-cli build -f http-ping.yml
    

The first time you run this we'll download some Docker images, but for each subsequent build it will use a cache.

> If your Docker engine is running in experimental mode you can also "squash" the layers for a smaller final image with `faas-cli build --squash`.
    
    
    $ faas-cli push -f http-ping.yml
    

We are pushing to the Docker Hub, but if you have a local registry that may be faster.
    
    
    $ faas-cli deploy -f http-ping.yml
    Deploying: http-ping.  
    Deployed.  
    202 Accepted  
    URL: http://localhost:31112/function/http-ping  
    

The function will be downloaded by Kubernetes and deployed on one of your nodes (Raspberry Pis).

> This could take a couple of minutes the first time since the Raspberry Pi's network and I/O interfaces are slower than regular PCs.

Now you can invoke the function via the UI or the CLI.

  * Invoke the function:

Here we can pipe in any output from another CLI command:
    
    
    $ echo -n "Hi Kubernetes!" | faas-cli invoke http-ping -f http-ping.yml
    Hi Kubernetes!  
    

Or type in freestyle:
    
    
    $ faas-cli invoke http-ping -f http-ping.yml
    Reading from STDIN - hit (Control + D) to stop.  
    I'm writing the tutorial now
    
    I'm writing the tutorial now  
    

  * List the functions and the invocation count:
    
    
    $ faas-cli list -f http-ping.yml
    Function                        Invocations     Replicas  
    http-ping                       2               1  
    

We see the replica count is set to 1 meaning there is only one container mapped to this function (more are added by OpenFaaS if we start to generate high load).

The invocation count is now 2 which is updated live from Prometheus metrics.

### Go deeper

Here are some ways you can support our work:

**Star** our GitHub repository for [OpenFaaS and show support](https://github.com/openfaas/faas) for the work we do.

**Keep learning**

Kubernetes is easy to learn but hard to master, so start today with my blog series:

  * [Learn Kubernetes by Alex Ellis](https://blog.alexellis.io/tag/learn-k8s/)

Compare and contrast the key differences between Docker Swarm and Kubernetes in my recent analysis:

  * [What you need to know: Kubernetes and Swarm](https://blog.alexellis.io/you-need-to-know-kubernetes-and-swarm/)

**Share with your network**

We'd love to see what you build with [OpenFaaS](https://github.com/openfaas/faas) and your new Kubernetes home-lab. Share and Tweet to [@openfaas](https://twitter.com/openfaas) or [@alexellisuk](https://twitter.com/alexellisuk).

> Build your own Serverless home-lab with Kubernetes and Raspbian [@kubernetesio](https://twitter.com/kubernetesio?ref_src=twsrc%5Etfw) [@Raspberry_Pi](https://twitter.com/Raspberry_Pi?ref_src=twsrc%5Etfw) [#rpiweekly](https://twitter.com/hashtag/rpiweekly?src=hash&ref_src=twsrc%5Etfw) <https://t.co/ytDMU92wWj> [pic.twitter.com/SYWKWaXa6v](https://t.co/SYWKWaXa6v)
> 
> -- Alex Ellis (@alexellisuk) [October 12, 2017](https://twitter.com/alexellisuk/status/918400378147917824?ref_src=twsrc%5Etfw)

**Got edits?**

The world of container and Kubernetes moves at a fast pace. If you have edits where files or URLs have been renamed or moved please get in touch so we can keep the guide at AAA quality for everyone.

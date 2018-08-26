# Object Detection on Drone Imagery Using Raspberry Pi

_Captured: 2018-06-16 at 10:16 from [www.hackster.io](https://www.hackster.io/arun-gandhi/object-detection-on-drone-imagery-using-raspberry-pi-208676?utm_source=Hackster.io+newsletter&utm_campaign=e2c75dfbc9-EMAIL_CAMPAIGN_2017_07_26_COPY_01&utm_medium=email&utm_term=0_6ff81e3e5b-e2c75dfbc9-141949901&mc_cid=e2c75dfbc9&mc_eid=1c68da4188)_

Blog link : <https://medium.com/nanonets/how-we-flew-a-drone-to-monitor-construction-projects-in-africa-using-deep-learning-b792f5c9c471>

[Pragmatic Master,](http://pragmaticmaster.com/) a South-African robotics-as-a-service collaborated with Nanonets for automation of remotely monitoring progress of a **housing construction project in Africa.**

> These projects are generally prone to delay and pilferage due to misreporting which can potentially be solved by flying a drone frequently to map and document.

We aim to detect the following infrastructure to capture the construction progress of a house in it's various stages : a foundation (start), wallplate (in-progress), roof (partially complete), apron (finishing touches) and geyser (ready-to-move in)

![](https://hackster.imgix.net/uploads/attachments/499787/0_VrUqVfAZ2MoYUDPe.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Pragmatic Master chose Nanonets as it's deep learning provider because of it's easy-to-use web platform and plug&play APIs.

The end-to-end process of using the [Nanonets API ](https://nanonets.com/drone/?utm_source=Medium.com&utm_campaign=Object%20Detection%20on%20Aerial%20Imagery%20using%20Drones%20with%20Deep%C2%A0Learning)is as simple as four steps.

![](https://hackster.imgix.net/uploads/attachments/499786/1_KoCgCAs50r6PYg_qctFtcw.png?auto=compress%2Cformat&w=680&h=510&fit=max)

  * **Upload images:** Images acquired from the drones can be uploaded directly to our upload [landing page.](https://nanonets.com/drone/?utm_source=Medium.com&utm_campaign=Object%20Detection%20on%20Aerial%20Imagery%20using%20Drones%20with%20Deep%C2%A0Learning) For the current case study, we had a total of **1442 images** of a construction site taken at low altitudes. Example of uploaded images is given below.

Labelling images is probably the hardest and the most time-consuming step in any supervised machine learning pipeline, but at [Nanonets ](https://nanonets.com/objectdetection#utm_source=Medium&utm_campaign=Object%20Detection%20on%20Aerial%20Imagery%20using%20Drones%20with%20Deep%20Learning)we have this covered for you. We have in-house experts that have multiple years of working with aerial images. They will annotate your images with high precision and accuracy to aid better model training. For the Pragmatic Master use-case, we were labelling the following objects and their total count in all the images.

  * Wallplate: 1043
![](https://hackster.imgix.net/uploads/attachments/499790/1_1VQyQSaRt2cQ3mXSKNFh-A.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Example labelled image of geysers

At Nanonets we employ the principle of **Transfer Learning** while training on your images. This involves re-training a pre-trained model that has already been pre-trained with a large number of aerial images. This helps the model identify micro patterns such as edges, lines and contours easily on your images and focus on the more specific macro patterns such as houses, trees, humans, cars, etc. Transfer learning also gives a boost in term of training time as the model does not need to be trained for a large number of iterations to give a good performance.

Our proprietary deep learning software smartly selects the best model along with optimising the hyper-parameters for your use-case. This involves searching through multiple models and through a hyperspace of parameters using advanced search algorithms.

The hardest objects to detect are the smallest ones, due to their low resolution. Our model training strategy is optimised to detect very small objects such as Geysers and Aprons which have an area of a few pixels.

![](https://hackster.imgix.net/uploads/attachments/499789/1_J9fkKzlYv-xnd275MiBYFw.jpeg?auto=compress%2Cformat&w=680&h=510&fit=max)

![](https://hackster.imgix.net/uploads/attachments/499788/1_DMwr0fOL8_Yd6Gzewi1HDA.jpeg?auto=compress%2Cformat&w=680&h=510&fit=max)

Full stitched images with predictions

Following are the mean average precision per class that we get,

  * **Roof: 95.1%**
  * **Geyser: 88%**
  * **Wallplate: 92%**
  * **Apron: 81%**

**Note:** Adding more images can lead to an increase in the mean average precision. Our API also supports detecting multiple objects in the same image such as Roofs and Aprons in one image.

Once the model is trained, you can either integrate [Nanonet's API ](https://nanonets.com/drone/?utm_source=Medium.com&utm_campaign=Object%20Detection%20on%20Aerial%20Imagery%20using%20Drones%20with%20Deep%C2%A0Learning)directly into your system or we also provide a docker image with the trained model and inference code that you can use. Docker images can easily scale and provide a fault tolerant inference system.

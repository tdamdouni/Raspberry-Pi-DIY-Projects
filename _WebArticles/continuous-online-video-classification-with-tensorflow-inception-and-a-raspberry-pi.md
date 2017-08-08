# Continuous online video classification with TensorFlow, Inception and a Raspberry Pi

_Captured: 2017-08-05 at 17:00 from [blog.coast.ai](https://blog.coast.ai/continuous-online-video-classification-with-tensorflow-inception-and-a-raspberry-pi-785c8b1e13e1?source=userActivityShare-c79006fee040-1501945243)_

## Or, using convolutional neural networks to identify what's on TV

![](https://cdn-images-1.medium.com/freeze/max/60/1*rO0ktQ1Hv-70UF1rBy1wyA.jpeg?q=20)![](https://cdn-images-1.medium.com/max/1600/1*rO0ktQ1Hv-70UF1rBy1wyA.jpeg)

Much has been written about using deep learning to classify _prerecorded video clips_. These papers and projects impressive tag, classify and even caption each clip, with each comprising a single action or subject.

Today, we're going to explore a way to _continuously classify video as it's captured_, in an online system. Continuous classification allows us to solve all sorts of interesting problems in real-time, like understanding what's in front of a car for autonomous driving applications to understanding what's streaming on a TV. We'll attempt to do the latter using only open source software and uber-cheap hardware. Specifically, TensorFlow on a Raspberry Pi with a PiCamera.

We'll use a "naive" classification approach in this post (see next section), which will give us a relatively straightforward path to solving our problem and will form the basis for more advanced systems to explore later.

By the time we're done today, we should be able to classify what we see on our TV as either a football game or an advertisement, running on our Raspberry Pi.

Let's get to it!

### The intuition

Video is an interesting classification problem because it includes both temporal and spatial features. That is, at each frame within a video, the frame itself holds important information (spatial), as does the context of that frame relative to the frames before it in time (temporal).

We hypothesize that for many applications, using only spatial features is sufficient for achieving high accuracy. This approach has the benefit of being relatively simple, or at least minimal. It's naive because it ignores the information encoded between multiple frames of the video.

Since football games have rather distinct spatial features, we believe this method should work wonderfully for the task at hand.

### Method

We're going to collect data for offline training with a Raspberry Pi and a PiCamera. We'll point the camera at a TV and record 10 frames per second, or more specifically, save 10 jpegs every second, which will comprise our "video".

Here's the code for capturing our images:

Once we have our data, we'll use a convolutional neural network (CNN) to classify each frame with one of our labels: ad or football.

### Offline training and exploration

#### TensorFlow and Inception

CNNs are the state-of-the-art for image classification. And in 2016, it's essentially a solved problem. It feels crazy to say that, but it really is: Thanks in large part to Google->TensorFlow->Inception and the many researchers who came before it, there's very little low-level coding required for us when it comes to training a CNN for our continuous video classification problem.

Pete Warden at Google wrote an awesome blog post called [TensorFlow for Poets](https://petewarden.com/2016/02/28/tensorflow-for-poets/) that shows how to retrain the last layer of Inception with new images and classes. This is called transfer learning, and it lets us take advantage of weeks of previous training without having to train a complex CNN from scratch. Put another way, it lets us train an image classifier with a relatively small training set.

#### _Our training data_

We collected 20 minutes of footage at 10 jpegs per second, which amounted to 4,146 ad frames and 7,899 football frames. The next step is to sort each frame into two folders: football and ad. The name of the folders represent the labels of each frame, which will be the classes our network will learn to predict on when we retrain the top layer of the Inception v3 CNN.

This is essentially using the flowers method described in TensorFlow for Poets, applied to video frames.

To retrain the final layer of the CNN on our new data, we checkout the r0.11 tag from the [TensorFlow repo](https://github.com/tensorflow/tensorflow) and run the following command:
    
    
    python3 tensorflow/examples/image_retraining/retrain.py \       
        --bottleneck_dir=/home/harvitronix/blog/inception/bottlenecks \  
        --model_dir=/home/harvitronix/blog/inception/ \  
        --output_graph=/home/harvitronix/blog/retrained_graph.pb \  
        --output_labels=/home/harvitronix/blog/retrained_labels.txt \  
        --image_dir /home/harvitronix/blog/images/classifications/

Retraining the final layer of the network on this data takes about 30 minutes on my laptop with a GeForce GTX 960m GPU. At the completion of 4,000 training steps, our model reports an incredible 98.8% accuracy on the held out validation set! I'm not sure I could do much better using my eyes on the same data. As a point of reference, if the network had classified each frame as football, it would have achieved about 66% accuracy. So it seems to be working!

It's always a good idea to run some known data through a trained network to sanity check the results, so we'll do that here.

Here's the code we use to classify a single image manually through our retrained model:

And here are the results of spot checking individual frames:

### Simulated online classification

Before we transfer everything to our Pi and do this in real-time, let's use a different batch of recorded data and see how well we do on that set.

To get this dataset, and to make sure we don't have any data leakage into our training set, we separately record another 19 minutes of the football broadcast. This dataset amounted to 2,639 ad frames and 8,524 football frames.

We run each frame of this set through our classifier and achieve a true holdout accuracy score of 93.3%. Awesome!

Looks like we've validated our hypothesis that we can achieve high levels of accuracy while only considering spatial features. Impressive results, considering that we only used 20 minutes of training data! Thank you, Google, Pete, TensorFlow and all the folks who have developed CNNs over the years for your incredible work and contributions.

### Online classification

Great, so now we have our CNN trained and we know that we can classify each frame of our video with relatively high accuracy. How does it do on live TV, with always changing context?

For this, we load up our Raspberry Pi 3 with our newly trained model weights, turn on the PiCamera at 10 fps, and instead of saving the image, send it through our CNN to be classified.

We have to make some modifications to the code to classify in real time. The final result looks like this:

We also have to get TensorFlow running on the Pi. Sam Abrahams wrote up [excellent instructions](https://github.com/samjabrahams/tensorflow-on-raspberry-pi) for doing this, so I won't cover them again here.

After we install our dependencies, we run the program and… crap! Inception on the Raspberry Pi 3 can only classify one image every four seconds.

Okay, so we don't quite have the hardware yet to do 10fps, but this still feels like magic, so let's see how we do.

Flipping on Sunday Night Football and pointing our camera at the TV shows a remarkable job at classifying each moment as football or ad, once every few seconds. For the vast majority of the broadcast, we see our prediction come out true to life. So cool.

### Next steps

In all, our naive method worked remarkably well at continuous online video classification for this particular use case. But we know that we're only considering part of the information provided to us inherently in video, and so there must be room for improvement, especially as our datasets become more complex.

For that, we'll have to dive deeper. So in [the next post](https://medium.com/@harvitronix/continuous-video-classification-with-tensorflow-inception-and-recurrent-nets-250ba9ff6b85#.edhv7ysrx), we'll explore feeding the output of our CNN (both the final softmax layer and the pool layer, which gives us a 2,048-d feature vector of each image) to an LSTM RNN to see if we can increase our accuracy.

Spoiler alert: We can!

### Further reading

  * This is an amazing reference that will get you caught up with the state of CNNs for video: "[Deep Learning for Video Classification and Captioning](https://arxiv.org/pdf/1609.06782.pdf)"
  * This is a creative network that uses a hybrid approach: "[Modeling Spatial-Temporal Clues in a Hybrid Deep Learning Framework for Video Classification](https://arxiv.org/pdf/1504.01561v1.pdf)"
  * Another great paper, this one focused on CNN+LSTMs, similar to what we'll explore in the next post: "[Beyond Short Snippets: Deep Networks for Video Classification](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Ng_Beyond_Short_Snippets_2015_CVPR_paper.pdf)"

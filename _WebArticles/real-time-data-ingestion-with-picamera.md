# Real-Time Data Ingestion With PiCamera

_Captured: 2017-01-19 at 11:11 from [dzone.com](https://dzone.com/articles/picamera-ingest-real-time?edition=262904&utm_source=Daily%20Digest&utm_medium=email&utm_campaign=dd%202017-01-18)_

Access the survey results ['State of Industrial Internet Application Development'](https://dzone.com/go?i=124029&u=http%3A%2F%2Fgo.digital.ge.com%2FEvans-Data-Survey-Results.html%3Futm_source%3Ddzone%26utm_medium%3Dppc%26utm_content%3DEvans_Data_Survey%26utm_campaign%3D2016-09-GLOB-DG-HORZ-PREDIX-Free_Trial_Nurture_DZONE-Child_3PTY) to learn about latest challenges, trends and opportunities with Industrial IoT, brought to you in partnership with [GE Digital](https://dzone.com/go?i=124029&u=http%3A%2F%2Fgo.digital.ge.com%2FEvans-Data-Survey-Results.html%3Futm_source%3Ddzone%26utm_medium%3Dppc%26utm_content%3DEvans_Data_Survey%26utm_campaign%3D2016-09-GLOB-DG-HORZ-PREDIX-Free_Trial_Nurture_DZONE-Child_3PTY).

![Image title](https://dzone.com/storage/temp/4024547-jp2aface.png)

I found a cool utility called [JP2A](https://github.com/cslarsen/jp2a) that converts JPEGs to ASCII art, so I converted some PiCamera images to ASCII Art.

`/opt/demo/jp2a-master/src/jp2a`

`"http://hdfsnode:50070/webhdfs/v1/images/$@?op=OPEN"`

With that simple script, you can convert an image stored in HDFS to text.

![Image title](https://dzone.com/storage/temp/4024556-picamflow.png)

My main processing is done in Python, which activates the camera and retrieves still images, a burst, or videos.

To attach the camera to your Raspberry Pi 3B+, you just need to connect to two wires while you are powered down. Make sure you are grounded and have no static electricity, then plug them in. The package will show you which two wires which are to import. To install the Python code for the camera, read this install document for [2.7](http://picamera.readthedocs.io/en/release-1.10/install2.html). All you have to do is `pip install PiCamera`.

Raspberry Pis and other small devices often have cameras or can have camera's attached. Raspberry Pis have [cheap camera add-ons](https://www.raspberrypi.org/products/camera-module/) that can ingest still images and videos. Using a simple Python script, we can ingest images and then ingest them into our central Hadoop Data Lake. This is a nice, simple use case for connected data platforms with both data in motion and data at rest. This data can be processed in-line with Deep Learning Libraries like TensorFlow for image recognition and assessment. Using OpenCV and other tools we can process in motion and look for issues like security breaches, leaks, and other events.

The most difficult part is the Python code, which reads from the camera, adds a watermark, converts the image to bytes, sends it through MQTT, and then FTPs to an FTP server. I do both because networking is always tricky. You could also add if it fails to connect to either, store to a directory on a mapped USB drive. Once network returns send it out, it would be easy to do that with MiniFi which could read that directory.

![Image title](https://dzone.com/storage/temp/4024563-piccamnifiimage.png)

Once the file lands into the MQTT broker or FTP server, NIFI pulls it and bring it into the flow. I first store to HDFS for our data at rest permanent storage for future deep learning processing. I also run three processors to extra image metadata and then call JP2A to convert the image into an ASCII picture.

For the Python code, it's simple:
    
    
     return ''.join(random.choice(string.lowercase) for i in range(length))
    
    
    img_name = 'pi_image_{0}_{1}.jpg'.format(randomword(3),strftime("%Y%m%d%H%M%S",gmtime()))
    
    
    client.connect("cloudmqttiothoster", 14162, 60)
    
    
    message = '"image": {"bytearray":"' + byteArr + '"} } '
    
    
    print client.publish("image",payload=message,qos=1,retain=False)
    
    
        ftp.storbinary('STOR ' + img_name, open(img_name, 'rb'))

For an IoT use case, I grab the image and then FTP it to a cloud server as well as send an MQTT message via a cloud MQTT broker. You can transmit files in various means and these two are easy. You will need to use PIP to install libraries as necessary.

The IoT Zone is brought to you in partnership with [GE Digital](https://dzone.com/go?i=116927&u=http%3A%2F%2Fgo.digital.ge.com%2FPredix-Architecture-WP.html%3Futm_source%3Ddzone%26utm_medium%3Dppc%26utm_content%3DPredix_Architecture_Whitepaper%26utm_campaign%3D2016-09-GLOB-DG-HORZ-PREDIX-Free_Trial_Nurture_DZONE-Child_3PTY). Discover how IoT developers are using Predix to [disrupt traditional industrial development models](https://dzone.com/go?i=116927&u=http%3A%2F%2Fgo.digital.ge.com%2FPredix-Architecture-WP.html%3Futm_source%3Ddzone%26utm_medium%3Dppc%26utm_content%3DPredix_Architecture_Whitepaper%26utm_campaign%3D2016-09-GLOB-DG-HORZ-PREDIX-Free_Trial_Nurture_DZONE-Child_3PTY).

# Intelligent Door

_Captured: 2017-09-15 at 10:10 from [www.hackster.io](https://www.hackster.io/vijayenthiran/intelligent-door-e59113)_

![Intelligent Door](https://hackster.imgix.net/uploads/cover_image/file/117766/DSC_0109.png?auto=compress%2Cformat&w=900&h=675&fit=min)

The project demonstrates an intelligent door which sends out email notification to the owner when there is an intrusion. This is achieved by using ADXL345 accelerometer which detects the change in motion of the door and raspberry pi to communicate to the AWS IoT console. Based on the messages from the AWS IoT console, AWS SNS will send out email notification to the owner.

AWS IoT console's MQTT Protocol is used for achieving this. MQTT is a machine to machine messaging protocol widely used in Internet of Things projects. The protocol has MQTT Broker (Server) and MQTT Clients. In our case AWS IoT acts as a secure MQTT Broker and Raspberry pi acts as MQTT Client. MQTT follows publisher-subscriber model. A message published to a topic will be received in all clients which has subscribed to that topic. Hence two-way communication is easily possible with MQTT.

  * **AWS IoT Console:** Amazon Web Services recenlty launched support for the IoT. It is a very secured platform compared to the other open source and free platfroms. You will have to register your device first and download certificates before publishing the data to the cloud.
  * **AWS SNS Console: **SNS is used to send out push notification by various means (HTTP, Email, Mobile etc.) In this project Email notification is chosen as most of the users uses email application in their mobile. No separte application is required to trigger push notifcaiton.
  * **Raspberry Pi: **Popularly known as low-cost credit card sized computer is a simple yet powerful ARM based computer runs Linux operating system. The default raspbian OS comes with preinstalled popular programming languages such as C++, python etc. 

Raspberry Pi is very easy to setup. Follow this official [getting started guide](https://www.raspberrypi.org/help/quick-start-guide/), once done open terminal window. Before start coding, lets connect ADXL345 accelerometer to the Raspbbery Pi. The connection is simple. Connect VCC -- VCC, GND -- GND, SCL -- SCL, SDL -- SDL. Schematic is provided below:

![](https://hackster.imgix.net/uploads/image/file/117600/schematic.png?auto=compress%2Cformat&w=680&h=510&fit=max)

ADXL345 accelerometer communicate to the master device through I2C communication. I2C is not enabled in raspberry pi by default.

Run the following commands sequentially to install necessary libraries for I2C:
    
    
    $ sudo apt-get install python-smbus
    $ sudo apt-get install i2c-tools
    

We will have to enable the I2C in raspberry pi configuration window so that the I2C module loads by default.

The following steps will show you do that:

;

;

![](https://hackster.imgix.net/uploads/image/file/117622/2016-02-01%2000_35_25-Adafruit%20Learning%20System.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Then reboot the raspberry pi.

With the accelerometer connected type the following command in the terminal.
    
    
    $ sudo i2cdetect -y 1   
    

If you have made the connection correclty, you should get output like this:

![](https://hackster.imgix.net/uploads/image/file/117633/2016-02-01%2000_43_04-pi%40raspberrypi_%20~_aws-iot.png?auto=compress%2Cformat&w=680&h=510&fit=max)

53 says that the in the address 53 accelerometer in connected.

Create a new folder names aws-iot for this project by typing the following command.
    
    
    $ mkdir aws-iot
    $ cd aws-iot
    

Now download the pimoroni accelerometer library by entering the following command:
    
    
    $ curl https://raw.githubusercontent.com/pimoroni/adxl345-python/master/adxl345.py > adxl345.py
    

The library helps to reduce the complexity of interfacing the ADXL345 accelerometer.

The raspberry pi is going to communicate with the AWS server though MQTT protocol. So we need to install mqtt client library for python.
    
    
    $ sudo pip install paho-mqtt
    

Once you sign up for the Amazon Webservice select the AWS IoT console.

![](https://hackster.imgix.net/uploads/image/file/117658/2016-01-31%2023_10_22-.png?auto=compress%2Cformat&w=680&h=510&fit=max)

In order to connect a device to the AWS IoT, we need to create a resource in it.

![](https://hackster.imgix.net/uploads/image/file/117660/2016-01-31%2023_12_10-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Select Create Thing button

![](https://hackster.imgix.net/uploads/image/file/117663/2016-01-31%2023_14_28-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Give a name for your thing. Since we are going to connect raspberry pi, we will give the name as "raspberry_pi". No need to add any attributes. Press Create button.

![](https://hackster.imgix.net/uploads/image/file/117664/2016-01-31%2023_15_30-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Once you have created the thing, you can view it by either of the following two buttons.

![](https://hackster.imgix.net/uploads/image/file/117666/2016-01-31%2023_16_58-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

This will open a small window on the right. You can see that the Linked Certificate field is empty. We need to have a certificate and key to get a device connected. To generate these press connect a device button.

![](https://hackster.imgix.net/uploads/image/file/117668/2016-01-31%2023_19_34-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Although we are going to use Python as our programming language, you can generate the certificates and key by selecting the sdk as Node JS.

;

;

![](https://hackster.imgix.net/uploads/image/file/117670/2016-01-31%2023_21_05-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

In the raspberry pi, create a folder named in the aws-iot folder and place the downloaded files in it. I use WinSCP to achieve this.

![](https://hackster.imgix.net/uploads/image/file/117683/2016-01-31%2023_29_43-.png?auto=compress%2Cformat&w=680&h=510&fit=max)

In addition to the certificate and key files, aws also need certificate file from Symantec. Download that by running the following command in the cert folder.
    
    
    $ curl https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem  > rootCA.pem
    

I have placed my accelerometer in the door such that the x arrow in the acceleromter is facing top. With my orientation of the accelerometer when the door is at rest I get a negative values in the Z axis. When someone opens the door the Z axis values comes to a positive or zero and goes back to the negative values. If it happens so, I will publish a string "Intrusion detected" to the mqtt topic "home/door". The logic can be found in the attached code.

Run the file typing the following command. Make sure the file is inside the aws-iot folder.
    
    
    $ sudo python intrusionDetection.py 
    

AWS IoT has a console to view the mqtt message posted from the connected device.

Select MQTT Client in the top right corner of your dashboard.

![](https://hackster.imgix.net/uploads/image/file/117692/2016-02-01%2000_11_02-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Select Device Gateway connection and enter the client ID as raspberry_pi and press connect.

![](https://hackster.imgix.net/uploads/image/file/117695/2016-02-01%2000_11_34-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Once connected you will receive a notification like this.

![](https://hackster.imgix.net/uploads/image/file/117698/2016-02-01%2000_12_40-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Subscribe to the topic "home/door"

![](https://hackster.imgix.net/uploads/image/file/117699/2016-02-01%2000_13_04-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Once subscribed,when there is a intruder you will receive the message in the console.

![](https://hackster.imgix.net/uploads/image/file/117702/2016-02-01%2000_14_14-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Select AWS SNS from the services and press "get started" button:

![](https://hackster.imgix.net/uploads/image/file/117706/1.PNG?auto=compress%2Cformat&w=680&h=510&fit=max)

Select Create Topic:

![](https://hackster.imgix.net/uploads/image/file/117709/2016-02-01%2001_27_09-AWS%20SNS.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Give the desired Topic Name and Display name and press create topic

![](https://hackster.imgix.net/uploads/image/file/117712/2016-02-01%2001_29_12-AWS%20SNS.png?auto=compress%2Cformat&w=680&h=510&fit=max)

In the next screen, select Create Subscription button

![](https://hackster.imgix.net/uploads/image/file/117713/2016-02-01%2001_31_17-AWS%20SNS.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Select the protocol as Email and enter the target email ID.

![](https://hackster.imgix.net/uploads/image/file/117717/2016-02-01%2001_32_47-AWS%20SNS.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Once you have create the subscription, you will see that the status as pending confirmaton.

![](https://hackster.imgix.net/uploads/image/file/117718/2016-02-01%2001_35_46-AWS%20SNS.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Open the target email id and confirm the subscription:

;

;

![](https://hackster.imgix.net/uploads/image/file/117722/2016-02-01%2001_37_18-AWS%20Notification%20-%20Subscription%20Confirmation%20-%20vijayenthiran.s%40gmail.com%20-%20Gmail.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Once confirmed the subspriton refresh the SNS dashboard. You will see that the Subscription ID will be generated.

![](https://hackster.imgix.net/uploads/image/file/117725/2016-02-01%2001_40_11-AWS%20SNS.png?auto=compress%2Cformat&w=680&h=510&fit=max)

We have succefully configured the SNS. We have to create a rule in AWS IoT so that if we receive any message in the topic "home/door" it should be routed to the SNS.

Go to the AWS IoT Console and select "Create resource" and select "Create a rule" button.

;

;

![](https://hackster.imgix.net/uploads/image/file/117737/2016-02-01%2001_46_57-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Enter the name as "Intrusion_Rule". Enter the attirbute as " * " (as we didn't enter any attributes in our thing and enter the topic name as "home/door".

![](https://hackster.imgix.net/uploads/image/file/117741/2016-02-01%2001_49_48-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

In the Choose action dropdown select the option as "Send Message as a push notification"

![](https://hackster.imgix.net/uploads/image/file/117744/2016-02-01%2001_50_31-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

In the SNS Target, select "Intrusion"

![](https://hackster.imgix.net/uploads/image/file/117745/2016-02-01%2001_50_59-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

We have to create a role. Select create a role button. It will open a new tab and should take you to the IAM Management Console.

![](https://hackster.imgix.net/uploads/image/file/117750/2016-02-01%2001_55_50-IAM%20Management%20Console.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Press Allow, it will create a new role successfully and close the tab automatically.

Click on Add Action button and press create button.

;

;

![](https://hackster.imgix.net/uploads/image/file/117752/2016-02-01%2001_57_02-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

You can see that the Rule is added and Enabled in the dashboard.

![](https://hackster.imgix.net/uploads/image/file/117759/2016-02-01%2002_07_48-AWS%20IoT.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Now run the intrusionDetection.py file again in the raspberry pi. In addition to the MQTT messages, you will also receive email notification, when there is an intruder.

![](https://hackster.imgix.net/uploads/image/file/117760/2016-02-01%2002_10_01-AWS%20Notification%20Message%20-%20vijayenthiran.s%40gmail.com%20-%20Gmail.png?auto=compress%2Cformat&w=680&h=510&fit=max)

If you have email notification enabled in your mobile, you will also receive push notification in your mobile.

![](https://hackster.imgix.net/uploads/image/file/117765/Screenshot_2016-02-01-02-13-58.png?auto=compress%2Cformat&w=680&h=510&fit=max)

# Home Automation With a Raspberry Pi (Part 1)

_Captured: 2017-05-10 at 22:07 from [dzone.com](https://dzone.com/articles/home-automation-with-a-raspberry-pi-part-1?edition=298048&utm_source=Daily%20Digest&utm_medium=email&utm_campaign=dd%202017-05-10)_

With the emergence of IoT, we're trying to achieve advanced connectivity and ensure efficiency through connected devices and network sensors.

At Azilen, our recent work on the automation of home appliances through gesture recognition is one such example where we aim to control and automate home appliances such as air conditioners and televisions. We have achieved gesture recognition for implementing functionality like turning on and off, increasing and decreasing the temperature for air conditioners and turning on and off a television.

Through an extensive research, our team explored various feasible options for selecting the right platform and suitable libraries to make real-time computer vision possible for gesture recognition. From Omega, Chip, Arduino, and Raspberry Pi amongst other platforms, and from BoofCV, OpenIMAJ, MATLAB, OpenCV, and JavaCV, among other libraries, the team selected Raspberry Pi and leading open source library Open CV and its Java port JavaCV as the right platform to make computer vision and image processing possible.

The library has more than 2,500 optimized algorithms, which include a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms. These algorithms can be used to detect and recognize faces, identify objects, classify human actions in videos, track camera movements, track moving objects, etc.

This blog talks about the complete step by step guide to setup OpenCV and JavaCV on Raspberry Pi.

![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/01/001.jpg)

**Note: **We assume that you have pre-installed the latest Raspbian operating system on your Raspberry Pi. If not please follow [this link](https://www.raspberry%20pi.org/downloads/noobs/) to install latest the Raspbian on your Raspberry Pi.

All required packages such as Maven, Ant, Git should be installed in the system.

## **Installation Guide**

Please follow steps below to setup OpenCV and JavaCV on Raspberry Pi

### **Step 1: Update Raspbian**

You need compiler tools, so update and upgrade the Raspberry Pi (Raspbian Linux) with the latest available packages.

Get all the compiler tools and video libraries using the commands below in your Terminal window, one by one:

### **Step 2: Install Dependencies**

OpenCV requires a few external dependencies for it to be able to run, so you need to install all the required dependencies in the following order, again one by one:

**Note: **If some of the libraries fail to download, then try to look for a different version of the library using apt-cache search, as some of these libraries are not in the Raspbian repository anymore or are available with newer versions. For example:

### **Step 3: Download the OpenCV Source Code and Install**

Now that we have our dependencies installed, let's grab the OpenCV archive version 2.4.13 from the official OpenCV repository.

**Note:** As future versions of OpenCV are released, you can replace 3.1.0, 3.2.0 with the latest version number, but this guide is focused around version 2.4.13.

Uncompress the downloaded source file. Move it into an uncompressed directory and create a new directory named "release" inside it. Run the commands below to configure, compile, and install OpenCV. Please note that compilation will take approximately 4-5 hours, so grab yourself a nice pizza and relax!

After cmake is done, the JAR file will be under the release/bin/ and release/lib/ folders. Since we built version 2.4.13, the generated file will be named OpenCV-2413.jar and libOpenCV_java.so.

Both generated files are required in the build path for any Java-based project with OpenCV. Meanwhile, libOpenCV_java.so is required for any C/C++ based project with OpenCV.

**Note:** If you get any Linker error or java.library.path issue, you need to provide a path for the generated OpenCV JAR file with **java -jar cmd **using -**Djava.library.path**= 'path to OpenCV libs', or you **can export the LD_LIBRARY_PATH** system variable with the lib path. You can also add an export command to **.bashcr file as well**

### **Step 4: Compile JavaCV/javaCPP**

Now that we have compiled and installed OpenCV 2.4.13 on our Raspberry Pi, we can compile and install JavaCV and JavaCPP on it as well! In order to do that, you need to have Java, Maven, and Git installed on the Raspberry Pi.

The compilation of JavaCV and javaCPP does not run with all versions of Java (such as Oracle JDK 8). It runs correctly with OpenJDK 7, which needs to be installed temporarily for this purpose if it's not already installed. There might be multiple versions of Java installed. It needs to be ensured that OpenJDK 7 is the default selected Java version. Please run the following commands in your Terminal window to install OpenJDK.

**Install OpenJDK 7 and select OpenJDK 7 as default Java version:**

For JavaCV/javaCPP, Maven is needed. The source will be downloaded **using Git**.

Once the source is downloaded, reset the sources to the old version, 0.7 of JavaCV and javaCPP, as they are the most recent working ones for our purpose. Two modifications to the source files need to be performed to run on the Raspberry Pi and these will be done with a sed command. Afterwards, the compilation can be started.

Run the following commands in your Terminal window (follow the steps in order):

And that's it. You have successfully installed JavaCV/JavaCPP on your Raspberry Pi. The next step is to verify your installation.

### **Step 5: Testing your OpenCV/JavaCV Installation**

Open your favorite editor on the Raspberry Pi (VI/NANO/PageLeaf).

Create a new Java file as shown below and save the file:

**Note:** Raspbian ships the latest Oracle JDK version with it. Please use the command 'whereis java' to find out the location of the Oracle JDK and make it the default Java version.  
Now compile this file using Oracle JDK version >= 7. Type the following commands into your Terminal to compile and run this Java code.

The Java code output must be as below:

![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/01/img1.jpg)

Congrats! You have a brand new, fresh install of OpenCV/JavaCV on your Raspberry Pi. And I'm sure you're just itching to leverage your Raspberry Pi to build some awesome computer vision apps.

## **So, What's Next?**

In our upcoming post, we aim to write a complete guide for automating an air conditioner and a television for implementing features through gesture recognition.

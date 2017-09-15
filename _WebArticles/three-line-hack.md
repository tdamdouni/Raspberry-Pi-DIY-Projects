# Three Line Hack

_Captured: 2017-08-24 at 23:30 from [www.tecoed.co.uk](http://www.tecoed.co.uk/python-ocr.html)_

## What is it?

Using Python and a Raspberry Pi plus **three lines of code **you can hack a picture or image and scrap all the text into the console window. The program uses OCR Optical Character Recognition, a technology that enables you to convert different types of documents, such as scanned paper documents, PDF files or images captured by a digital camera into editable and searchable data. This code uses images in a range of file types, jpeg and png.

## 1\. Getting Started

This is a really easy hack which basically requires three lines of code and a couple of additional libraries. Firstly update your Raspberry Pi:

In the LX Terminal type:  
_**sudo apt-get update**_  
_**sudo apt-get upgrade**_

Then install Google's Tessaract OCR software by typing:  
**_sudo apt-get install tesseract-ocr_**

![Picture](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/13461_orig.png)

> _(tesseract-ocr is a project Google have been working on full details are available here, it contains extra codes and developments)_

Next install the Python Wrapper for the Tesseract-OCR software - this basically enables you to program the OCR using Python Code.

In the LX Terminal type using PIP:  
**_sudo pip install pytesseract_**

![Picture](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/3772729_orig.png)

The final part is to install the Python Imaging Library PIL  
**_sudo apt-get install python-imaging  
sudo apt-get install python-imaging-tk_**

Then reboot the Pi  
**_sudo reboot_**

## 2\. The Code

Now download or create an image which contains text, the two below worked very well. I also tried a screen shot of a website and had about 70% success, there were some random characters and issues.

In the LX Terminal type  
**_sudo idle_**

Open a new Python window and add the following code  
**_import Image  
import pytesseract  
print pytesseract.image_to_string(Image.open('test.png'))_**

Where **test** is the name of the picture you which to scan, I tried jpg and png and they both worked well. Save the program into the same folder as the pictures and hit F5 to run. It really is that simple!

![Picture](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/7201390_orig.png)

![](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/4688836.jpg)

![](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/878505.jpg)


__ __ __ __

* * *

## What is it?

* * *

Using Python and a Raspberry Pi plus **three lines of code **you can hack a picture or image and scrap all the text into the console window.  The program uses OCR Optical Character Recognition, a technology that enables you to convert different types of documents, such as scanned paper documents, PDF files or images captured by a digital camera into editable and searchable data.  This code uses images in a range of file types, jpeg and png. 

* * *

## 1\. Getting Started

* * *

This is a really easy hack which basically requires three lines of code and a couple of additional libraries.  Firstly update your Raspberry Pi:    
  
In the LX Terminal type:  
_**sudo apt-get update**_  
_**sudo apt-get upgrade**_  
  
Then install Google's Tessaract OCR software by typing:  
**_sudo apt-get install tesseract-ocr_**  

[ ![Picture](/uploads/1/4/2/4/14249012/13461_orig.png) ](/uploads/1/4/2/4/14249012/13461_orig.png)

_(tesseract-ocr is a project Google have been working on full details are available [here, it contains extra codes and developments) ](https://code.google.com/p/python-tesseract/issues/detail?id=60)_

Next install the Python Wrapper for the Tesseract-OCR software -  this basically enables you to program the OCR using Python Code.  
  
In the LX Terminal type using PIP:  
**_sudo pip install pytesseract_**  

[ ![Picture](/uploads/1/4/2/4/14249012/3772729_orig.png) ](/uploads/1/4/2/4/14249012/3772729_orig.png)

  
The final part is to install the Python Imaging Library PIL  
**_sudo apt-get install python-imaging  
sudo apt-get install python-imaging-tk_**  
  
Then reboot the Pi  
**_sudo reboot_**  
  

## Three Line Hack

* * *
* * *

## 2\. The Code

* * *

Now download or create an image which contains text, the two below worked very well.  I also tried a screen shot of a website and had about 70% success, there were some random characters and issues.  
  
In the LX Terminal type  
**_sudo idle_**  
  
Open a new Python window and add the following code  
**_import Image  
import pytesseract  
print pytesseract.image_to_string(Image.open('test.png'))_**  
  
Where **test** is the name of the picture you which to scan, I tried jpg and png and they both worked well.  Save the program into the same folder as the pictures and hit F5 to run.  It really is that simple!  

[ ![Picture](/uploads/1/4/2/4/14249012/7201390_orig.png) ](/uploads/1/4/2/4/14249012/7201390_orig.png)

![](/uploads/1/4/2/4/14249012/4688836.jpg)

![](/uploads/1/4/2/4/14249012/878505.jpg)

**Some other Tesseract-OCR Resource Links:**  

  1. [Google Tesseract-OCR](https://code.google.com/p/pytesser/wiki/README)  
  2. [Python Wrapper on GitHub](https://github.com/madmaze/pytesseract)
  3. [Other Projects](https://rdmilligan.wordpress.com/2014/11/21/ocr-on-raspberry-pi/)

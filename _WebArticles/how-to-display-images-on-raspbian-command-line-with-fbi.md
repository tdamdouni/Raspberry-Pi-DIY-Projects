# How to Display Images on Raspbian Command Line with fbi

_Captured: 2017-05-06 at 15:54 from [www.raspberrypi-spy.co.uk](http://www.raspberrypi-spy.co.uk/2017/02/how-to-display-images-on-raspbian-command-line-with-fbi/)_

![FBI command line photo viewer](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2017/02/fbi_01-702x336.jpg)

There maybe times when you want to view a photo from the Raspbian command line. Previously I had recommended [using "fim" to display images on the command line](http://www.raspberrypi-spy.co.uk/2014/09/how-to-display-images-on-raspbian-command-line/) but this is no longer available from the Raspbian repository. Instead you can use the utility that it was based on called "fbi". It doesn't have the ascii art capability of fim but is useful for images and slideshows.

Fbi displays the specified file(s) on the linux console using the framebuffer device. PhotoCD, jpeg, ppm, gif, tiff, xwd, bmp, png and webp formats are supported natively.

## Install fbi

To install fim use the following commands :
    
    
    sudo apt-get update
    sudo apt-get -y install fbi

## Use fbi

To display a single image with the "auto-zoom" option use :
    
    
    fbi -a myphoto.jpg

Press ESC to return to the command line.

To display all the images in the current directory use the following command :
    
    
    fbi -a *.jpg

The PageUp/PageDown keys can be used to cycle through the images selected by the "*.jpg" filter.

To create a slideshow you can use :
    
    
    fbi -a -t 5 *.jpg

This will cycle through all the images with an interval of 5 seconds.

## Command line options

Here are some of the more useful command line options :
    
    
    -h Print usage info.
    -V Print fbi version number.
    -l file Read image filelist from file.
    -a Enable autozoom
    -v Be verbose: enable status line on the bottom of the screen.
    -u Randomize the order of the filenames.
    -e Enable editing commands.
    -p Preserve timestamps (when editing images).
    -t sec Load next image after sec seconds without any keypress (i.e.slideshow).
    -1 Don't loop (only use with -t).
    -g n Gamma correction. Default is 1.0.

Generally they are used between "fbi" and the image file name(s).

For example this will play a slideshow of all images in a random order with 4 seconds between each image. The images will be auto-scaled :
    
    
    fbi -a -u -t 4 *.jpg

## Keyboard Controls

Pressing h while viewing a photo will bring up a list of keyboard commands you can use :

**Scrolling**
    
    
    LEFT_ARROW, RIGHT_ARROW, UP_ARROW, DOWN_ARROW
     Scroll large images.
    
    PREV_SCREEN, k
     Previous image.
    
    NEXT_SCREEN, SPACE, j
     Next image.
    
    ig Jump to image #i.

**Zoom**
    
    
    a  Autozoom.
    +  In.
    -  Out.
    is  Set zoom to i%.

**Other**
    
    
    ESC  Quit
    q  Quit
    v  Toggle status line.
    h  Display textbox with brief help.
    i  Display textbox with some EXIF info.
    p  Pause the slideshow (if started with -t, toggle).

**Edit mode**  
Fbi also provides some very basic image editing facilities. You have to start fbi with the -e switch to use them.
    
    
    D  Delete image.
    r  Rotate 90 degrees clockwise.
    l  Rotate 90 degrees counter-clock wise.
    x  Mirror image vertically (top / bottom).
    y  Mirror image horizontally (left to right).

The delete function actually wants a capital letter D, thus you have to type Shift+d. This is done to avoid deleting images by mistake because there are no safety bells: If you ask fbi to delete the image, it will be deleted with‐  
out questions asked.

The rotate function actually works for JPEG images only. It does a lossless transformation of the image.

## EXIF Information

The photos EXIF information can be displayed by pressing i :

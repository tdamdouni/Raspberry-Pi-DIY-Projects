# Minecraft Photobooth

_Captured: 2017-05-04 at 20:01 from [www.raspberrypi.org](https://www.raspberrypi.org/learning/minecraft-photobooth/worksheet/)_

Create a working photobooth in Minecraft: when the player enters the photobooth it triggers the camera module and takes their picture. Don't forget to smile!

## Connect the camera

Before booting your Pi, you'll need to connect the camera. You can find instructions on how to do this on the [camera module setup](https://www.raspberrypi.org/help/camera-module-setup/) page.

## Importing the Minecraft and PiCamera Modules

The first thing you need to do is import the Minecraft API (Application Programming Interface). This enables you to connect to Minecraft and use Python to code. You also need to import the PiCamera module to control the camera and the time module to add a small delay between taking the photo and then taking the next photo.

  1. Open Minecraft from the application menu; enter an existing world or create a new one.

  2. Move the Minecraft window to one side of the screen.

You'll need to use the `Tab` key to take your mouse's focus away from the Minecraft window to move it. You'll need this later when you switch between the Minecraft and Python windows.

  3. Open Python 3 from the applications menu:

![Open Python 3](https://www.raspberrypi.org/learning/minecraft-photobooth/images/python3-app-menu.png)

This will open up the Python IDLE code editor which you will use to write the photobooth program.

  4. Click `New > Window` to open a new window.

  5. Enter the code shown below:
    
        from mcpi.minecraft import Minecraft
    from picamera import PiCamera
    from time import sleep
    
    mc = Minecraft.create()
    camera = PiCamera()
    
    mc.postToChat("Hello world")

  6. Save with `Ctrl + S` and run the program with `F5`. You should see the message "Hello world" appear in the Minecraft world.

## Testing the camera module

Next, you'll write some code to test the camera.

  1. Add the following lines to the end of your program:
    
        camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/selfie.jpg')
    camera.stop_preview()

We have set the camera to show a two second preview so that you can strike your pose and smile before the picture is taken. The image is stored as a file called `selfie.jpg` in your home directory.

  2. Save and run your program to take a picture!

  3. Open the File Manager to view the picture you took.

## Building a photobooth

Now you need to create a photobooth in the Minecraft environment. This is done manually and the photobooth can be built whereever you want to locate it.

Using any block type, build your photobooth. It can be any shape you like, but it should have at least one block width of free space inside so that the player can enter, like a door or gate.

![Photobooth](https://www.raspberrypi.org/learning/minecraft-photobooth/images/photobooth.png)

Once you have created your photobooth, you need to be able to move your player inside and onto the trigger block. This is the block that the player stands on to run the function that you wrote in step 1, which will trigger the camera. In the Minecraft environment, your position is given in reference to the `x`, `y`, and `z` axis. Look at the top left of the window and you will see the `x`, `y`, `z` co-ordinates of your player, for example `10.5`, `9.0`, `-44.3`. Assuming you are still in the photobooth then these are also the `x`, `y`, `z` co-ordinates of the 'trigger' block in your photobooth.

  1. Walk into your photobooth

  2. Record the `x`, `y`, `z`, co-ordinates of your camera 'trigger' block.

## Finding your position

When you are playing Minecraft, your program will need to verify that you are inside the photobooth. If you are, then it will trigger the `take_the_pic` function and take a picture with the camera. To do this, Minecraft needs to know where you are in the world.

To find your position, you use the code, `x, y, x = mc.player.getPos()`. This saves the `x`, `y`, and `z` position of your player into the variables `x`, `y`, and `z`. You can then use `print(x)` to print the `x` value, or `print(x, y, z)` to see them all. Now you know the position of the player, you can test to see if they are in the photobooth. As we're using Minecraft we can also use `mc.postToChat` to send the coordinates to the Minecraft window.

  1. Change the message "Hello world" to "Find the photobooth" after the `Minecraft.create()` line like so:
    
        mc = Minecraft.create()
    
    mc.postToChat("Find the photobooth")

  2. Add to the end of your code:
    
        while True:
        x, y, z, = mc.player.getPos()
        mc.postToChat((x, y, z))

  3. Save and run the code and you'll see your coordinates posted to the Minecraft window.

  4. Focus on the Python window and press `Ctrl + C` to stop the code running.

## Testing whether you are in the Photobooth

At this point we have a photobooth, the coordinates of the trigger block, and code to control the camera module and take a picture. The next step is to test whether the program identifies when you are in the photobooth. To do this we must create a loop which checks if your player's co-ordinates match the trigger block coordinates. If they do, then you are standing in the photobooth. To do this we use a simple `if` statement, which we call a conditional.

  1. Change the lines inside your `while` loop to match the code below:
    
        while True:
        x, y, z = mc.player.getPos()
    
        sleep(3)
    
        if x >= 10.5 and y == 9.0 and z == -44.3:
            mc.postToChat("You are in the photobooth!")

Ensure the coordinates you enter are the location of your own photobooth.

  2. Save and run your code to test it: walk into your photobooth and you should see the message "You are in the photobooth!" in the Minecraft window.

You will note that the `if` statement checks if `x` value is greater than or equal to `10.5`: this is ensure that it picks up the block as it could have a value of `10.6`. Remember to replace the `x`, `y`, and `z` values with the values from your photobooth.

## Putting it all together

Now you have a working photobooth we need to add the camera module to take a picture. We will add a quick reminder to smile and then call the camera capture code.

  1. Add the instructions to send messages to Minecraft and the call to `capture()` inside your `if` statement:
    
        if x >= 10.5 and y == 9.0 and z == -44.3:
        mc.postToChat("You are in the Photobooth!")
        sleep(1)
        mc.postToChat("Smile!")
        sleep(1)
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/selfie.jpg')
        camera.stop_preview()
    
    sleep(3)

This will keep checking your location. When your location matches that of the photobooth, it will take a picture with the camera.

## What next?

  1. Try adding a specific block which triggers the camera

  2. Try adding further blocks to control camera settings such as taking a video or applying a filter

  3. Try using blocks to start and stop the camera recording a video

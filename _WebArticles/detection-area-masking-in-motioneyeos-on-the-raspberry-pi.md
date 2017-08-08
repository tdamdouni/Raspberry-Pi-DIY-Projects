# Detection Area Masking in motionEyeOS on the Raspberry Pi

_Captured: 2017-08-08 at 17:55 from [www.raspberrypi-spy.co.uk](http://www.raspberrypi-spy.co.uk/2017/04/detection-area-masking-in-motioneyeos-raspberry-pi/)_

![motionEyeOS Logo and Pi Camera](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2017/04/pi_camera_module_motioneyeos_logo-702x336.jpg)

Now that I've got [a few motionEyeOS cameras](http://www.raspberrypi-spy.co.uk/2017/04/raspberry-pi-zero-w-cctv-camera-with-motioneyeos/) working around the house I've made a few tweaks to optimise the events they capture. They are both in areas that capture movement from plants and animals and this motion can create lots of unnecessary images.

In order to reduce these "false positives" you can create a "mask" which tells motionEyeOS to ignore movement in certain areas of the image.

Here is the original view from one of my cameras. The trees on the other side of the fence move in the wind and cause a large amount of movement in the frame.

To solve my tree problem I decide to create a "mask".

Within the settings panel of the web interface you can find the mask settings under "Motion Detection". Turn the "Mask" "ON", set the "Mask Type" to "Editable" and click "Edit Mask".

A grid will be overlaid on the camera image. By clicking on the grid boxes you can turn them black. Clicking a black box will clear it. In my example I've defined an area of black boxes to cover the trees.

Clicking "Save Mask" will save the mask pattern. Click the "Apply" button at the top of the screen to enable the mask.

Movement in the masked area will now be ignored. In this case it stopped the trees generating movement events and reduced the number of images the system was storing every day.

Clicking "Clear Mask" will reset all the black boxes so you can either have no mask or start again if you need to redo the mask.

One important thing to remember when defining masks is that it will effect all movement in that black box. In my example I'm interested in the trees by the fence but it will also affect any movement in that whole rectangle. This might include someone climbing over the fence. They wouldn't trigger the camera until they dropped into the un-masked area on this side of the fence.

The mask will also affect any movement between the camera and the masked area. If a ball came over the fence it would be invisible all the while it remained in the masked area. It's always worth testing your camera still detects movement in the areas you expect. For example a person walking through the frame.

All my motionEyeOS based projects are listed under [the motionEyeOS tag](http://www.raspberrypi-spy.co.uk/tag/motioneyeos/).

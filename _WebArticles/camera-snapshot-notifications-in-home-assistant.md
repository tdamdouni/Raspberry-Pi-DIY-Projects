# Camera snapshot notifications in Home Assistant

_Captured: 2017-10-29 at 13:33 from [seanb.co.uk](https://seanb.co.uk/2017/10/camera-snapshot-notifications-in-home-assistant/)_

If you have a camera set up in Home Assistant, a common requirement is to be able to grab a snapshot in response to an event. You might want to grab a snapshot when motion is detected or your [doorbell rings](https://seanb.co.uk/2017/08/cheap-and-cheerful-doorbell-automation/).

The simple approach is to use the wget command to grab the image and save it to a file.

You could go direct to the camera, but to do that you'd need to set up a separate script for each camera. The script would have to include the URL of the camera and any authentication needed. That seems like an unnecessary duplication of effort if you already have the camera set up in Home Assistant.

Instead, you can set up a command component to grab the current image from the camera entity in Home Assistant. The camera entities have an attribute called entity_picture that points to the URL of the current image. You can use wget to grab this URL to a file.

Note that you can't simply hardcode the URL into a script because the token parameter in the URL will change. You need to grab the attribute value when you want the picture.

First set up a shell command component in your main configuration.yaml file that takes two arguments - a filename and a URL - and grabs the URL into the file:

`shell_command:``take_snapshot: 'wget -O {{filename }} {{ url }}'`

You can now call that command as an action in your automation:

`action:``\- service: shell_command.take_snapshot``data_template:``url: 'http://localhost:8123{{ states.camera.mjpeg_camera.attributes.entity_picture }}'``filename: '/tmp/snapshot.jpg'`

Now you have a snapshot image that you can use for notifications and the great thing is that it works for any camera that you can view in Home Assistant - you just need to change the entity id that you use to grab the picture attribute.

What if you want to show the snapshot in the front end? Home Assistant has a persistent_notification component that can show messages in the front end until you dismiss them, but unfortunately it doesn't have an option to add an image to the notification.

There is a workaround using group visibility.

First of all, define a camera using the local_file platform to point to your snapshot image.

`\- platform: local_file``file_path: /tmp/snapshot.jpg``name: "Doorbell"`

Put this in a group:

`doorbell_notification:``name: Doorbell``entities:``\- camera.doorbell`

You'll want to put the group definition at the top of your group.yaml file as groups are displayed in the order that they're defined in the file. Create an automation to run on startup to hide the group - there doesn't seem to be a way default groups to hidden:

`\- alias: 'Hide doorbell snapshot on startup'``trigger:``\- platform: homeassistant``event: start``action:``\- service: group.set_visibility``entity_id: group.doorbell_notification``data:``visible: False`

When the event occurs, you need to set up an automation to do three things. First grab the snapshot as above, then create a persistent notification and finally show your hidden group. For example, I've extended my doorbell notification:

`\- alias: 'Show snapshot when doorbell rings'``trigger:``\- platform: event``event_type: signal_received``event_data:``entity_id: sensor.doorbell_sound``action:``\- service: shell_command.take_snapshot``data_template:``url: 'http://localhost:8123{{ states.camera.mjpeg_camera.attributes.entity_picture }}'``filename: '/tmp/snapshot.jpg'``\- service: persistent_notification.create``data: ``message: "Doorbell rung"``title: "Notification"``notification_id: "doorbell"``\- service: group.set_visibility``entity_id: group.doorbell_notification``data:``visible: True`

You should then get a notification and see your snapshot when the doorbell rings:

![](https://seanb.co.uk/wp-content/uploads/2017/10/doorbell-snapshot.png)

Obviously I'm using a dummy picture here

You'll want the snapshot to disappear when you dismiss the notification, and that's where the notification_id comes in. If you use the ID an entity will be created named persistent_notification.<notification_id>.

You can then trigger an automation based on the state of that entity:

`\- alias: 'Dismiss doorbell notification'``trigger:``platform: state``entity_id: persistent_notification.doorbell``from: "Doorbell rung"``action:``\- service: group.set_visibility``entity_id: group.doorbell_notification``data:``visible: False`

You'll notice that this looks for the specific text of the notification. When the notification appears the state changes from "None" to the notification text and when the notification is dismissed the state changes to "None". Unfortunately looking for a state change to "None" doesn't work - the entity is destroyed when you dismiss the notification. I should point out that there might be a better way of doing this - I've just found a way that works.

This method works well if you have a default view set up in Home Assistant. A default view replaces the home tab, allowing you to customise the home page. Home Assistant creates a large number of entities that you might not need to see in the front end, and it's much easier to use a default view than to individually customise each entity to hide it.

If you're not using a default view you may need to put the snapshot camera in another group on a separate tab, otherwise when you hide the group the camera will appear anyway - according to the [docs](https://home-assistant.io/docs/configuration/group_visibility/): "If a sensor belongs to only one group and that group is hidden, the sensor will "jump" to the top of the web interface. Add the sensor to an additional (visible) group if you do not want this to happen".

This is just one approach. For another approach, using a Pi camera and MQTT, see Robin Cole's excellent write up at [hackster.io](https://www.hackster.io/robin-cole/pi-camera-doorbell-with-notifications-408d3d).

in [Home Automation](https://seanb.co.uk/category/home-automation/)

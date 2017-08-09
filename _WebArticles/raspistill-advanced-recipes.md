# 4. Advanced Recipes

_Captured: 2017-05-10 at 22:24 from [picamera.readthedocs.io](http://picamera.readthedocs.io/en/release-1.13/recipes2.html#web-streaming)_

![_images/yuv420.svg](http://picamera.readthedocs.io/en/release-1.13/_images/yuv420.svg)


    print('Sent %d images in %d seconds at %.2ffps' % (
        output.count, finish-start, output.count / (finish-start)))
    

The above script achieves 30fps with ease.

## 4.10. Web streaming

Streaming video over the web is surprisingly complicated. At the time of writing, there are still no video standards that are universally supported by all web browsers on all platforms. Furthermore, HTTP was originally designed as a one-shot protocol for serving web-pages. Since its invention, various additions have been bolted on to cater for its ever increasing use cases (file downloads, resumption, streaming, etc.) but the fact remains there's no "simple" solution for video streaming at the moment.

If you want to have a play with streaming a "real" video format (specifically, MPEG1) you may want to have a look at the [pistreaming](https://github.com/waveform80/pistreaming/) demo. However, for the purposes of this recipe we'll be using a much simpler format: MJPEG. The following script uses Python's built-in `[http.server`](https://docs.python.org/3.4/library/http.server.html#module-http.server) module to make a simple video streaming server:
    
    
    import io
    import picamera
    import logging
    import socketserver
    from threading import Condition
    from http import server
    
    PAGE="""\
    <html>
    <head>
    <title>picamera MJPEG streaming demo</title>
    </head>
    <body>
    <h1>PiCamera MJPEG Streaming Demo</h1>
    <img src="stream.mjpg" width="640" height="480" />
    </body>
    </html>
    """
    
    class StreamingOutput(object):
        def __init__(self):
            self.frame = None
            self.buffer = io.BytesIO()
            self.condition = Condition()
    
        def write(self, buf):
            if buf.startswith(b'\xff\xd8'):
                # New frame, copy the existing buffer's content and notify all
                # clients it's available
                self.buffer.truncate()
                with self.condition:
                    self.frame = self.buffer.getvalue()
                    self.condition.notify_all()
                self.buffer.seek(0)
            return self.buffer.write(buf)
    
    class StreamingHandler(server.BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.send_response(301)
                self.send_header('Location', '/index.html')
                self.end_headers()
            elif self.path == '/index.html':
                content = PAGE.encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(content))
                self.end_headers()
                self.wfile.write(content)
            elif self.path == '/stream.mjpg':
                self.send_response(200)
                self.send_header('Age', 0)
                self.send_header('Cache-Control', 'no-cache, private')
                self.send_header('Pragma', 'no-cache')
                self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
                self.end_headers()
                try:
                    while True:
                        with output.condition:
                            output.condition.wait()
                            frame = output.frame
                        self.wfile.write(b'--FRAME\r\n')
                        self.send_header('Content-Type', 'image/jpeg')
                        self.send_header('Content-Length', len(frame))
                        self.end_headers()
                        self.wfile.write(frame)
                        self.wfile.write(b'\r\n')
                except Exception as e:
                    logging.warning(
                        'Removed streaming client %s: %s',
                        self.client_address, str(e))
            else:
                self.send_error(404)
                self.end_headers()
    
    class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
        allow_reuse_address = True
        daemon_threads = True
    
    with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
        output = StreamingOutput()
        camera.start_recording(output, format='mjpeg')
        try:
            address = ('', 8000)
            server = StreamingServer(address, StreamingHandler)
            server.serve_forever()
        finally:
            camera.stop_recording()
    

Once the script is running, visit `http://your-pi-address:8000/` with your web-browser to view the video stream.

## 4.11. Capturing images whilst recording

The camera is capable of capturing still images while it is recording video. However, if one attempts this using the stills capture mode, the resulting video will have dropped frames during the still image capture. This is because images captured via the still port require a mode change, causing the dropped frames (this is the flicker to a higher resolution that one sees when capturing while a preview is running).

However, if the _use_video_port_ parameter is used to force a video-port based image capture (see [Rapid capture and processing](http://picamera.readthedocs.io/en/release-1.13/recipes2.html)) then the mode change does not occur, and the resulting video should not have dropped frames, assuming the image can be produced before the next video frame is due:
    
    
    import picamera
    
    with picamera.PiCamera() as camera:
        camera.resolution = (800, 600)
        camera.start_preview()
        camera.start_recording('foo.h264')
        camera.wait_recording(10)
        camera.capture('foo.jpg', use_video_port=True)
        camera.wait_recording(10)
        camera.stop_recording()
    

The above code should produce a 20 second video with no dropped frames, and a still frame from 10 seconds into the video. Higher resolutions or non-JPEG image formats may still cause dropped frames (only JPEG encoding is hardware accelerated).

## 4.12. Recording at multiple resolutions

The camera is capable of recording multiple streams at different resolutions simultaneously by use of the video splitter. This is probably most useful for performing analysis on a low-resolution stream, while simultaneously recording a high resolution stream for storage or viewing.

The following simple recipe demonstrates using the _splitter_port_ parameter of the `[start_recording()`](http://picamera.readthedocs.io/en/release-1.13/api_camera.html) method to begin two simultaneous recordings, each with a different resolution:
    
    
    import picamera
    
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.framerate = 30
        camera.start_recording('highres.h264')
        camera.start_recording('lowres.h264', splitter_port=2, resize=(320, 240))
        camera.wait_recording(30)
        camera.stop_recording(splitter_port=2)
        camera.stop_recording()
    

There are 4 splitter ports in total that can be used (numbered 0, 1, 2, and 3). The video recording methods default to using splitter port 1, while the image capture methods default to splitter port 0 (when the _use_video_port_ parameter is also True). A splitter port cannot be simultaneously used for video recording and image capture so you are advised to avoid splitter port 0 for video recordings unless you never intend to capture images whilst recording.

New in version 1.3.

## 4.13. Recording motion vector data

The Pi's camera is capable of outputting the motion vector estimates that the camera's H.264 encoder calculates while generating compressed video. These can be directed to a separate output file (or file-like object) with the _motion_output_ parameter of the `[start_recording()`](http://picamera.readthedocs.io/en/release-1.13/api_camera.html) method. Like the normal _output_ parameter this accepts a string representing a filename, or a file-like object:
    
    
    import picamera
    
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 30
        camera.start_recording('motion.h264', motion_output='motion.data')
        camera.wait_recording(10)
        camera.stop_recording()
    

Motion data is calculated at the [macro-block](https://en.wikipedia.org/wiki/Macroblock) level (an MPEG macro-block represents a 16x16 pixel region of the frame), and includes one extra column of data. Hence, if the camera's resolution is 640x480 (as in the example above) there will be 41 columns of motion data (), in 30 rows ().

Motion data values are 4-bytes long, consisting of a signed 1-byte x vector, a signed 1-byte y vector, and an unsigned 2-byte SAD ([Sum of Absolute Differences](https://en.wikipedia.org/wiki/Sum_of_absolute_differences)) value for each macro-block. Hence in the example above, each frame will generate 4920 bytes of motion data (). Assuming the data contains 300 frames (in practice it may contain a few more) the motion data should be 1,476,000 bytes in total.

The following code demonstrates loading the motion data into a three-dimensional numpy array. The first dimension represents the frame, with the latter two representing rows and finally columns. A structured data-type is used for the array permitting easy access to x, y, and SAD values:
    
    
    from __future__ import division
    
    import numpy as np
    
    width = 640
    height = 480
    cols = (width + 15) // 16
    cols += 1 # there's always an extra column
    rows = (height + 15) // 16
    
    motion_data = np.fromfile(
        'motion.data', dtype=[
            ('x', 'i1'),
            ('y', 'i1'),
            ('sad', 'u2'),
            ])
    frames = motion_data.shape[0] // (cols * rows)
    motion_data = motion_data.reshape((frames, rows, cols))
    
    # Access the data for the first frame
    motion_data[0]
    
    # Access just the x-vectors from the fifth frame
    motion_data[4]['x']
    
    # Access SAD values for the tenth frame
    motion_data[9]['sad']
    

You can calculate the amount of motion the vector represents simply by calculating the [magnitude of the vector](https://en.wikipedia.org/wiki/Magnitude_%28mathematics%29#Euclidean_vector_space) with Pythagoras' theorem. The SAD ([Sum of Absolute Differences](https://en.wikipedia.org/wiki/Sum_of_absolute_differences)) value can be used to determine how well the encoder thinks the vector represents the original reference frame.

The following code extends the example above to use PIL to produce a PNG image from the magnitude of each frame's motion vectors:
    
    
    from __future__ import division
    
    import numpy as np
    from PIL import Image
    
    width = 640
    height = 480
    cols = (width + 15) // 16
    cols += 1
    rows = (height + 15) // 16
    
    m = np.fromfile(
        'motion.data', dtype=[
            ('x', 'i1'),
            ('y', 'i1'),
            ('sad', 'u2'),
            ])
    frames = m.shape[0] // (cols * rows)
    m = m.reshape((frames, rows, cols))
    
    for frame in range(frames):
        data = np.sqrt(
            np.square(m[frame]['x'].astype(np.float)) +
            np.square(m[frame]['y'].astype(np.float))
            ).clip(0, 255).astype(np.uint8)
        img = Image.fromarray(data)
        filename = 'frame%03d.png' % frame
        print('Writing %s' % filename)
        img.save(filename)
    

You may wish to investigate the `[PiMotionArray`](http://picamera.readthedocs.io/en/release-1.13/api_array.html) and `[PiMotionAnalysis`](http://picamera.readthedocs.io/en/release-1.13/api_array.html) classes in the `[picamera.array`](http://picamera.readthedocs.io/en/release-1.13/api_array.html) module which simplifies the above recipes to the following:
    
    
    import numpy as np
    import picamera
    import picamera.array
    from PIL import Image
    
    with picamera.PiCamera() as camera:
        with picamera.array.PiMotionArray(camera) as stream:
            camera.resolution = (640, 480)
            camera.framerate = 30
            camera.start_recording('/dev/null', format='h264', motion_output=stream)
            camera.wait_recording(10)
            camera.stop_recording()
            for frame in range(stream.array.shape[0]):
                data = np.sqrt(
                    np.square(stream.array[frame]['x'].astype(np.float)) +
                    np.square(stream.array[frame]['y'].astype(np.float))
                    ).clip(0, 255).astype(np.uint8)
                img = Image.fromarray(data)
                filename = 'frame%03d.png' % frame
                print('Writing %s' % filename)
                img.save(filename)
    

The following command line can be used to generate an animation from the generated PNGs with ffmpeg (this will take a _very_ long time on the Pi so you may wish to transfer the images to a faster machine for this step):
    
    
    avconv -r 30 -i frame%03d.png -filter:v scale=640:480 -c:v libx264 motion.mp4
    

Finally, as a demonstration of what can be accomplished with motion vectors, here's a gesture detection system:
    
    
    import os
    import numpy as np
    import picamera
    from picamera.array import PiMotionAnalysis
    
    class GestureDetector(PiMotionAnalysis):
        QUEUE_SIZE = 10 # the number of consecutive frames to analyze
        THRESHOLD = 4.0 # the minimum average motion required in either axis
    
        def __init__(self, camera):
            super(GestureDetector, self).__init__(camera)
            self.x_queue = np.zeros(self.QUEUE_SIZE, dtype=np.float)
            self.y_queue = np.zeros(self.QUEUE_SIZE, dtype=np.float)
            self.last_move = ''
    
        def analyze(self, a):
            # Roll the queues and overwrite the first element with a new
            # mean (equivalent to pop and append, but faster)
            self.x_queue[1:] = self.x_queue[:-1]
            self.y_queue[1:] = self.y_queue[:-1]
            self.x_queue[0] = a['x'].mean()
            self.y_queue[0] = a['y'].mean()
            # Calculate the mean of both queues
            x_mean = self.x_queue.mean()
            y_mean = self.y_queue.mean()
            # Convert left/up to -1, right/down to 1, and movement below
            # the threshold to 0
            x_move = (
                '' if abs(x_mean) < self.THRESHOLD else
                'left' if x_mean < 0.0 else
                'right')
            y_move = (
                '' if abs(y_mean) < self.THRESHOLD else
                'down' if y_mean < 0.0 else
                'up')
            # Update the display
            movement = ('%s %s' % (x_move, y_move)).strip()
            if movement != self.last_move:
                self.last_move = movement
                if movement:
                    print(movement)
    
    with picamera.PiCamera(resolution='VGA', framerate=24) as camera:
        with GestureDetector(camera) as detector:
            camera.start_recording(
                os.devnull, format='h264', motion_output=detector)
            try:
                while True:
                    camera.wait_recording(1)
            finally:
                camera.stop_recording()
    

Within a few inches of the camera, move your hand up, down, left, and right, parallel to the camera and you should see the direction displayed on the console.

New in version 1.5.

## 4.14. Splitting to/from a circular stream

This example builds on the one in [Recording to a circular stream](http://picamera.readthedocs.io/en/release-1.13/recipes1.html) and the one in [Capturing images whilst recording](http://picamera.readthedocs.io/en/release-1.13/recipes2.html) to demonstrate the beginnings of a security application. As before, a `[PiCameraCircularIO`](http://picamera.readthedocs.io/en/release-1.13/api_streams.html) instance is used to keep the last few seconds of video recorded in memory. While the video is being recorded, video-port-based still captures are taken to provide a motion detection routine with some input (the actual motion detection algorithm is left as an exercise for the reader).

Once motion is detected, the last 10 seconds of video are written to disk, and video recording is split to another disk file to proceed until motion is no longer detected. Once motion is no longer detected, we split the recording back to the in-memory ring-buffer:
    
    
    import io
    import random
    import picamera
    from PIL import Image
    
    prior_image = None
    
    def detect_motion(camera):
        global prior_image
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg', use_video_port=True)
        stream.seek(0)
        if prior_image is None:
            prior_image = Image.open(stream)
            return False
        else:
            current_image = Image.open(stream)
            # Compare current_image to prior_image to detect motion. This is
            # left as an exercise for the reader!
            result = random.randint(0, 10) == 0
            # Once motion detection is done, make the prior image the current
            prior_image = current_image
            return result
    
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        stream = picamera.PiCameraCircularIO(camera, seconds=10)
        camera.start_recording(stream, format='h264')
        try:
            while True:
                camera.wait_recording(1)
                if detect_motion(camera):
                    print('Motion detected!')
                    # As soon as we detect motion, split the recording to
                    # record the frames "after" motion
                    camera.split_recording('after.h264')
                    # Write the 10 seconds "before" motion to disk as well
                    stream.copy_to('before.h264', seconds=10)
                    stream.clear()
                    # Wait until motion is no longer detected, then split
                    # recording back to the in-memory circular buffer
                    while detect_motion(camera):
                        camera.wait_recording(1)
                    print('Motion stopped!')
                    camera.split_recording(stream)
        finally:
            camera.stop_recording()
    

This example also demonstrates using the _seconds_ parameter of the `[copy_to()`](http://picamera.readthedocs.io/en/release-1.13/api_streams.html) method to limit the before file to 10 seconds of data (given that the circular buffer may contain considerably more than this).

New in version 1.0.

## 4.15. Custom encoders

You can override and/or extend the encoder classes used during image or video capture. This is particularly useful with video capture as it allows you to run your own code in response to every frame, although naturally whatever code runs within the encoder's callback has to be reasonably quick to avoid stalling the encoder pipeline.

Writing a custom encoder is quite a bit harder than writing a [custom output](http://picamera.readthedocs.io/en/release-1.13/recipes2.html) and in most cases there's little benefit. The only thing a custom encoder gives you that a custom output doesn't is access to the buffer header flags. For many output formats (MJPEG and YUV for example), these won't tell you anything interesting (i.e. they'll simply indicate that the buffer contains a full frame and nothing else). Currently, the only format where the buffer header flags contain useful information is H.264. Even then, most of the information (I-frame, P-frame, motion information, etc.) would be accessible from the `[frame`](http://picamera.readthedocs.io/en/release-1.13/api_camera.html) attribute which you could access from your custom output's `write` method.

The encoder classes defined by picamera form the following hierarchy (dark classes are actually instantiated by the implementation in picamera, light classes implement base functionality but aren't technically "abstract"):

![_images/encoder_classes.svg](http://picamera.readthedocs.io/en/release-1.13/_images/encoder_classes.svg)

The following table details which `[PiCamera`](http://picamera.readthedocs.io/en/release-1.13/api_camera.html) methods use which encoder classes, and which method they call to construct these encoders:

Method(s) Calls Returns

`[capture()`](http://picamera.readthedocs.io/en/release-1.13/api_camera.html) `[capture_continuous()`](http://picamera.readthedocs.io/en/release-1.13/api_camera.html) `[capture_sequence()`](http://picamera.readthedocs.io/en/release-1.13/api_camera.html)
`_get_image_encoder()`
`[PiCookedOneImageEncoder`](http://picamera.readthedocs.io/en/release-1.13/api_encoders.html) `[PiRawOneImageEncoder`](http://picamera.readthedocs.io/en/release-1.13/api_encoders.html)

`[capture_sequence()`](http://picamera.readthedocs.io/en/release-1.13/api_camera.html)
`_get_images_encoder()`
`[PiCookedMultiImageEncoder`](http://picamera.readthedocs.io/en/release-1.13/api_encoders.html) `[PiRawMultiImageEncoder`](http://picamera.readthedocs.io/en/release-1.13/api_encoders.html)

`[start_recording()`](http://picamera.readthedocs.io/en/release-1.13/api_camera.html) `[record_sequence()`](http://picamera.readthedocs.io/en/release-1.13/api_camera.html)
`_get_video_encoder()`
`[PiCookedVideoEncoder`](http://picamera.readthedocs.io/en/release-1.13/api_encoders.html) `[PiRawVideoEncoder`](http://picamera.readthedocs.io/en/release-1.13/api_encoders.html)

It is recommended, particularly in the case of the image encoder classes, that you familiarize yourself with the specific function of these classes so that you can determine the best class to extend for your particular needs. You may find that one of the intermediate classes is a better basis for your own modifications.

In the following example recipe we will extend the `[PiCookedVideoEncoder`](http://picamera.readthedocs.io/en/release-1.13/api_encoders.html) class to store how many I-frames and P-frames are captured (the camera's encoder doesn't use B-frames):
    
    
    import picamera
    import picamera.mmal as mmal
    
    # Override PiVideoEncoder to keep track of the number of each type of frame
    class MyEncoder(picamera.PiCookedVideoEncoder):
        def start(self, output, motion_output=None):
            self.parent.i_frames = 0
            self.parent.p_frames = 0
            super(MyEncoder, self).start(output, motion_output)
    
        def _callback_write(self, buf):
            # Only count when buffer indicates it's the end of a frame, and
            # it's not an SPS/PPS header (..._CONFIG)
            if (
                    (buf.flags & mmal.MMAL_BUFFER_HEADER_FLAG_FRAME_END) and
                    not (buf.flags & mmal.MMAL_BUFFER_HEADER_FLAG_CONFIG)
                ):
                if buf.flags & mmal.MMAL_BUFFER_HEADER_FLAG_KEYFRAME:
                    self.parent.i_frames += 1
                else:
                    self.parent.p_frames += 1
            # Remember to return the result of the parent method!
            return super(MyEncoder, self)._callback_write(buf)
    
    # Override PiCamera to use our custom encoder for video recording
    class MyCamera(picamera.PiCamera):
        def __init__(self):
            super(MyCamera, self).__init__()
            self.i_frames = 0
            self.p_frames = 0
    
        def _get_video_encoder(
                self, camera_port, output_port, format, resize, **options):
            return MyEncoder(
                    self, camera_port, output_port, format, resize, **options)
    
    with MyCamera() as camera:
        camera.start_recording('foo.h264')
        camera.wait_recording(10)
        camera.stop_recording()
        print('Recording contains %d I-frames and %d P-frames' % (
                camera.i_frames, camera.p_frames))
    

Please note that the above recipe is flawed: PiCamera is capable of initiating [multiple simultaneous recordings](http://picamera.readthedocs.io/en/release-1.13/recipes2.html). If this were used with the above recipe, then each encoder would wind up incrementing the `i_frames` and `p_frames` attributes on the `MyCamera` instance leading to incorrect results.

New in version 1.5.

## 4.16. Raw Bayer data captures

The `bayer` parameter of the `[capture()`](http://picamera.readthedocs.io/en/release-1.13/api_camera.html) method causes the raw Bayer data recorded by the camera's sensor to be output as part of the image meta-data.

Note

The `bayer` parameter only operates with the JPEG format, and only for captures from the still port (i.e. when `use_video_port` is False, as it is by default).

Raw Bayer data differs considerably from simple unencoded captures; it is the data recorded by the camera's sensor prior to _any_ GPU processing including auto white balance, vignette compensation, smoothing, down-scaling, etc. This also means:

  * Bayer data is organized in a BGGR pattern (a minor variation of the common [Bayer CFA](https://en.wikipedia.org/wiki/Bayer_filter)). The raw data therefore has twice as many green pixels as red or blue and if viewed "raw" will look distinctly strange (too dark, too green, and with zippering effects along any straight edges).
![_images/bayer_pattern.svg](http://picamera.readthedocs.io/en/release-1.13/_images/bayer_pattern.svg)

  * To make a "normal" looking image from raw Bayer data you will need to perform [de-mosaicing](https://en.wikipedia.org/wiki/Demosaicing) at the very least, and probably some form of [color balance](https://en.wikipedia.org/wiki/Color_balance).

This (heavily commented) example script causes the camera to capture an image including the raw Bayer data. It then proceeds to unpack the Bayer data into a 3-dimensional [numpy](http://www.numpy.org/) array representing the raw RGB data and finally performs a rudimentary de-mosaic step with weighted averages. A couple of numpy tricks are used to improve performance but bear in mind that all processing is happening on the CPU and will be considerably slower than normal image captures:
    
    
    from __future__ import (
        unicode_literals,
        absolute_import,
        print_function,
        division,
        )
    
    
    import io
    import time
    import picamera
    import numpy as np
    from numpy.lib.stride_tricks import as_strided
    
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        # Let the camera warm up for a couple of seconds
        time.sleep(2)
        # Capture the image, including the Bayer data
        camera.capture(stream, format='jpeg', bayer=True)
        ver = {
            'RP_ov5647': 1,
            'RP_imx219': 2,
            }[camera.exif_tags['IFD0.Model']]
    
    # Extract the raw Bayer data from the end of the stream, check the
    # header and strip if off before converting the data into a numpy array
    
    offset = {
        1: 6404096,
        2: 10270208,
        }[ver]
    data = stream.getvalue()[-offset:]
    assert data[:4] == 'BRCM'
    data = data[32768:]
    data = np.fromstring(data, dtype=np.uint8)
    
    # For the V1 module, the data consists of 1952 rows of 3264 bytes of data.
    # The last 8 rows of data are unused (they only exist because the maximum
    # resolution of 1944 rows is rounded up to the nearest 16).
    #
    # For the V2 module, the data consists of 2480 rows of 4128 bytes of data.
    # There's actually 2464 rows of data, but the sensor's raw size is 2466
    # rows, rounded up to the nearest multiple of 16: 2480.
    #
    # Likewise, the last few bytes of each row are unused (why?). Here we
    # reshape the data and strip off the unused bytes.
    
    reshape, crop = {
        1: ((1952, 3264), (1944, 3240)),
        2: ((2480, 4128), (2464, 4100)),
        }[ver]
    data = data.reshape(reshape)[:crop[0], :crop[1]]
    
    # Horizontally, each row consists of 10-bit values. Every four bytes are
    # the high 8-bits of four values, and the 5th byte contains the packed low
    # 2-bits of the preceding four values. In other words, the bits of the
    # values A, B, C, D and arranged like so:
    #
    #  byte 1   byte 2   byte 3   byte 4   byte 5
    # AAAAAAAA BBBBBBBB CCCCCCCC DDDDDDDD AABBCCDD
    #
    # Here, we convert our data into a 16-bit array, shift all values left by
    # 2-bits and unpack the low-order bits from every 5th byte in each row,
    # then remove the columns containing the packed bits
    
    data = data.astype(np.uint16) << 2
    for byte in range(4):
        data[:, byte::5] |= ((data[:, 4::5] >> ((4 - byte) * 2)) & 0b11)
    data = np.delete(data, np.s_[4::5], 1)
    
    # Now to split the data up into its red, green, and blue components. The
    # Bayer pattern of the OV5647 sensor is BGGR. In other words the first
    # row contains alternating green/blue elements, the second row contains
    # alternating red/green elements, and so on as illustrated below:
    #
    # GBGBGBGBGBGBGB
    # RGRGRGRGRGRGRG
    # GBGBGBGBGBGBGB
    # RGRGRGRGRGRGRG
    #
    # Please note that if you use vflip or hflip to change the orientation
    # of the capture, you must flip the Bayer pattern accordingly
    
    rgb = np.zeros(data.shape + (3,), dtype=data.dtype)
    rgb[1::2, 0::2, 0] = data[1::2, 0::2] # Red
    rgb[0::2, 0::2, 1] = data[0::2, 0::2] # Green
    rgb[1::2, 1::2, 1] = data[1::2, 1::2] # Green
    rgb[0::2, 1::2, 2] = data[0::2, 1::2] # Blue
    
    # At this point we now have the raw Bayer data with the correct values
    # and colors but the data still requires de-mosaicing and
    # post-processing. If you wish to do this yourself, end the script here!
    #
    # Below we present a fairly naive de-mosaic method that simply
    # calculates the weighted average of a pixel based on the pixels
    # surrounding it. The weighting is provided by a byte representation of
    # the Bayer filter which we construct first:
    
    bayer = np.zeros(rgb.shape, dtype=np.uint8)
    bayer[1::2, 0::2, 0] = 1 # Red
    bayer[0::2, 0::2, 1] = 1 # Green
    bayer[1::2, 1::2, 1] = 1 # Green
    bayer[0::2, 1::2, 2] = 1 # Blue
    
    # Allocate an array to hold our output with the same shape as the input
    # data. After this we define the size of window that will be used to
    # calculate each weighted average (3x3). Then we pad out the rgb and
    # bayer arrays, adding blank pixels at their edges to compensate for the
    # size of the window when calculating averages for edge pixels.
    
    output = np.empty(rgb.shape, dtype=rgb.dtype)
    window = (3, 3)
    borders = (window[0] - 1, window[1] - 1)
    border = (borders[0] // 2, borders[1] // 2)
    
    rgb = np.pad(rgb, [
        (border[0], border[0]),
        (border[1], border[1]),
        (0, 0),
        ], 'constant')
    bayer = np.pad(bayer, [
        (border[0], border[0]),
        (border[1], border[1]),
        (0, 0),
        ], 'constant')
    
    # For each plane in the RGB data, we use a nifty numpy trick
    # (as_strided) to construct a view over the plane of 3x3 matrices. We do
    # the same for the bayer array, then use Einstein summation on each
    # (np.sum is simpler, but copies the data so it's slower), and divide
    # the results to get our weighted average:
    
    for plane in range(3):
        p = rgb[..., plane]
        b = bayer[..., plane]
        pview = as_strided(p, shape=(
            p.shape[0] - borders[0],
            p.shape[1] - borders[1]) + window, strides=p.strides * 2)
        bview = as_strided(b, shape=(
            b.shape[0] - borders[0],
            b.shape[1] - borders[1]) + window, strides=b.strides * 2)
        psum = np.einsum('ijkl->ij', pview)
        bsum = np.einsum('ijkl->ij', bview)
        output[..., plane] = psum // bsum
    
    # At this point output should contain a reasonably "normal" looking
    # image, although it still won't look as good as the camera's normal
    # output (as it lacks vignette compensation, AWB, etc).
    #
    # If you want to view this in most packages (like GIMP) you'll need to
    # convert it to 8-bit RGB data. The simplest way to do this is by
    # right-shifting everything by 2-bits (yes, this makes all that
    # unpacking work at the start rather redundant...)
    
    output = (output >> 2).astype(np.uint8)
    with open('image.data', 'wb') as f:
        output.tofile(f)
    

An enhanced version of this recipe (which also handles different bayer orders caused by flips and rotations) is also encapsulated in the `[PiBayerArray`](http://picamera.readthedocs.io/en/release-1.13/api_array.html) class in the `[picamera.array`](http://picamera.readthedocs.io/en/release-1.13/api_array.html) module, which means the same can be achieved as follows:
    
    
    import time
    import picamera
    import picamera.array
    import numpy as np
    
    with picamera.PiCamera() as camera:
        with picamera.array.PiBayerArray(camera) as stream:
            camera.capture(stream, 'jpeg', bayer=True)
            # Demosaic data and write to output (just use stream.array if you
            # want to skip the demosaic step)
            output = (stream.demosaic() >> 2).astype(np.uint8)
            with open('image.data', 'wb') as f:
                output.tofile(f)
    

## 4.17. Using a flash with the camera

The Pi's camera module includes an LED flash driver which can be used to illuminate a scene upon capture. The flash driver has two configurable GPIO pins:

  * one for connection to an LED based flash (xenon flashes won't work with the camera module due to it having a [rolling shutter](https://en.wikipedia.org/wiki/Rolling_shutter)). This will fire before ([flash metering](https://en.wikipedia.org/wiki/Through-the-lens_metering#Through_the_lens_flash_metering)) and during capture
  * one for an optional privacy indicator (a requirement for cameras in some jurisdictions). This will fire after taking a picture to indicate that the camera has been used

These pins are configured by updating the [VideoCore device tree blob](https://www.raspberrypi.org/documentation/configuration/pin-configuration.md). Firstly, install the device tree compiler, then grab a copy of the default device tree source:
    
    
    $ sudo apt-get install device-tree-compiler
    $ wget https://github.com/raspberrypi/firmware/raw/master/extra/dt-blob.dts
    

The device tree source contains a number of sections enclosed in curly braces, which form a hierarchy of definitions. The section to edit will depend on which revision of Raspberry Pi you have (check the silk-screen writing on the board for the revision number if you are unsure):

Model Section

Raspberry Pi Model B rev 1
`/videocore/pins_rev1`

Raspberry Pi Model A and Model B rev 2
`/videocore/pins_rev2`

Raspberry Pi Model A+
`/videocore/pins_aplus`

Raspberry Pi Model B+ rev 1.1
`/videocore/pins_bplus1`

Raspberry Pi Model B+ rev 1.2
`/videocore/pins_bplus2`

Raspberry Pi 2 Model B rev 1.0
`/videocore/pins_2b1`

Raspberry Pi 2 Model B rev 1.1 and rev 1.2
`/videocore/pins_2b2`

Raspberry Pi 3 Model B rev 1.0
`/videocore/pins_3b1`

Raspberry Pi 3 Model B rev 1.2
`/videocore/pins_3b2`

Raspberry Pi Zero rev 1.2 and rev 1.3
`/videocore/pins_pi0`

Under the section for your particular model of Pi you will find `pin_config` and `pin_defines` sections. Under the `pin_config` section you need to configure the GPIO pins you want to use for the flash and privacy indicator as using pull down termination. Then, under the `pin_defines` section you need to associate those pins with the `FLASH_0_ENABLE` and `FLASH_0_INDICATOR` pins.

For example, to configure GPIO 17 as the flash pin, leaving the privacy indicator pin absent, on a Raspberry Pi 2 Model B rev 1.1 you would add the following line under the `/videocore/pins_2b2/pin_config` section:
    
    
    pin@p17 { function = "output"; termination = "pull_down"; };
    

Please note that GPIO pins will be numbered according to the [Broadcom pin numbers](https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering) (BCM mode in the RPi.GPIO library, _not_ BOARD mode). Then change the following section under `/videocore/pins_2b2/pin_defines`. Specifically, change the type from "absent" to "internal", and add a number property defining the flash pin as GPIO 17:
    
    
    pin_define@FLASH_0_ENABLE {
        type = "internal";
        number = <17>;
    };
    

With the device tree source updated, you now need to compile it into a binary blob for the firmware to read. This is done with the following command line:
    
    
    $ dtc -q -I dts -O dtb dt-blob.dts -o dt-blob.bin
    

Dissecting this command line, the following components are present:

  * `dtc` \- Execute the device tree compiler
  * `-I dts` \- The input file is in device tree source format
  * `-O dtb` \- The output file should be produced in device tree binary format
  * `dt-blob.dts` \- The first anonymous parameter is the input filename
  * `-o dt-blob.bin` \- The output filename

This should output nothing. If you get lots of warnings, you've forgotten the `-q` switch; you can ignore the warnings. If anything else is output, it will most likely be an error message indicating you have made a mistake in the device tree source. In this case, review your edits carefully (note that sections and properties _must_ be semi-colon terminated for example), and try again.

Now the device tree binary blob has been produced, it needs to be placed on the first partition of the SD card. In the case of non-NOOBS Raspbian installs, this is generally the partition mounted as `/boot`:
    
    
    $ sudo cp dt-blob.bin /boot/
    

However, in the case of NOOBS Raspbian installs, this is the recovery partition, which is not mounted by default:
    
    
    $ sudo mkdir /mnt/recovery
    $ sudo mount /dev/mmcblk0p1 /mnt/recovery
    $ sudo cp dt-blob.bin /mnt/recovery
    $ sudo umount /mnt/recovery
    $ sudo rmdir /mnt/recovery
    

Please note that the filename and location are important. The binary blob must be named `dt-blob.bin` (all lowercase), and it must be placed in the root directory of the first partition on the SD card. Once you have rebooted the Pi (to activate the new device tree configuration) you can test the flash with the following simple script:
    
    
    import picamera
    
    with picamera.PiCamera() as camera:
        camera.flash_mode = 'on'
        camera.capture('foo.jpg')
    

You should see your flash LED blink twice during the execution of the script.

The GPIOs only have a limited current drive which is insufficient for powering the sort of LEDs typically used as flashes in mobile phones. You will require a suitable drive circuit to power such devices, or risk damaging your Pi. One developer on the Pi forums notes:

> For reference, the flash driver chips we have used on mobile phones will often drive up to 500mA into the LED. If you're aiming for that, then please think about your power supply too.

If you wish to experiment with the flash driver without attaching anything to the GPIO pins, you can also reconfigure the camera's own LED to act as the flash LED. Obviously this is no good for actual flash photography but it can demonstrate whether your configuration is good. In this case you need not add anything to the `pin_config` section (the camera's LED pin is already defined to use pull down termination), but you do need to set `CAMERA_0_LED` to absent, and `FLASH_0_ENABLE` to the old `CAMERA_0_LED` definition (this will be pin 5 in the case of `pins_rev1` and `pins_rev2`, and pin 32 in the case of everything else). For example, change:
    
    
    pin_define@CAMERA_0_LED {
        type = "internal";
        number = <5>;
    };
    pin_define@FLASH_0_ENABLE {
        type = "absent";
    };
    

into this:
    
    
    pin_define@CAMERA_0_LED {
        type = "absent";
    };
    pin_define@FLASH_0_ENABLE {
        type = "internal";
        number = <5>;
    };
    

After compiling and installing the device tree blob according to the instructions above, and rebooting the Pi, you should find the camera LED now acts as a flash LED with the Python script above.

New in version 1.10.

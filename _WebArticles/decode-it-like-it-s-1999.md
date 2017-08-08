# Decode It Like It's 1999

_Captured: 2017-05-10 at 22:26 from [jsmpeg.com](http://jsmpeg.com/)_

## A JavaScript MPEG1 Video & MP2 Audio Decoder

JSMpeg is a Video Player written in JavaScript. It consists of an MPEG-TS Demuxer, MPEG1 Video & MP2 Audio Decoders, WebGL & Canvas2D Renderers and WebAudio Sound Output. JSMpeg can load static files via Ajax and allows low latency streaming (~50ms) via WebSocktes.

JSMpeg can decode 720p Video at 30fps on an iPhone 5S, works in any modern browser (Chrome, Firefox, Safari & Edge) and comes in at 20kb gzipped.

Using it can be as simple as this:
    
    
    <script src="jsmpeg.min.js"></script>
    <div class="jsmpeg" data-url="video.ts"></div>

## Low Latency Video & Audio Streaming that works everywhere - yes, even on the iPhone

JSMpeg can connect to a WebSocket server that sends out binary MPEG-TS data. Where this data comes from, is up to you.

![](http://jsmpeg.com/jsmpeg-latency.jpg)

The latency is only dependend on your source, the network conditions and how fast your browser, GPU and monitor can spit out frames. For a screen capture on a local network, it can be as low as 50ms.

One of the easiest ways to set this up is to use `ffmpeg` and a tiny nodejs WebSocket server. See the [documentation on github](https://github.com/phoboslab/jsmpeg) for the details.

## Projects using JSMpeg & further reading

  *   
Various interesting bits about JSMpeg's development 
  * [JSMpeg - Fronteers 2015, Dominic Szablewski](https://vimeo.com/144499042)  
A talk about the inner workings of the MPEG1 codec 
  * [Instant Webcam](http://instant-webcam.com/)  
Stream video from iPhone/iPad to any Browser in your Wi-Fi 
  * [jsmpeg-vnc](http://phoboslab.org/log/2015/07/play-gta-v-in-your-browser-sort-of)  
Control your Windows PC through your Browser 

## Why use JSMpeg?

What's the alternative?

  * HTTP Live Streaming (HLS) or MPEG-DASH add _at least_ 5 seconds of latency. 
  * WebRTC is not supported on iOS. 
  * Not all browsers can decode H264; not all browsers can decode VP8. 
  * WebRTC is tremendously complex. Try setting up a WebRTC broadcast server and you'll find yourself in a mess of STUN, TURN, signaling and media servers while trying to setup and compile a whooping 4GB git repository with custom tooling just to end up with what is essentially a black box that you can't possibly understand within your lifetime (well, I can't). 

With JSMpeg you get:

  * A video and audio format that works in all modern browsers. 
  * No licensing fees. All MPEG1 and MP2 patents have expired. 
  * Very tight control over the Audio and Video decoders to implement your ideas. 
  * Very low latency realtime streaming with high framerates and acceptable quality and bitrates. 
  * **A stack that you can understand from top to bottom.**

Should you use JSMpeg for everything? Certainly not. If you just want to have a static video on your page, go with Youtube or encode it as WebM & MP4 and host it yourself.

If you need tight control over playback, realtime streaming or if you're just curious about Video & Audio codecs, JavaScript or WebGL, consider JSMpeg.

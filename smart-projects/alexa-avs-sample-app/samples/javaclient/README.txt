Refer to https://developer.amazon.com/public/solutions/alexa/alexa-voice-service/ for the most up to date documentation on how to
use this client and how to provision with your account and test device information. Please note that in order to use this client you
must also use one of the companion samples for authentication.

Then do the following:

First, check what version of Java you have. Only 1.8 is supported:

  $ java -version
  java version "1.8.0_74"
  Java(TM) SE Runtime Environment (build 1.8.0_74-b02)
  Java HotSpot(TM) 64-Bit Server VM (build 25.74-b02, mixed mode)

Then, consult the table at this URL: http://www.eclipse.org/jetty/documentation/current/alpn-chapter.html#alpn-versions
Copy the version of ALPN that you require for your version of the JDK.

When you run the app you'll need to run it like so:
mvn exec:exec -Dalpn-boot.version=YOUR_VERSION
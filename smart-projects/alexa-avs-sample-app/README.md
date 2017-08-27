![](../../wiki/assets/alexa-logo-3.png)

## About the project

This project provides a step-by-step walkthrough to help you build a **hands-free** [Alexa Voice Service](https://developer.amazon.com/avs) (AVS) prototype in 60 minutes, using wake word engines from [Sensory](https://github.com/Sensory/alexa-rpi) or [KITT.AI](https://github.com/Kitt-AI/snowboy). Now, in addition to pushing a button to "start listening", you can now also just say the wake word "Alexa", much like the [Amazon Echo](https://amazon.com/echo). You can find step-by-step instructions to set up the hands-free prototype on [Raspberry Pi](../../wiki/Raspberry-Pi), or follow the instructions to set up the push-to-talk only prototype on [Linux](../../wiki/Linux), [Mac](../../wiki/Mac), or [Windows](../../wiki/Windows).

---

## What is AVS?

[Alexa Voice Service](https://developer.amazon.com/avs) (AVS) is Amazon’s intelligent voice recognition and natural language understanding service that allows you as a developer to voice-enable any connected device that has a microphone and speaker.

---

## Get started

You can set up this project on the following platforms -

* [Raspberry Pi](../../wiki/Raspberry-Pi), or
* [Linux](../../wiki/Linux), or
* [Mac](../../wiki/Mac), or
* [Windows](../../wiki/Windows)  

Or you can prototype with these third-party dev kits -

* *New!* [Raspberry Pi + Microsemi AcuEdge Development Kit for Amazon AVS](https://github.com/MicrosemiVoiceProcessing/ZLK38AVS/wiki/howto)    
* [Raspberry Pi + Conexant 4-mic Development Kit for Amazon AVS](https://github.com/conexant/alexa-avs-sample-app/wiki/Conexant4Mic-Raspberry-Pi)
* [Raspberry Pi + Conexant 2-Mic Development Kit for Amazon AVS](../../wiki/Conexant2Mic-Raspberry-Pi)  

---

## What's new?  

**July 6, 2017:**

*Updates*

* The sample app has been updated to support Notifications.
  * Enable the [Quote Maker](https://www.amazon.com/dp/B071ZMZWF7/ref=sr_1_1?s=digital-skills&ie=UTF8&qid=1499374636&sr=1-1&keywords=quote+maker) skill, located in the Alexa Skills Store to test Notifications with the AVS Sample App.
* Added a login/logout button.

**June 21, 2017:**  

*Updates*

* The sample app now supports Display Cards.  
  * `TemplateRuntime` directives will be displayed in the sample app as JSON.   
  * To enable Display Cards:  
    * Login to the [Amazon Developer Portal](https://developer.amazon.com/login.html) and navigate to your product: **Alexa > AVS**.
    * Click **Edit**, then click **Device Capabilities**.  
    * Select **Display Cards**, then select **Display Cards with Media**.  

**May 31, 2017:**

*Updates*  

* The Raspberry Pi + Microsemi AcuEdge Development Kit for Amazon AVS is now available for purchase. [Learn more »](https://developer.amazon.com/alexa-voice-service/dev-kits/microsemi-acuedge/)  

**May 4, 2017:**  

*Updates*

* The Conexant 4-mic Development Kit for Amazon AVS is now available, making it easier and more cost-effective to build far-field products with Amazon Alexa. [Learn more »](http://developer.amazon.com/alexa-voice-service/dev-kits/conexant-4-mic/)  

**April 27, 2017:**

*Updates*

* Need help troubleshooting the AVS Sample App? Check out the new [Troubleshooting Guide](https://github.com/alexa/alexa-avs-sample-app/wiki/Troubleshooting).

**April 20, 2017:**  

*Updates*  

* The companion service persists refresh tokens between restarts. This means you won't have to authenticate each time you bring up the sample app. Read about the update on the [Alexa Blog »](https://developer.amazon.com/blogs/alexa/post/bb4a34ad-f805-43d9-bbe0-c113105dd8fd/understanding-login-authentication-with-the-avs-sample-app-and-the-node-js-server).  
* The **Listen** button has been replaced with a microphone icon.  
* The sample app uses new Alexa wake word models from KITT.ai.  

*Maintenance*  

* ALPN version has been updated in `POM.xml`.  
* Automated install no longer requires user intervention to update certificates.  

*Bug Fixes*  

* The sample app ensures that the downchannel stream is established before sending the initial `SynchronizeState` event. This adheres to the guidance provided in [Managing an HTTP/2 Connection with AVS](https://developer.amazon.com/public/solutions/alexa/alexa-voice-service/docs/managing-an-http-2-connection).
* Locale strings in the sample app user interface have been updated to match the values in `config.json`.  
* Fixed no volume in Linux bug.  
* **WiringPi** is now installed as part of `automated_install.sh`.  
* Fixed 100% CPU bug.  

*Known Issues*

* To log out of the java sample app you must delete your `refresh_tokens` file in the `/samples/companionService` folder. Otherwise, the sample app will authenticate on each reboot. [Click here for log out instructions](../../wiki/Sample-App-Log-Out-Instructions).

---

## Important considerations

* Review the AVS [Terms & Agreements](https://developer.amazon.com/public/solutions/alexa/alexa-voice-service/support/terms-and-agreements).  

* The earcons associated with the sample project are for **prototyping purposes only**. For implementation and design guidance for commercial products, please see [Designing for AVS](https://developer.amazon.com/public/solutions/alexa/alexa-voice-service/content/designing-for-the-alexa-voice-service) and [AVS UX Guidelines](https://developer.amazon.com/public/solutions/alexa/alexa-voice-service/content/alexa-voice-service-ux-design-guidelines).

* **Usage of Sensory & KITT.AI wake word engines**: The wake word engines included with this project (Sensory and KITT.AI) are intended to be used for **prototyping purposes only**. If you are building a commercial product with either solution, please use the contact information below to enquire about commercial licensing -
  * [Contact Sensory](http://www.sensory.com/support/contact/us-sales/) for information on TrulyHandsFree licensing.
  * [Contact KITT.AI](mailto:snowboy@kitt.ai) for information on SnowBoy licensing.

* **IMPORTANT**: The Sensory wake word engine included with this project is time-limited: code linked against it will stop working when the library expires. The library included in this repository will, at all times, have an expiration date that is at least **120 days** in the future. See Sensory's [GitHub](https://github.com/Sensory/alexa-rpi#license) page for more information on how to renew the license for non-commercial use.

---

## Contribute

* Want to report a bug or request an update to the documentation? See [CONTRIBUTING.md](https://github.com/alexa/alexa-avs-sample-app/blob/master/CONTRIBUTING.md).
* Having trouble? Check out our [troubleshooting guide](../../wiki/Troubleshooting).
* Have questions or need help building the sample app? Open a [new issue](https://github.com/alexa/alexa-avs-sample-app/issues/new).

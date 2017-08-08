# Create your own Git server using Raspberry Pi and GitLab

_Captured: 2017-08-05 at 17:21 from [medium.com](https://medium.com/@kevalpatel2106/create-your-own-git-server-using-raspberry-pi-and-gitlab-f64475901a66?source=userActivityShare-c79006fee040-1501946458)_

# Create your own Git server using Raspberry Pi and GitLab

![](https://cdn-images-1.medium.com/max/2000/1*heR5Y-7HzY8wDLOxCQntMQ.jpeg)

If you are a software developer or you are linked to software development you might know what is **Git** and **GitHub**.

For those who don't know what is GitHub, GitHub is a web service based on the software Git (which is a versioning software written by Linus Torvald, creator of Linux). Git allows you to store the history of your software code base and easily control versioning. GitHub host all those Git repositories and also provides many other features like bug tracking, milestone creation and also the creation of Wiki for your project.

In this article, you will learn how to host your own git server like GitHub on your raspberry pi using GitLab.

### Why do your want to host your local Git server?

GitHub is pretty amazing. It may satisfy all your code hosting requirements. But there are three main reasons to host your own git server.

  1. GitHub is **free only for the public projects only**. If you don't want to make your software open source then you have to buy the GitHub subscription plans. Now you may make project for hobby or you have a start-up company with the relatively small team. In that case of you don't want to buy those expensive subscription plans, you have to host your git server.
  2. If you want to use GitHub or any other git servers, **you have to trust the third party for hosting your data**. If you want to keep your data/source code secure and also want to control over where your data is being host, you have to host a local Git server.
  3. It's really fun. Really!!!

The easiest and the cheapest way to create these type of Git server is by using the most versatile and cheap Raspberry Pi.

### What do you need for this project?

\- A **Raspberry Pi 3**. (Raspberry Pi 3 is recommended as it has 64 bit CPU and GitLab requires a 64-bit architecture.)

\- **Power supply** to feed your raspberry pi.

\- **16 or 32GB microSD** card to store the Git reposetory. _(Make you have the latest version of Rasbpian Jessie flashed on the SD card and your SSH is enabled.)_

### How to install GitLab on Pi?

Installing GitLab on the Raspberry Pi is very simple. It's just 4 simple steps and that's it! You are all done. Let's get started.

First, login to your raspberry pi terminal using SSH and flow below steps.

### 1\. Install required dependencies.

  * Run the fllowing command in your SSH terminal to install and configure the necessary dependencies.

sudo apt-get install curl openssh-server ca-certificates postfix apt-transport-https
[view raw](https://gist.github.com/kevalpatel2106/a2de7305dde77ff35756095a79dc7853/raw/df9cc6d7a20cc8c948985845e0cbc730aff7c14b/install-gitlab.sh) [install-gitlab.sh](https://gist.github.com/kevalpatel2106/a2de7305dde77ff35756095a79dc7853#file-install-gitlab-sh) hosted with ❤ by [GitHub](https://github.com)

This command will install postfix on your raspberry pi. If you want to send emails from your GitLab server please select 'Internet Site' during setup.

  * Once it is done, run below command to add GPG keys. This will allow us ti easily update our GitLab server.

curl https://packages.gitlab.com/gpg.key | sudo apt-key add -
[view raw](https://gist.github.com/kevalpatel2106/67be31ad43dc0427df422f5ed1e9c5c2/raw/0fb57f2872a7ad8e877dd0b8a84ffd941c445c25/install-gitlab.sh) [install-gitlab.sh](https://gist.github.com/kevalpatel2106/67be31ad43dc0427df422f5ed1e9c5c2#file-install-gitlab-sh) hosted with ❤ by [GitHub](https://github.com)

### 2\. Install GitLab CE (Community Edition) server.

  * Run below command one by one to download and install GitLab. This may take time based on your internet speed.

sudo curl -sS https://packages.gitlab.com/install/repositories/gitlab/raspberry-pi2/script.deb.sh | sudo bash

sudo apt-get install gitlab-ce
[view raw](https://gist.github.com/kevalpatel2106/b3f7eb2e36b6ab1530674c6e8f93283b/raw/b5776a78e3cb58b96251732f1c9b357d8cea336a/install-gitlab.sh) [install-gitlab.sh](https://gist.github.com/kevalpatel2106/b3f7eb2e36b6ab1530674c6e8f93283b#file-install-gitlab-sh) hosted with ❤ by [GitHub](https://github.com)

### 3\. Configure and start GitLab.

  * Run below command to configure your gitlab server for the first time. This command will take couple of minutes to execute.

sudo gitlab-ctl reconfigure
[view raw](https://gist.github.com/kevalpatel2106/438fd62067035df153f754c0d37a0258/raw/f4095b89f03806cf60d3c127cca214e7a252ef0e/install-gitlab.sh) [install-gitlab.sh](https://gist.github.com/kevalpatel2106/438fd62067035df153f754c0d37a0258#file-install-gitlab-sh) hosted with ❤ by [GitHub](https://github.com)

  * That's it. Congratulations!!! You sucessfully installed GitLab server on your Raspberry Pi. Now one final step is remaining.

### 4\. Set up your GitLab account.

  * Get the IP of your raspberry pi using _ifconfig_ command.
  * Now on your computer, go to the browser. Open the IP you get from the previous step in your browser. Volla!!! You will have the GitLab server page on your computer screen right from the tiny raspberry pi.
![](https://cdn-images-1.medium.com/max/2000/1*FjXGG_QEMN3cKKFmfqMqlg.png)

  * On your first visit, you'll be redirected to a password reset screen to provide the password for the initial administrator account. Enter your desired password and you'll be redirected back to the login screen.

> Keep in mind that your default account's username is **root**.

  * Log in with your username (that is root by default) and the password you set in the previous step. You will have the home page of your GitLab server, where all your future projects will be listed.
![](https://cdn-images-1.medium.com/max/2000/1*581M2MGPuRkF7YI_sQcfbA.png)

> Finally!!👾 Running [@gitlab](http://twitter.com/gitlab) CE locally on my #RaspberryPi3. #Git #RaspberryPi #LearnEveryDay
> 
> -- [@kevalpatel2106](https://twitter.com/kevalpatel2106/status/881063654359093248)

### **Conclusion:**

So, now you learned how you can host your own Git server at your home. This will cost you less than $50. But, it will provide you complete control over your codebase.

Later if you want to migrate to any of online git server, you can easily change your Git hosting by easily adding a remote pointing to the online repository.

_~If you liked the article, click the 💚 below so more people can see it! Also, you can follow me on __[Medium_](https://medium.com/@kevalpatel2106)_ or on __[My Blog_](https://medium.com/@kevalpatel2106)_, so you get updates regarding my future articles!!~_

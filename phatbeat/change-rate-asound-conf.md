_http://forums.pimoroni.com/t/airdac-speaker-phat-questions/4126/27_

... after that, make sure the rate value in /etc/asound.conf is appropriate for what you wish to do, or take the rate completely out of file (which in theory should then hand over the control of rate switching to ALSA, which may allow more flexibility.

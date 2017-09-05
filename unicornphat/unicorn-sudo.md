_http://forums.pimoroni.com/t/unicorn-phat-only-works-with-terminal-and-sudo/5873/2_

It’s a limitation of the way Unicorn HAT and pHAT works, it needs low level access to the hardware which, in turn, requires root privileges. One solution to this would be to run a script continuously as root (a daemon) and communicate to that from your less privileged python process.

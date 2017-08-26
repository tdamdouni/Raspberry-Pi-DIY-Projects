#scroll-phat-swift
<a href="https://gitter.im/Sephiroth87/scroll-phat-swift?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge"><img src="https://badges.gitter.im/Join%20Chat.svg" alt="Join the chat at https://gitter.im/Sephiroth87/scroll-phat-swift" /></a>

scroll-phat-swift is a Linux library to control [Pimoroni Scroll pHAT](https://shop.pimoroni.com/collections/raspberry-pi-zero/products/scroll-phat) for Raspberry Pi.

<p align="center">
	<img src="https://raw.githubusercontent.com/Sephiroth87/scroll-phat-swift/master/snake.gif" alt="Snake" />
</p>

##Installation
Package Manager is not functional on Raspberry Pi yet, so you'll have to do it manually for now.
After cloning, compile your program adding the 2 system dependencies, the SMBus file and the scroll-phat one, like:
```
swiftc -o MyProgram -I ./SMBus/Packages/Ci2c -I ./SMBus/Packages/CioctlHelper ./SMBus/Sources/SMBus.swift ./Sources/ScrollpHAT.swift main.swift
```
You can look in the Examples folder for see how to build your program.

##Usage
No need to import anything since the library is built together with your other sources.
Create a ScrollpHAT object:
```
let pHAT = try ScrollpHAT()
```
to turn on/off an led use :
```
pHAT.setPixel(x: 0, y: 0, value: true)
try pHAT.update()
```
write a string:
```
try pHAT.writeString("SWIFT")
```
scrolling:
```
try pHAT.scroll()
try pHAT.scrollTo(0)
```
##TODO
- [x] Add missing functions (text, scrolling)
- [ ] Add documentation
- [ ] Support Package Manager

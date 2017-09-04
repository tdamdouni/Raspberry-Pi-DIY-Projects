import usb.core
import usb.util
import time

USB_IF      = 0 # Interface
USB_TIMEOUT = 5 # Timeout in MS

USB_VENDOR  = 0x1d57
USB_PRODUCT = 0xad02

dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT)

endpoint = dev[0][(0,0)][0]

if dev.is_kernel_driver_active(USB_IF) is True:
  dev.detach_kernel_driver(USB_IF)

usb.util.claim_interface(dev, USB_IF)

while True:
  control = None

  try:
      control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
      print (control)
  except:
      pass

  time.sleep(0.01) # Let CTRL+C actually exit

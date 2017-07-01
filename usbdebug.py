import usb.core
from usb.backend import libusb1
be = libusb1.get_backend()
dev = usb.core.find(backend=be)
#dev = usb.core.find(idVendor=0x0401, idProduct=0x6011)
dev.set_configuration()
#product = dev.product
#manufact = dev.manufacturer

print (dev.product )
print (dev.manufacturer)
print (dev.langids)
print (dev)

dev.write(2, 'BB')
#dev.write(2, 'b')



#msg = 'test'
#ret = dev.read(0x81, len(msg), 100)
#print (msg)
#print (ret)

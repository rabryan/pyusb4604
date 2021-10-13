DEV_VENDOR_ID = 0x0424
DEV_PRODUCT_ID = 0x2530

class USB4604():
    def __init__(self, dev):
        self._dev = dev
    
    
    def write_reg(self, reg, data_byte):
        self._dev.ctrl_transfer(0x41, 0x03, reg, 0x0, data_or_wLength = [data_byte])
    
    def read_reg(self, reg):
        return self._dev.ctrl_transfer(0xC1, 0x04, reg, 0x0, data_or_wLength = 1)
    
    #def set_gpio_dir(self, register, data_byte):
    #    self._dev.ctrl_transfer(0x41, 0x03, reg, 0x0, data_or_wLength = [data_bytes])
    

if __name__ == '__main__':
    import sys
    import usb
    import time

    dev = usb.core.find(idVendor = DEV_VENDOR_ID, idProduct = DEV_PRODUCT_ID)

    if dev is None:
        print("No usb4604 hce device found (idVendor = {} idProduct = {})".format(DEV_VENDOR_ID, DEV_PRODUCT_ID))

    
    print("Found usb4604 on bus {} addr {}".format(dev.bus, dev.address))

    ifc = USB4604(dev)
   
    #set GPIO 0-7 as outputs

    ifc.write_reg(0x833, 0xFF)
    while True:
        ifc.write_reg(0x837, 0x01)
        time.sleep(0.2)
        ifc.write_reg(0x837, 0x02)
        time.sleep(0.2)
        ifc.write_reg(0x837, 0x08)
        time.sleep(0.2)




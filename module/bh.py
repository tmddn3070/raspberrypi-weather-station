"""
Weather station bh1750 module
created: 2022-07-13
version: 0.0.1
"""
# main module
import smbus

def getlux():
    I2C_CH = 1
    BH1750_DEV_ADDR = 0x23
    #CONT_H_RES_MODE     = 0x10
    #CONT_H_RES_MODE2    = 0x11
    #CONT_L_RES_MODE     = 0x13
    #ONETIME_H_RES_MODE  = 0x20
    ONETIME_H_RES_MODE2 = 0x21
    #ONETIME_L_RES_MODE  = 0x23
    #LowResMode: Range 0 ~ 54612.5 lux, 16ms Measurement Time
    #HighResMode: Range 0 ~ 54612.5 lux, 120ms Measurement Time
    #HighResMode2: Range 0 ~ 27306.25 lux, 120ms Measurement Time
    
    i2c = smbus.SMBus(I2C_CH)
    luxbyte = i2c.read_byte_data(BH1750_DEV_ADDR, ONETIME_H_RES_MODE2, 2)
    lux = int.from_bytes(luxbyte, byteorder='big')
    return lux

def checklux():
    lux = getlux()
    if lux > 0:
        return "LUXOK"
    else:
        return "LUXKO"
import busio
import digitalio
import board
import time
import picamera
import spidev 
import RPi.GPIO as GPIO
import zbarlight
import os
import sys
import PIL
import numpy as np
from functools import partial
from adafruit_tinylora.adafruit_tinylora import TTN, TinyLoRa

#GPIO setup
## We stellen de GPIO pin 17 als input
GPIO.setmode (GPIO.BCM) 
PIN1 = 25
PIN2 = 18
PIN3 = 23
PIN4 = 24
PIN5 = 21
GPIO.setup(PIN1,GPIO.IN) 
GPIO.setup(PIN4,GPIO.IN) 
GPIO.setup(PIN2,GPIO.OUT)
GPIO.setup(PIN3,GPIO.OUT)
GPIO.setup(PIN5,GPIO.OUT)

#initialisatie
interval = 10 # Sample period in seconds
GPIO.setmode(GPIO.BCM) 	# use GPIO numbers

# Use ADC
spi = spidev.SpiDev() # create spi object
spi.open(0,1) # open spi port 0, device CS1
spi.max_speed_hz = 4000000

# Create library object using our bus SPI port for radio
spi2 = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# RFM9x Breakout Pinouts
cs = digitalio.DigitalInOut(board.D5)
irq = digitalio.DigitalInOut(board.D6)   #G0
rst = digitalio.DigitalInOut(board.D4)

# TTN Device Address, 4 Bytes, MSB
devaddr = bytearray([0x26, 0x01, 0x17, 0x62 ])

# TTN Network Key, 16 Bytes, MSB
nwkey = bytearray([ 0xEF, 0xD6, 0xD1, 0xD4, 0xB7, 0xDB, 0x64, 0x28, 0x60, 0xBE, 0x90, 0xD0, 0xD8, 0x6D, 0x03, 0xDC ])

# TTN Application Key, 16 Bytess, MSB
app = bytearray([0xB9, 0xC2, 0x67, 0x8A, 0xF9, 0xF4, 0x92, 0x24, 0x1F, 0xED, 0x2D, 0x10, 0xFF, 0x3D, 0xB6, 0x3B ])

ttn_config = TTN(devaddr, nwkey, app, country='EU')

lora = TinyLoRa(spi2, cs, irq, rst, ttn_config, channel=0)

# Data Packet to send to TTN
data = bytearray(7)

def get_image():
	with picamera.PiCamera() as camera:
		camera.resolution = (1296, 972)
		camera.start_preview()
		# Camera warm-up time
		count = 0
		while (count < 3):
			GPIO.output(PIN5,GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(PIN5,GPIO.LOW)
			time.sleep(0.5)
			count = count+1
		camera.capture('foo.jpg')
		camera.close()

#@staticmethod
def startdate(pin):
	handeling = 49
	image_taken(handeling)
def einddate(pin):
	handeling = 48 
	image_taken(handeling)
	
def image_taken(handeling):
	handeling = handeling
	spatie = 46
	spatie = spatie.to_bytes(1, 'little')
	print ('Taking picture..')
	try:
		f = 1
		#qr_count = len(os.listdir('qr_codes'))
		get_image()
		#os.system('sudo fswebcam -d /dev/video'+sys.argv[1]+' -q qr_codes/qr_'+str(qr_count)+'.jpg')
		print ('Picture taken..')
	except Exception as e:
		f = 0
		print ('Picture couldn\'t be taken with exception ' + str(e))

	

	if(f):
		print ('Scanning image..')
		f = open('foo.jpg','rb')
		qr = PIL.Image.open(f);
		qr.load()

		codes = zbarlight.scan_codes('qrcode',qr)
		if(codes==None):
			#os.remove('qr_codes/qr_'+str(qr_count)+'.jpg')
			print ('No QR code found')
			print ('handeling is:', handeling)
			#rood licht 
			GPIO.output(PIN2,GPIO.LOW)
			GPIO.output(PIN3,GPIO.HIGH)
			time.sleep(3)
		else:
			print('QR code(s):')
			print (codes)
			print ('handeling is:', handeling)	
			codes = codes[0]
			handeling = handeling.to_bytes(1, 'little')
			codes = (codes + spatie)
			codes = (codes + handeling )
			i = 0
			for c in codes:
				print(c)
				data[i] = c & 0xff
				i +=1
			# Send data packet
			print('Sending packet...')
			
			#groen licht met 
			GPIO.output(PIN3,GPIO.LOW)
			GPIO.output(PIN2,GPIO.HIGH)
			
			lora.send_data(data, len(data), lora.frame_counter)
			print('Packet Sent!')
			lora.frame_counter += 1
			time.sleep(2)


#interupt
#GPIO.add_event_detect(PIN1,GPIO.FALLING)
#GPIO.add_event_callback(PIN1,image_taken())
GPIO.add_event_detect(PIN1, GPIO.RISING, callback= startdate , bouncetime=100)
GPIO.add_event_detect(PIN4, GPIO.RISING, callback= einddate  , bouncetime=100)

while True:
	print('hallo iedereen')
	GPIO.output(PIN2,GPIO.LOW)
	GPIO.output(PIN3,GPIO.LOW)
	time.sleep(3)
	

	
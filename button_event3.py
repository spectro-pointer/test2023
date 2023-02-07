#!/usr/bin/python3
import RPi.GPIO as GPIO, time, os, subprocess

from detector3 import Detector
from time import sleep
import  logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file = '/home/pi/TEST.log'
log_format = logging.Formatter('[%(asctime)s] %(levelname)-8s [%(name)s.%(funcName)-10s:%(lineno)d] %(message)s')
file_handler = logging.FileHandler(log_file, mode='a+')
file_handler.setFormatter(log_format)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.debug('debug')

ip = 'localhost'
det = Detector(ip)

location = '/home/pi/spectrometer/spectrums'
det.location = location

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
gpio_start = 17
gpio_stop  = 18
GPIO.setup(gpio_start, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(gpio_stop , GPIO.IN, pull_up_down = GPIO.PUD_UP)


# Our function on what to do when the button is pressed
def Start(channel):
#	subprocess.call(['spectrometer3.py'])
    print("start")
    det.start()
    logger.debug("start")
def Stop(channel):
#	subprocess.call(['spectrometer3.py'])
    print("stop")
    det.stop()
    logger.debug("stop")
# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(gpio_start, GPIO.FALLING, callback = Start,bouncetime=500)
GPIO.add_event_detect(gpio_stop , GPIO.FALLING, callback = Stop,bouncetime=500 )
logger.debug("addevent")
# Now wait!
while True:
    time.sleep(1)

#import necessary libraries
import RPi.GPIO as GPIO
import time

#initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

#define a function to turn the light on then off.

def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(1)
	GPIO.output(pin,False)
	time.sleep(1)
	return

# use blinkOnce function in a loop, then cleanup!
for i in range(0,25):
	blinkOnce(22)
GPIO.cleanup()

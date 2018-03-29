#Initialize the necessary libraries
import RPi.GPIO as GPIO
import time

#initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(4, GPIO.OUT)

Light_status = "off"

while True:
	if GPIO.input(5) == True:
		if Light_status == "on":
			GPIO.output(4,False)
			Light_status = "off"
			print Light_status
		elif Light_status == "off":
			GPIO.output(4,True)
			Light_status = "on"
			print Light_status
		time.sleep(1)

print "button pushed"


GPIO.cleanup()

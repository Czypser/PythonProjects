import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

def TurnOffLEDs(x):
	for i in x:
		GPIO.output(i, False)

def RandomLED(x):
	random.choice(x)

Buttons = [17, 27]
LEDs = [22, 5, 6, 13, 19, 4]

for i in Buttons:
        GPIO.setup(i, GPIO.IN)
	print i

for i in LEDs:
	GPIO.setup(i, GPIO.OUT)
	print i

TurnOffLEDs(LEDs)

while True:
	if GPIO.input(17) == True or GPIO.input(27) == True:
		print "button pressed"
		TurnOffLEDs(LEDs)
		time.sleep(1)
		color = random.choice(LEDs)
		GPIO.output(color ,True)
		print color

GPIO.cleanup()

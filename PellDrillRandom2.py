import RPi.GPIO as GPIO
import time

RightSideHeadLED = 4
RightSideHeadButton = 18
ButtonOutput = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(ButtonOutput,GPIO.OUT)
GPIO.setup(RightSideHeadLED,GPIO.OUT)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	if GPIO.input(RightSideHeadButton) == True:
		print "button released"
		GPIO.output(RightSideHeadLED,False)
	if GPIO.input(RightSideHeadButton) == False:
		print "button pressed"
		GPIO.output(RightSideHeadLED,True)
	time.sleep(2)
GPIO.cleanup()

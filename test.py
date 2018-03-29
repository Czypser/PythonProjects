import RPi.GPIO as GPIO
import time
RightSideHeadLED = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(RightSideHeadLED,GPIO.OUT)
print "LED on"
GPIO.output(RightSideHeadLED,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(RightSideHeadLED,GPIO.LOW)
GPIO.cleanup()

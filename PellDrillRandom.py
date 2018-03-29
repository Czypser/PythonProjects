import RPi.GPIO as GPIO
import time
import random

LeftSideHeadLED = 4
LeftSideChestLED = 17
LeftSideLegLED = 27
CenterHeadLED = 22
CenterChestLED = 5
CenterLegLED = 6
RightSideHeadLED = 13
RightSideChestLED = 19
RightSideLegLED = 26

#Left Head, Center Chest, Right Leg
ButtonGroup1 = 18
#Center Head, Right Chest, Left Leg
ButtonGroup2 = 23
#Right Head, Left Chest, Center Leg
ButtonGroup3 = 24

LEDArray = [RightSideHeadLED, LeftSideHeadLED, CenterHeadLED]
ButtonArray = [ButtonGroup1, ButtonGroup2, ButtonGroup3]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDArray,GPIO.OUT)
GPIO.setup(ButtonArray, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def AllLightsOff(x):
	GPIO.output(x,False)
	time.sleep(0.1)

def LightLED(x):
	GPIO.output(x,True)

CurrentLED = random.choice(LEDArray)
LightLED(CurrentLED)

while True:
	if CurrentLED in (LeftSideHeadLED, CenterChestLED, RightSideLegLED):
		if GPIO.input(ButtonGroup1) == False:
			print ('LeftSideHeadButton Pressed')
			AllLightsOff(LEDArray)
			CurrentLED = (random.choice(LEDArray))
			LightLED(CurrentLED)
			print (CurrentLED)
			time.sleep(0.1)
	if CurrentLED in (CenterHeadLED, RightSideChestLED, LeftSideLegLED):
		if GPIO.input(ButtonGroup2) == False:
			print ('CenterHeadButtom Pressed')
			AllLightsOff(LEDArray)
			CurrentLED = (random.choice(LEDArray))
			LightLED(CurrentLED)
			print (CurrentLED)
			time.sleep(0.1)
	if CurrentLED in (RightSideHeadLED, LeftSideChestLED, CenterLegLED):
		if GPIO.input(ButtonGroup3) == False:
			print ('Right Side Headd Pressed')
			AllLightsOff(LEDArray)
			CurrentLED = (random.choice(LEDArray))
			LightLED(CurrentLED)
			print(CurrentLED)
			time.sleep(0.1)
GPIO.cleanup()

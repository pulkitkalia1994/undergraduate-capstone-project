import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.IN)
x=GPIO.input(18)
while(x==1):
	time.sleep(1)
	x=GPIO.input(18)
	
print("gas leakage")
execfile('/home/pi/motor.py')

import time
import RPi 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)                   
GPIO.setup(24, GPIO.OUT)                   
 
pwm=GPIO.PWM(24,50)                       
pwm.start(1)

pwm.ChangeDutyCycle(11.5)
time.sleep(1)
GPIO.cleanup()

execfile('/home/pi/connection.py')

import sys
sys.path.append('/home/pi/Projects/lcd')
import lcd
import time
import RPi.GPIO as GPIO
DELAY = 0.00005
LED_ON = 15
##### INIT BLOCK START #####
lcd.lcd_init()
GPIO.setwarnings(False)
GPIO.setup(LED_ON,GPIO.OUT)
time.sleep(DELAY)
##### INIT BLOCK END #####

lcd.lcd_string("this is text", 1)




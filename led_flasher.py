import sys
sys.path.append('/home/pi/Projects/lcd')
import lcd
import time
import RPi.GPIO as GPIO
BD = 0.05 #The delay for the text to work
LED_ON = 15 #GPIO the LCD Backlight is on
D = .1 #Delay for flahsing the screen
k = 0
lcd.lcd_init()
GPIO.setup(LED_ON,GPIO.OUT)
time.sleep(BD)
lcd.lcd_string("Flashing....",1)

while k < 10:
	GPIO.output(LED_ON, True)
	time.sleep(D)
	GPIO.output(LED_ON, False)
	time.sleep(D)
	k = k + 1

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

def main():
	print("ProgRan")

def lcd_pipe():
	#Text to be Wirghten to eatch line
	LineOne = "Test 1"
	LineTwo = "Test 2"
	LineThree = "Test 3"
	LineFour = "Test $"

	##Print the text to each line
	lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
	lcd.lcd_string(LineOne, 1)
	lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
	lcd.lcd_string(LineTwo, 1)
	lcd.lcd	_byte(lcd.LCD_LINE_3, lcd.LCD_CMD)
	lcd.lcd_string(LineThree, 1)
	lcd.lcd_byte(lcd.LCD_LINE_4, lcd.LCD_CMD)
	lcd.lcd_string(LineFour, 1)

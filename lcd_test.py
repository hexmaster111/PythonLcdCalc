import sys
sys.path.append('/home/pi/Projects/PythonLcdCalc')
import lcd
import time
import RPi.GPIO as GPIO
DELAY = 0.00005
LED_ON = 15

lcd.lcd_init()
GPIO.setwarnings(False)
GPIO.setup(LED_ON,GPIO.OUT)

time.sleep(0.00005)
lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
lcd.lcd_string("Raspberry Pi", 1)
lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
time.sleep(.005)
lcd.lcd_string("Model B+", 1)
lcd.lcd_byte(lcd.LCD_LINE_3, lcd.LCD_CMD)
time.sleep(.005)
lcd.lcd_string("On a",1)
lcd.lcd_byte(lcd.LCD_LINE_4, lcd.LCD_CMD)
lcd.lcd_string("4x16 DOWG",1)
#lcd.GPIO.cleanup()


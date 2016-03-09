#!/usr/bin/python
#By Trevor Gruszynski
#Devluped to simplify the lcd.py Lib
import RPi.GPIO as GPIO, time


##Define the pins
TBL_LED = 21
Y_LED = 20
CALC_LED = 16

def led_init():i
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TBL_LED, GPIO.OUT)
	GPIO.setup(Y_LED, GPIO.OUT)
	GPIO.setup(CALC_LED, GPIO.OUT)

def led_mode(mode):
        if mode == 0:# in TBL
                GPIO.output(TBL_LED, True)
                GPIO.output(Y_LED, False)
                GPIO.output(CALC_LED, False)
        if mode == 1:#In Y=
                GPIO.output(TBL_LED, False)
                GPIO.output(Y_LED, True)
                GPIO.output(CALC_LED, False)
        if mode == 2:#In calc
                GPIO.output(TBL_LED, False)
                GPIO.output(Y_LED, False)
                GPIO.output(CALC_LED, True)
        if mode == 3:#In Opts
                GPIO.output(TBL_LED, False)
                GPIO.output(Y_LED, False)
                GPIO.output(CALC_LED, False)

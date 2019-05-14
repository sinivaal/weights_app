import RPi.GPIO as GPIO
import time
from datetime import datetime

def get_weight(hx, cal_2_a, cal_2_b):
	try:
		channel_A = (hx.get_weight_A(1)+ cal_2_a)
		channel_B = (hx.get_weight_B(1)+ cal_2_b)
		hx.power_down()
		hx.power_up()
		time.sleep(0.1)
	finally:  
		cleanAndExit()
		return channel_A, channel_B

def get_time():
	time_now = datetime.now().strftime ("%H:%M:%S")
	return time_now

def get_date():
	date_now = datetime.now().strftime ("%Y-%m-%d")
	return date_now

def cleanAndExit():
	print ("Cleaning...")
	GPIO.cleanup()
	print ("Bye!")
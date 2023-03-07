#!/usr/bin/python3
import random
randnum = random.randint(-10,10)
if (randnum >= 0):
	if (randnum > 0):
		print(f"{randnum} is positive")
	else:
		print(f"{randnum} is zero")
else:
	print(f"{randnum} is negative")
	


#!/usr/bin/python3
# prints ASCII alphabet in lowercase
for i in range(97, 123):
    if i != 101 and i != 113:
	print("{}".format(chr(i)), end="")

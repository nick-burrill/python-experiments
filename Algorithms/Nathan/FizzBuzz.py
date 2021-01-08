import time
import math

list = list(range(1,101))
LN = 0

print (list)
time.sleep(1)
print ("")
print ("and now for the magic")
time.sleep(1)

while LN < 99:

	if int((LN+1)/15) == (LN+1)/15:
		list[LN] = str("fizzbuzz")
		print ("found fizzbuzz")

	elif int((LN+1)/3) == (LN+1)/3:		
		list[LN] = str("fizz")
		print ("found fizz")

	elif int((LN+1)/5) == (LN+1)/5:
		list[LN] = str("Buzz")
		print ("found buzz")

	LN = LN + 1

print (list)
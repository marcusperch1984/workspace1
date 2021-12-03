#!/usr/bin/env python3

#import pandas as pd

a = [100, 700, 600]

p1 = a[0]
p2 = a[1]
p3 = a[2]

print("hello world - array")

# 1) if / else


if (p1 > p2) and (p1 > p3):
	print("p1 is the winner with " + str(p1))
elif (p2 > p1) and (p2 > p3):
	print("p2 is the winner with " + str(p2))
else:
	print("p3 is the winner with " + str(p3))



# 2) loop

result = 0

for singleElementOfArray in a:

	if result < singleElementOfArray:
		result = singleElementOfArray

print("loop: result = " + str(result))



#print"stra[0]"



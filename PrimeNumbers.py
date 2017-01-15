#Program to print Prime Numbers in a range
#takes the input from console
from __future__ import print_function 

import sys
num1 = int(raw_input("Enter the starting number: "))
num2 = int(raw_input("Enter the last number: "))
if(num1>1):
		
	print("prime numbers in given range are:")
	for num in range(num1, num2+1):
		
		for i in range(2,num):
			if (num % i) == 0:
				break
		else:
			print(num)

else:
	print("number should be greater than 1 for prime numbers")

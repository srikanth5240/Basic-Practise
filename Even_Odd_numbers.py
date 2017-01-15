#Program to print Even and Odd Numbers in a range
#takes the input from console
#import sys
from __future__ import print_function 

num1 = int(raw_input("Enter the starting number: "))
num2 = int(raw_input("Enter the last number: "))
if(num1>0):
	#print("Even numbers in given range are:")
	for i in range(num1, num2+1):
		if i%2 == 0:
			print(i,end='')
	print("Odd numbers in given range are:")
	for i in range(num1, num2+1):
		if i%2 != 0:
			print(i)
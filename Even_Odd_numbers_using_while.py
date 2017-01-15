#Program to print Even and Odd Numbers in a range
#takes the input from console
import sys
num1 = int(raw_input("Enter the starting number: "))
num2 = int(raw_input("Enter the last number: "))
i= num1
if(num1>0):
	print("Even numbers in given range are:")
	while (i < num2+1):
		if (i%2 == 0):
			print(i)
		i=i+1

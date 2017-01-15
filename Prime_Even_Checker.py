#Program to check given number is Prime or Even
#takes the input from console
import sys
num = int(raw_input("Enter the nuber: "))

is_prime = True
if (num>1):
	for i in range(2,num):
		if (num % i) == 0:
			is_prime = False
	if is_prime == True:
		print(num,"is a prime number")
	else:
		print(num,"is not a prime number")

else:
	print("number should be greater than 1 for prime numbers")

if(num>0):	
	if ((num%2) == 0):
		print(num, "is a even number")
	else:
		print(num, "is a odd number")
else:
	print("number should be greater than zero to find even number")
	
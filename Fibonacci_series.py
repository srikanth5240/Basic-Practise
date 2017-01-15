# Program to display the Fibonacci sequence up to n-th term where n is provided by the user
from __future__ import print_function 

nterms = int(raw_input("No of termms in series are: "))

#first two terms 
num1 = int(raw_input("Enter the first number: "))
num2 = int(raw_input("Enter the second number: "))

count = 2

# check if the number of terms is valid

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(num1)
else:
   print("Fibonacci sequence upto " + str(nterms) + "terms are:")
   print(num1,",",num2,end=', ')
   while count < nterms:
       nth = num1 + num2
       print(nth,end=' , ')
       # update values
       num1 = num2
       num2 = nth
       count += 1
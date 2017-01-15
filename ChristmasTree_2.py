#Half christmas_tree
n = int(raw_input("No of lines in series for christmas tree: "))

for i in range(0, n):
	print ('*'*(i+1))


print ("===================")

for i in range(0, n):
	print ((' '*int(n-i-1)) + ('*'*int(i+1)))
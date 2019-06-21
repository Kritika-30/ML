#!/usr/bin/python3

#importing library 
import numpy as np

print('Enter the dimenions for 2D array')
# taking input from user
m,n=input().split('x')

#creation of array 'a' of random numbers
a = np.random.random((int(m),int(n)))

# saving the output in a file
f = open("numpy.txt",'w')
f.write(str(a))

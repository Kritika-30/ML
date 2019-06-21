#!/usr/bin/python3

#importing library
import numpy as np

# creation of array of elements 100-200
array1=np.arange(100,200,5)
# making that array of dimension 8x2 
array2=array1[0:16].reshape(8,2)
print(array2)

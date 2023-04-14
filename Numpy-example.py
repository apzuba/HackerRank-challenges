

#Examples of using the Numpy package

"""
Task

You are given the shape of the array in the form of space-separated integers, 
each integer representing the size of different dimensions, 
your task is to print an array of the given shape and 
integer type using the tools numpy.zeros and numpy.ones.
"""
"""
Sample Input 0

3 3 3
"""

import numpy as np

shp = tuple(map(int, input().split()))

print(np.zeros(shp, dtype=int), np.ones(shp, dtype=int),  sep='\n')






"""
Sample Input

1 4
1 2 3 4
5 6 7 8
"""

import numpy as np

N = int(input()[:1])

A = np.array([list(map(int, input().split())) for _ in range(N)])
B = np.array([list(map(int, input().split())) for _ in range(N)])

print(A+B, A-B, A*B, A//B, A%B, A**B, sep='\n')

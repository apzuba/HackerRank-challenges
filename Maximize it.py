"""
HackerRank Maximize it! problem.
"""

"""
Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
"""
#example of using Itertools package (product Module)

from itertools import product

K, M = input().split()
K = int(K)
M = int(M)
curr_best = 0

all_options = [list(map(int, input().split()[1:])) for _ in range(K)]

for option in set(product(*all_options)):
    curr_score = sum([el**2 for el in option])%M
    if curr_score > curr_best: curr_best = curr_score 
        
print(curr_best)

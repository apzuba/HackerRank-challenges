""" Task:
For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification.
"""

"""
Sample Input

4
bcdef
abcdefg
bcde
bcdef
"""
#Example of using the collections package (Counter Module)


from collections import Counter

all_words = []
for _ in range(int(input())):
    all_words.append(*(input().split()))
       
print(len(Counter(all_words).keys()))
print(*Counter(all_words).values())

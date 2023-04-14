"""
A valid credit card from ABCD Bank has the following characteristics:

► It must start with a ,  or .
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digits.
"""

"""
Sample Input

6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
"""

#Example of using the Regex in Python

import re

for _ in range(int(input())):
    c_card = input().strip()
    pattern = re.compile(
    r"^"
    r"^[456][0-9]{3}-?([0-9]{4}-?){3}$"
    r"$"
    )
    order = pattern.search(c_card)
    repeat = re.search(r".*(\d)(-?\1){3}", c_card)
    
    if bool(order) and not bool(repeat): print("Valid")
    else: print("Invalid")

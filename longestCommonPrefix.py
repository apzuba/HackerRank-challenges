"""
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:

        test_l = strs
        the_current_winner = []
        
        if len(test_l) == 1:
            return test_l[0]
        elif len(test_l) == 0:
            return ""
        else:
            pass

        len_min = len(min(test_l))

        while True:
            for i in range(1,len_min+1):
                for n in range(1, len(test_l)):
                    if test_l[n-1][0:i] == test_l[n][0:i]:
                        pass
                    else:
                        if len(the_current_winner) != 0:
                            print(the_current_winner[0])
                            return(the_current_winner[0])
                        else:
                            return ""
                the_current_winner.clear()
                the_current_winner.append(test_l[n][0:i])
            print(the_current_winner[0])
            return(the_current_winner[0])

Solution.longestCommonPrefix(strs = ["flower","flow","flight"]) 
Solution.longestCommonPrefix(strs = ["dog","racecar","car"])
Solution.longestCommonPrefix(strs = ["d"])
Solution.longestCommonPrefix(strs = [""])

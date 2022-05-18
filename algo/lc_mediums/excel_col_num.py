# Rather than scanning from right to left as described in Approach 1, we can also scan the title from left to right.

# For example, if we want to get the decimal value of string "1337", we can iteratively find the result by scanning the string from left to right as follows:

# '1' = 1
# '13' = (1 x 10) + 3 = 13
# '133' = (13 x 10) + 3 = 133
# '1337' = (133 x 10) + 7 = 1337
# Instead of base-10, we are dealing with base-26 number system. Based on the same idea, we can just replace 10s with 26s and convert alphabets to numbers.

# For a title "LEET":

# L = 12
# E = (12 x 26) + 5 = 317
# E = (317 x 26) + 5 = 8247
# T = (8247 x 26) + 20 = 214442

#left to right
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res  = 0
        for i in columnTitle:
            res *= 26
            res += ord(i) - ord('A') + 1
        
        return res

#right to left - didnt understand this solution. revisit later. 
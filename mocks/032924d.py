"""
Given a string s, return the number of homogenous substrings of s. 
Since the answer may be too large, return it modulo 10^9 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
Example 2:

Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".
"""

def countHomogenous(s: str) -> int:
    answer = 0
    left, right = 0, 0
    while right < len(s):
        # curr = s[left]
        # old_right = right
        while right <= len(s) - 1 and s[right] == s[right + 1]:
            right += 1
        print((left, right))
        length = right - left
        print(length)
        answer += length * (length + 1) // 2
        left += length
        right += 1
    return answer

assert countHomogenous("abbcccaa") == 13
assert countHomogenous("xy") == 2
assert countHomogenous("zzzzz") == 15

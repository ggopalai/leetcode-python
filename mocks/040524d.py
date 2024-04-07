"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. 
You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
"""

#s[i].lower() == s[i + 1].lower() and s[i] != s[i + 1]

def makeGood(s: str) -> str:
    # check = [True] * len(s)
    stack = []
    # ptr = -1
    i = 0
    while i < len(s):
        if stack:
            ch = stack.pop()
            if ch.lower() == s[i].lower() and s[i] != ch:
                i += 1
                continue
            stack.extend([ch, s[i]])
            i += 1
            continue
        stack.append(s[i])
        i += 1
        # if i != len(s) - 1:
        #     if s[i].lower() == s[i + 1].lower() and s[i] != s[i + 1]:
        #         # check[i] = False
        #         # check[i + 1] = False
        #         i += 2
        #         continue
        # if ptr != -1:
        #     if s[i].lower() == s[ptr].lower() and s[i] != s[ptr]:
        #         check[i] = False
        #         check[ptr] = False
        #         while check[ptr] != False:
        #             ptr -= 1
        #         i += 1
        #         continue
    #     ptr = i
    #     i += 1
    # print(ptr)
    # print(check)
    # ans = ""
    # for i in range(len(s)):
    #     if check[i]:
    #         ans += s[i]
    print(stack)
    return "".join(stack)
            

assert makeGood("leEeetcode") == "leetcode"
assert makeGood("abBAcC") == ""
assert makeGood("s") == "s"
assert makeGood("jeSsEJ") == ""



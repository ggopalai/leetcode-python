# Naive method - find between two, use the same function for other functions. 

# Other solutions - divide and conquer, tries. 

from typing import List


def lcpTwo(s: str, r: str):
        i = j = 0
        wc = str()
        while i < len(s) and j < len(r):
            if s[i] == r[j]:
                wc += s[i]
                i += 1
                j += 1
            else:
                break
        return wc

def lcpGroup(l : List[str]) -> str:

    prefix = l[0]
    for i in l:
        prefix = lcpTwo(prefix, i)
    return prefix

print(lcpTwo("technology", "technicality"))

print(lcpGroup(["technology", "technicality", "techely"]))


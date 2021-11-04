#! /Users/ggopalai/.pyenv/shims/python3
import sys 

def binary(list, key):
    l = 0
    h = len(list) - 1
    while l <= h:
        m = int((l + h)/2)
        if list[m] == key:
            print(f"found key at {m+1}")
            return
        elif key < list[m]:
            h = m - 1
        else:
            l = m + 1

    print("key not found")   

if __name__ == "__main__":
    binary([1, 5, 18, 20, 45, 67], int(sys.argv[1]))
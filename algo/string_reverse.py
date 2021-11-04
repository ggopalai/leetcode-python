import sys 

# gagan -> len(gagan) = 5, 

def reverse(s: str) -> str:
    res = ''
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    return res

if __name__ == '__main__':
    print(reverse(sys.argv[1]))
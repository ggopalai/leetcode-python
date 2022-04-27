import sys 

def reverse(s: str) -> str:
    res = ''
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    return res

if __name__ == '__main__':
    try:  
        print(reverse(sys.argv[1]))
    except IndexError:
        print('please enter string to reverse')
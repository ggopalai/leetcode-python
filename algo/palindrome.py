import sys 

def palindrome(n: int) -> bool:
    x = n
    sum = 0
    while x > 0:
        sum = sum * 10 + (x % 10)
        x = int(x / 10)

    if sum == n:
        return True
    
    return False

if __name__ == '__main__':
    print(palindrome(int(sys.argv[1])))
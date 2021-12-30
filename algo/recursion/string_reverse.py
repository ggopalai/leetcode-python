import sys 

def reverse(s: str):
    if not s:
        return 
    else:
        reverse(s[1:])
        print(s[0], end='')

if __name__ == '__main__':
    reverse("gagan123")


# solution from sanfoundry.com
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(reverse(a))
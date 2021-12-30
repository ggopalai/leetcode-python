#used this a module, to access linear method from python interpreter

a = [1, 4, 5, 12, 5 , 6 ,18, 45]

def linear(key):
    for i in a:
        if i == key:
            print('found at {}'.format(a.index(i)))
            exit()
    print('value not found')


if __name__ == '__main__':
    key = input('enter number to search :')
    linear(key)
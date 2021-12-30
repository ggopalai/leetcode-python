def bubble(l):
    for i in range(0, len(l)):
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

if __name__ == "__main__":
    l = [4, 7 , 1, 10, 78, 0 , -1]
    print(bubble(l))
from typing import List

def mergesort(a: List, l: int, r: int) -> List:
    if l < r:
        mid = (l+r)//2
        # print(mid)
        t1 = mergesort(a, l, mid)
        t2 = mergesort(a, mid+1, r)
        b = merge(t1.extend(t2), l, mid, mid+1, r)
        # print(b)
        return b

    return a[l:r+1]


def merge(a: List, l1: int, r1: int, l2: int, r2: int) -> List:
    temp = list()
    while l1 <= r1 and l2 <= r2:
        if a[l1] < a[l2]:
            # print(f'left - {a[l1]}')
            temp.append(a[l1])
            l1 += 1
        else:
            # print(f'right - {a[l2]}')
            temp.append(a[l2])
            l2 += 1

    if l1 > r1:
        # print('writing from right')
        while l2 <= r2:
            temp.append(a[l2])
            l2 += 1

    if l2 > r2:
        # print('writing from left')
        while l1 <= r1:
            temp.append(a[l1])
            l1 += 1
    
    # print(temp)
    return temp

if __name__ == '__main__':
    unsorted_list = [4, 3, 2, 1]
    sorted = mergesort(unsorted_list, 0, len(unsorted_list)-1)
    print(sorted)
from typing import List

def mergesort(a: List, l: int, r: int) -> List:
    if l < r:
        mid = (l+r)//2
        # print(mid)
        t1 = mergesort(a, l, mid)
        print(f't1 - {t1}')
        t2 = mergesort(a, mid+1, r)
        print(t2)
        b = merge(t1 + t2, l, mid, mid+1, r)
        print(b)
        return b

    return a[l:r+1]


def merge(a: List, l1: int, r1: int, l2: int, r2: int) -> List:
    print(f'inside merge - {a}')
    temp = list()
    print(f'{l1} {r1} {l2} {r2}')
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


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(array):
            if len(array) > 1:

                #  r is the point where the array is divided into two subarrays
                r = len(array)//2
                L = array[:r]
                M = array[r:]

                # Sort the two halves
                mergeSort(L)
                mergeSort(M)

                i = j = k = 0

                # Until we reach either end of either L or M, pick larger among
                # elements L and M and place them in the correct position at A[p..r]
                while i < len(L) and j < len(M):
                    if L[i] < M[j]:
                        array[k] = L[i]
                        i += 1
                    else:
                        array[k] = M[j]
                        j += 1
                    k += 1

                # When we run out of elements in either L or M,
                # pick up the remaining elements and put in A[p..r]
                while i < len(L):
                    array[k] = L[i]
                    i += 1
                    k += 1

                while j < len(M):
                    array[k] = M[j]
                    j += 1
                    k += 1
        
        mergeSort(nums)
        
        return nums
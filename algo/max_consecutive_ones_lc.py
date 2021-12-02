from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
        maxi = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if count > maxi:
                    maxi = count
                count = 0
        if count > maxi: #comparision when last number is 1
            maxi = count
        
        return maxi

if __name__ == '__main__':
    inp = [1,1,0,0,0,1]
    print(findMaxConsecutiveOnes([inp]))
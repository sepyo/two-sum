from itertools import combinations
#from typing import List

def twoSum(nums, target):
#def twoSum(self, nums:List[int], target:int)->List[int]:
    for i, j in combinations(range(len(nums)), 2):
        if nums[i] + nums[j] == target:
            return [i, j]
    return [-1, -1]

#a = [1, 3, 4, 2, 8, 9, 1, 3013 ,3,1, 3,1,3,  1, 3]
#print(twoSum(a, 3017))


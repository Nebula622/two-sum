from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dict = {}
    for i, num in enumerate(nums):
        complement = target - num 
        if complement in dict:
            return [dict[complement], i]        
        dict[num] = i   
    return []
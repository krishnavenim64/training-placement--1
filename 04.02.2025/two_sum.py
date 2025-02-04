import numpy as np
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for idx, n in enumerate(nums):
            if target - n in d.keys():
                return [d[target-n], idx]
            d[n] = idx


        

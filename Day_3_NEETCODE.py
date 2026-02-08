#BRUTE FORCE!!!!
def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
                  
#USING HASHING!!!

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i, num in enumerate(nums):
            diff = target-num
            if diff in seen:
                return [seen[diff], i]

            seen[num] = i

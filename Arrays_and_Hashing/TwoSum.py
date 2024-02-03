# Your Python code goes here


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j



check = Solution()
nums = [11,2,15,7]
target = 17
print(check.twoSum(nums,target))
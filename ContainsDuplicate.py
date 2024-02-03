
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
            return False
                
        



check = Solution()
nums = [1,2,3,4,1]
print(check.containsDuplicate(nums))
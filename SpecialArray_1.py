class Solution(object):
    def isArraySpecial(self, nums):
       for i in range(1,len(nums)):
        if nums[i] % 2== nums[i-1] % 2:
            return False
       return True     

nums=[1,2,3]
sol=Solution()
print(sol.isArraySpecial(nums))       
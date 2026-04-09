class Solution(object):
    def getConcatenation(self, nums):
        #return nums + nums

        '''n=len(nums)
        for i in range(n):
            nums.append(nums[i])
        return nums  '''

        #return nums * 2

        nums.extend(nums)
        return nums  
        
nums=[1,2,1] 
sol=Solution()
print(sol.getConcatenation(nums))       
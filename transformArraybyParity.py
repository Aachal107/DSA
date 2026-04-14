class Solution(object):
    def transformArray(self, nums):
        output=[]
        for num in nums:
            if num%2==0:
                output.append(0)
            else:
                output.append(1)

        output.sort()
        return output            
        
nums=[4,3,2,1] 
sol=Solution()
print(sol.transformArray(nums))       
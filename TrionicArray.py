class Solution(object):
    def isTrionic(self, nums):
        phase=0
        for i in range(1,len(nums)):
            if phase==0 and nums[i] > nums[i-1]:
                phase=1
                continue

            if phase==1 and nums[i] < nums[i-1]:
                phase=2
                continue

            if phase==2 and nums[i] > nums[i-1]:
                phase=3
                continue


            if phase==0 and nums[i] <= nums[i-1]:
                return False

            if phase==1 and nums[i] <= nums[i-1]:
                return False 

            if phase==2 and nums[i] >= nums[i-1]:
                return False

            if phase==3 and nums[i] <= nums[i-1]:
                return False           
                
        return phase==3                    
        
nums=[1,3,5,4,2,6]
#nums=[2,1,3]
sol=Solution()
print(sol.isTrionic(nums))        
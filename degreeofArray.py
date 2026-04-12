class Solution(object):
    def findShortestSubArray(self, nums):
         count={}
         start={}
         end={}
         for i in range(0,len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
            else:
                count[nums[i]]+=1

            if nums[i] not in start:
                start[nums[i]]=i
                end[nums[i]] = i
            else:
                end[nums[i]] = i

         res = len(nums)
         degree=max(count.values())
         for i in count:
             if count[i]  == degree:
                res=min(res,end[i] - start[i] + 1)

         return res                           
        
nums=[1,2,2,3,1]
sol=Solution()
print(sol.findShortestSubArray(nums))        
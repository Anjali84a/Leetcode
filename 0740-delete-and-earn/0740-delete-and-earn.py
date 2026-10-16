class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        points=[0]*(max(nums)+1)
        for x in nums:
            points[x]+=x
        prev2=0
        prev1=0
        for i in range(len(points)):
            curr=max(prev1,prev2+points[i])
            prev2=prev1
            prev1=curr
        return prev1
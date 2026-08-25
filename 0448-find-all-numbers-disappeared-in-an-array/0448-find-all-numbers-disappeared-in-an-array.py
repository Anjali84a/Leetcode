class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s1=set(nums)
        ans=[]
        for i in range(n):
            if i+1 not in s1:
                ans.append(i+1)
        return ans
        
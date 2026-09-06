class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        ans=""
        count=0
        for i in range(len(num)-1,0,-1):
            if num[i]=='0':
                count+=1
            else:
                break
        ans=num[0:len(num)-count]
        return ans
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans=[]
        if x<0:
            return False
        while x>=1:
            ans.append(int(x%10))
            x=x/10
        if ans[::]==ans[::-1]:
            return True
        return False
        
        
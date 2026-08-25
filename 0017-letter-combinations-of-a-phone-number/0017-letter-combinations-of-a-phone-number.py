class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        com={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        ans=[""]
        for digit in digits:
            new=[]
            for x in ans:
                for ch in com[digit]:
                    new.append(x+ch)
            ans=new
        return ans
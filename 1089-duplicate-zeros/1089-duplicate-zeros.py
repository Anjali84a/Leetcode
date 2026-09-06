class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ans=[]
        for i in range(len(arr)):
            if arr[i]==0:
                ans.append(arr[i])
                ans.append(arr[i])
                
            else:
                ans.append(arr[i])
        for i in range(len(arr)):
            arr[i]=ans[i]

        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=nums1+nums2
        n=len(arr)+1
        ans=0
        if(len(arr)<=1):
            return arr[0]
        arr.sort()
        if n%2!=0:
            x=int(n/2)-1
            y=int(n/2)
            ans=(arr[x]+arr[y])/2
        else :
            x=int(n/2)-1
            ans=arr[x]
            
        return ans
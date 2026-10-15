class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        maxx= 0
        if(satisfaction[0]>0):
            sum=0
            for i in range(1,len(satisfaction)+1):
                x=i*satisfaction[i-1]
                sum += x
                print(x)
            return sum

        while(satisfaction and satisfaction[0]<0):
            n=len(satisfaction)
            sum=0
            for i in range(1,n+1):
                x=i*satisfaction[i-1]
                sum += x
            maxx=max(sum,maxx)
            satisfaction.pop(0) 
        return maxx
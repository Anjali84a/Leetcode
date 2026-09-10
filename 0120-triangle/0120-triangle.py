class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        if n<=1:
            return triangle[0][0]
        for i in range(n-2,0,-1):
            for j in range(0,i+1):
                triangle[i][j]= min(triangle[i+1][j]+triangle[i][j],
                                    triangle[i+1][j+1]+triangle[i][j])
        sum=min(triangle[1][0],triangle[1][1])
        sum+=triangle[0][0]
        return sum
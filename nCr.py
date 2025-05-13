class Solution:
    def nCr(self, n, r):
        # code here
        a=1
        b=1
        for i in range(1,n+1):
            a*=i
        for j in range(1,n-r+1):
          b*=j
        c=1
        for k in range(1,r+1):
            c*=k
        result=a//(c*b)
        return result
            

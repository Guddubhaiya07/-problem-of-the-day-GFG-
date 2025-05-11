from typing import List


class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here
        arrs=[]
        n=len(arr)
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=arr[j]
                arrs.append(sum)
        arrs.sort(reverse=True)
        return arrs[k-1]
if __name__ == "__main__":
    arr = [20, -5, -1]
    k = 3
    print(kthLargest(arr, k))

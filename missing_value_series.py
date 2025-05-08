class Solution:
    def findMissing(self, arr):
       n = len(arr)
       diff1 = arr[1] - arr[0]
       diff2 = arr[-1] - arr[-2]
       diff3 = (arr[-1] - arr[0]) // n
    
       if diff1 == diff2:
         diff = diff1
       elif diff1 == diff3:
         diff = diff1
       else:
         diff = diff2

       if diff == 0:
         return arr[0]
         #d=(arr[-1]-arr[0])//n
       s = ((2 * arr[0] + (len(arr)) * diff) * (len(arr)+1)) // 2
    

       missing = s - sum(arr)
       return int(missing)
if __name__ == "__main__":
    arr = [2, 4, 8, 10, 12, 14]
    missing = findMissing(arr)
    print(missing)
           
            

class Solution:

	def findMaximum(self, arr):
		# code here
		for i in range(len(arr)-1):
		    if arr[i]>=arr[i+1]:
		        return arr[i]
		        
if __name__ == "__main__":
    arr = [1, 2, 4, 5, 7, 8, 3]
    print(findMaximum(arr))

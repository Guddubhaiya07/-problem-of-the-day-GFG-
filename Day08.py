#Longest Subarray with Majority Greater than K
class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        prefix_sum = 0
        first_occurrence = {}  # maps prefix_sum to first index
        max_len = 0

        for i in range(n):
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            # If prefix sum > 0 from index 0 to i
            if prefix_sum > 0:
                max_len = i + 1

            # Else check if prefix_sum - 1 was seen before
            if (prefix_sum - 1) in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix_sum - 1])

            # Store first occurrence of this prefix_sum
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i

        return max_len

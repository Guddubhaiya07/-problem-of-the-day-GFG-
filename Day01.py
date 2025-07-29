#Majority Element II


class Solution:
    def findMajority(self, arr):
        if not arr:
            return []

        # Step 1: Find candidates
        count1 = count2 = 0
        candidate1 = candidate2 = None

        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify counts
        result = []
        for c in set([candidate1, candidate2]):
            if arr.count(c) > len(arr) // 3:
                result.append(c)

        return sorted(result)  # sort for consistent output

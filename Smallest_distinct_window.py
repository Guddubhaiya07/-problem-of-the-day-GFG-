#🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋
class Solution:
    def findSubString(self, str):
        a=set(str)
        return len(a)
#This code is write but not pass all test cases
🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊
class Solution:
    def findSubString(self, s):
        n = len(s)
        distinct_chars = len(set(s))  # total distinct characters
        char_count = {}
        min_len = n + 1
        count = 0  # how many distinct chars are currently in window
        start = 0

        for end in range(n):
            char_count[s[end]] = char_count.get(s[end], 0) + 1

            if char_count[s[end]] == 1:
                count += 1

            while count == distinct_chars:
                if end - start + 1 < min_len:
                    min_len = end - start + 1

                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    count -= 1
                start += 1

        return min_len
        

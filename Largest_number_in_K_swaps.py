class Solution:
    def findMaximumNum(self, s, k):
        self.max_num = s
        self.helper(list(s), k, 0)
        return self.max_num

    def helper(self, s_list, k, index):
        if k == 0 or index == len(s_list):
            return

        max_char = max(s_list[index:])
        for j in range(len(s_list) - 1, index - 1, -1):
            if s_list[j] == max_char and s_list[j] != s_list[index]:
                # Swap
                s_list[index], s_list[j] = s_list[j], s_list[index]
                current_str = ''.join(s_list)

                if current_str > self.max_num:
                    self.max_num = current_str

                self.helper(s_list, k - 1, index + 1)

                # Backtrack
                s_list[index], s_list[j] = s_list[j], s_list[index]

        # Important: also explore without swap if no better char or we skip swap
        if max_char == s_list[index]:
            self.helper(s_list, k, index + 1)
if __name__ == "__main__":
  
    s = "7599"
    k = 2

    print(findMaximumNum(s, k))

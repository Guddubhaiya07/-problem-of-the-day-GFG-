#Balancing Consonants and Vowels Ratio

class Solution:
    def countBalanced(self, arr):
        def is_vowel(ch):
            return ch in {'a', 'e', 'i', 'o', 'u'}

        
        word_balances = []
        for word in arr:
            balance = 0
            for ch in word:
                if is_vowel(ch):
                    balance += 1
                else:
                    balance -= 1
            word_balances.append(balance)

       
        from collections import defaultdict
        balance_freq = defaultdict(int)
        balance_freq[0] = 1 
        total = 0
        prefix_sum = 0

        for b in word_balances:
            prefix_sum += b
            total += balance_freq[prefix_sum]
            balance_freq[prefix_sum] += 1

        return total

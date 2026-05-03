class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # 1.Brute Force Arrroach
        maxLen = 0
        for i in range(len(s)):
            freq = [0]*26
            max_freq = 0

            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('A')] +=1
                max_freq = max(max_freq, freq[ord(s[j]) - ord('A')])

                window_len = j-i+1
                replace = window_len - max_freq

                if replace <= k:
                    maxLen = max(maxLen, window_len)
        
        return maxLen

        # 2.Optimal Arrroach

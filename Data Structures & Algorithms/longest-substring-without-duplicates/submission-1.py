class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 1. Brute Force
        # maxLen = 0

        # for i in range(len(s)):
        #     hash_set = [0] * 256

        #     for j in range(i, len(s)):
        #         if (hash_set[ord(s[j])] == 1):
        #             break
        #         hash_set[ord(s[j])] = 1

        #         current_len = j - i + 1
        #         maxLen = max(current_len, maxLen)
        
        # return maxLen


        #2. Optimal approach

        hash_set = [-1] * 256
        l, r, maxLen = 0, 0, 0

        while r<len(s):
            if hash_set[ord(s[r])] != -1:
                l = max(hash_set[ord(s[r])] + 1, l)
            
            curr_len = r-l+1
            maxLen = max(curr_len, maxLen)

            hash_set[ord(s[r])] = r

            r+=1

        return maxLen




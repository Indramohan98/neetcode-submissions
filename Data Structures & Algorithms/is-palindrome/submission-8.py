class Solution:

    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join([ch for ch in s if ch.isalnum()]).lower()
        reversedMystr = new_str[::-1]
        return new_str == reversedMystr

        
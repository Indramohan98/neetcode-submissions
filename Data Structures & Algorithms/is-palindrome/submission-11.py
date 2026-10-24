class Solution:
    def isPalindrome(self, s: str) -> bool:

        # nstr = ""
        # res = True
        # for ch in s:
        #     if ch.isalnum():
        #         nstr +=ch.lower()

        # start, end = 0, len(nstr)-1

        # while(start <= end):
        #     if nstr[start] != nstr[end]:
        #         res = False
        #     start+=1
        #     end-=1
        # return res        

        start, end = 0, len(s)-1

        while (start < end):
            while (start < end and not s[start].isalnum()):
                start+=1
            while (start < end and not s[end].isalnum()):
                end-=1
            if s[start].lower() != s[end].lower():
                return False
            start+=1
            end-=1
        return True
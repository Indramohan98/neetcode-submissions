class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # 1.Brute Force -> O (N * 2)
        # res = 0
        # store = set(nums)

        # for num in nums:
        #     streak, curr = 0, num
        #     while curr in store:
        #         streak += 1
        #         curr += 1
        #     res = max(streak, res)
        # return res

        # 2. Better Approach -> O (n log n)
        nums.sort()
        currLen = 1
        maxLen = 1

        if len(nums) == 0:
            return 0
        
        for i in range(len(nums)-1):
            print(i)
            if nums[i] == nums[i+1]:
                continue
            if nums[i]+1 == nums[i+1]:
                currLen += 1
            else:
                maxLen = max(maxLen, currLen)
                currLen = 1

        return max(maxLen, currLen)



                        

        
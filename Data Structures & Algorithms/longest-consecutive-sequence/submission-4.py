class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # 1. Better Approach
        nums.sort()
        currlen = 1
        maxlen = 1
        
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            
            if nums[i] + 1 == nums[i+1]:
                currlen+=1
            else:
                maxlen = max(currlen, maxlen)
                currlen = 1
        print(currlen, maxlen)
        return max(maxlen, currlen)

    # 2. Optimal Approach
        # numset = set(nums)
        # longest = 0

        # for num in numset:
        #     if(num - 1) not in numset:
        #         length = 1
        #         while (num+length) in numset:
        #             length+=1
        #         longest = max(length, longest)
        
        # return longest
        
        
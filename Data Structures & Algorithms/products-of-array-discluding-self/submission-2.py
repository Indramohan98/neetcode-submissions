class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 1.Brute Force - O (N * 2)
        # res = []
        # for i in range(len(nums)):
        #     mul = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             mul *= nums[j]
        #     res.append(mul)
        # return res

        # 2. Better
        # prod, zero_cnt = 1, 0

        # for num in nums:
        #     if num:
        #         prod *= num
        #     else:
        #         zero_cnt += 1

        # if zero_cnt > 1:
        #     return [0] * len(nums)
        
        # res = [0] * len(nums)
        # for i, v in enumerate(nums):
        #     if zero_cnt:
        #         res[i] = 0 if v else prod
        #     else:
        #         res[i] = prod // v
        
        # return res

        # 3. Optimal Solution
        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[n-1] = 1

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res


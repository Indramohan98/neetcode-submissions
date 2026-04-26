class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. Brute force
        # res = []
        # for i in range(len(nums)):
        #     temp = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             temp = temp*nums[j]
        #             print(i, j, nums[j])
        #         else:
        #             continue
        #     res.append(temp)
        # return res

        # 2. Better Approach
        # zero_count = 0
        # prod = 1

        # for num in nums:
        #     if num:
        #         prod*=num
        #     else:
        #         zero_count+=1
        
        # if zero_count > 1: return [0] * len(nums)

        # res = [0] * len(nums)

        # for i, v in enumerate(nums):
        #     if zero_count:
        #         res[i] = 0 if v else prod
        #     else:
        #         res[i] = prod // v
        
        # return res

        # 3. Optimal approach

        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
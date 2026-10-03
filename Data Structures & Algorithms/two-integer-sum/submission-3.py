class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        # Brute Force O(N * 2)

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        #2. Optimal O (N) 

        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i
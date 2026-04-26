class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #1.Brute Force
        # ls = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 sorted_sub = sorted([nums[i], nums[j], nums[k]])
        #                 if sorted_sub not in ls:
        #                     ls.append(sorted_sub)
        # return ls

        #2. Better Approa
        # ls = set()
        # for i in range(len(nums)):
        #     my_set = set()
        #     for j in range(i+1, len(nums)):
        #         third = -(nums[i]+nums[j])
        #         if third in my_set:
        #             sorted_ls = tuple(sorted([nums[i], nums[j], third]))
        #             ls.add(sorted_ls)
        #         my_set.add(nums[j])

        # return [list(t) for t in ls]

        #3. Optimal solution - 2 pointer
        nums.sort()  # Step 1: Sort
        res = []
    
        for i in range(len(nums)):
            # Step 2: Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
    
            left, right = i + 1, len(nums) - 1
    
            # Step 3: Two-pointer traversal
            while left < right:
                total = nums[i] + nums[left] + nums[right]
    
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
    
                    # Step 4: Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
    
                    left += 1
                    right -= 1
    
        return res


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Brute O(N*2)
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             if curr == nums[j]:
        #                 return True
        
        # return False


        st = set()

        for elem in nums:
            if elem not in st:
                st.add(elem)
            else:
                return True
        
        return False

                

        
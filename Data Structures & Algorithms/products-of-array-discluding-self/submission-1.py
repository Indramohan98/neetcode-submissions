class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            element=1
            for j in range(len(nums)):
                if j!=i:
                    element*=nums[j]
            result.append(element)
        return result
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
# 2. Better Approach
        # hm = {}
        # for i in range(len(numbers)):
        #     temp = target - numbers[i]
        #     if hm.get(temp):
        #         return [hm[temp], i+1]
        #     hm[numbers[i]] = i+1

        # return []
#3. optimal Approach
        left = 0
        right = len(numbers)-1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left+1, right+1]
            elif curr_sum < target:
                left+=1
            else:
                right-=1
        
        return []
        
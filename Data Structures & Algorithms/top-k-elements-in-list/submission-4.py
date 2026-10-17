class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 1. Brute force O(n log n)

        # hashmap = {}
        # for num in nums:
        #     hashmap[num] = hashmap.get(num, 0) + 1
        
        # hashmap = dict(sorted(hashmap.items(), key=lambda item:item[1], reverse=True))

        # # print(hashmap)
        # # res = list(hashmap.keys())[:k]
        
        # return list(hashmap.keys())[:k]


        # 2. Better Solution - O(n)

        hashmap = {}
        bucket = [[] for i in range(len(nums)+1)]

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key, val in hashmap.items():
            bucket[val].append(key)

        res  = []

        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
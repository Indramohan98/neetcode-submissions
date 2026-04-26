class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
    
        # sorted_keys = sorted(freq, key=freq.get, reverse=True)
        # return sorted_keys[:k]


        freq = {}
        bucket = [[] for i in range(len(nums)+1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for n, c in freq.items():
            bucket[c].append(n)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
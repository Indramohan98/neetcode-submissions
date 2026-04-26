class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if(dic.get(num) == None):
                dic[num] = 1
            else:
                dic[num] += 1

        sortedDict = dict(sorted(dic.items(), key= lambda item: item[-1], reverse=True))
        arr = list(sortedDict.keys())
        
        res = []
        for i in range(k):
            res.append(arr[i])

        return res

        
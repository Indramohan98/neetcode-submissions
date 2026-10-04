class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #1 Brute Force (Hashmap)

        # hashmap = defaultdict(list)
        # for i in range(len(strs)):
        #     sortedS = "".join(sorted(strs[i]))
        #     hashmap[sortedS].append(strs[i])

        # return list(hashmap.values())

        #2. Optimal Hash Table

        hashtable = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for ch in str:
                count[ord(ch) - ord('a')] += 1
            hashtable[tuple(count)].append(str)
        return list(hashtable.values())
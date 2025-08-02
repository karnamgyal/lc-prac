from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1
        
        freq = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

        result = []
        for pair in freq[:k]:
            result.append(pair[0])

        return result
class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        sorted_count = sorted(count, key=lambda x: count[x], reverse = True)
        return sorted_count[:k]

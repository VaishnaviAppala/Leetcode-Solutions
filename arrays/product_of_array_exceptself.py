class Solution(object):
    def productExceptSelf(self, nums):
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        suffix = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        answer = []
        for i in range(len(nums)):
            answer.append(prefix[i] * suffix[i])
        return answer

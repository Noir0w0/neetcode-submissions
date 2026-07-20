class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        left = 1
        right = 1

        for i in range(1,n):
            res[i] = left * nums[i-1]
            left = left * nums[i-1]

        for i in range(n-2, -1, -1):
            res[i] = right * nums[i+1] * res[i]
            right = right * nums[i+1]

        return res

            # 1 2 4 6 8
            # 1 1 2 8 48
            # 1 1 2 8 48

            # 1 2 4 6 8
            # 1 1 2 8 48
            # 1 1 1 1 1
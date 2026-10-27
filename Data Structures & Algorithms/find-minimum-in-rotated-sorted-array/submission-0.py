class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0                 # first index
        right = len(nums) - 1    # last index

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum is to the right of mid
                left = mid + 1
            else:
                # Minimum is at mid or to its left
                right = mid

        return nums[left]
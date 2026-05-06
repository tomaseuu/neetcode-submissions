

# UMPIRE

# Understand:
# - Input: list of integers
# - Output: integer
# Understanding: Return the longest consecutive sequence

# Plan:
# 1. If nums is empty, return 0.
# 2. Sort nums.
# 3. Start current_length = 1 and longest = 1.
# 4. Loop through nums starting at index 1.
# 5. If nums[i] is the same as nums[i - 1], skip it.
# 6. If nums[i] == nums[i - 1] + 1, add 1 to current_length.
# 7. Otherwise, reset current_length back to 1.
# 8. Keep updating longest.
# 9. Return longest.

#Implement:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()

        longest = 1
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            
            elif nums[i] == nums[i - 1] + 1:
                current_length += 1
            else:
                current_length = 1
            
            if current_length > longest:
                longest = current_length
        
        return longest




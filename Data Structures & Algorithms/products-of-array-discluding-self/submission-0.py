class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result




# Thoughts:


# I need to return an output where output[i] is the product of all 
# the elements of num except nums[i]


# input: [1, 2, 3]



#indexes = 0, 1, 2

#i = 0

#loop: 2 * 3 = 6

#at index 0, it would be 6
#then we would increase the i to move to the next index.
#i++
#index is now 1, and it would take index 1 multiply with index 3
#which results in 3

#so we need a loop to go through the indexes.
#we need to increment the indexes after each loop
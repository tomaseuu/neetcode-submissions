class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output=[]
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    output += i,j
                    return output

        return None
    



# nums = [ 3,4,5,6], target = 7
# output: [0,1]

# Thought process:
# Same idea with array hashing, we need two loops. One will go through all the indexes, and the other one would go
# +1 and through all the indexes then compare each other.

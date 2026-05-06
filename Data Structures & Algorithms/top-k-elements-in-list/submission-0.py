class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # STEP 1: Build a frequency map: value -> count
        freq = {}         # start empty
        for x in nums:    # loop over each element in nums
            freq[x] = freq.get(x, 0) + 1
        # STEP 2: Build buckets where index = frequency
        n = len(nums)
        buckets = [[] for i in range (n + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # STEP 3: Walk buckets from high freq -> low and collect k numbers
        res = []
        for f in range(n, 0, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


# Input:  [1, 2, 2, 3, 3, 3].  k = 2

# Output: ]2,3] -> 2 and 3 have more repeated numbers, and it is in the order of least repeated to most repeated.



# I would want to through the nums list and count each integer in the list -> [0,1,2,3,4,...] and every count of a duplicate will add to the k.
# k will look at one number each that has a duplicate and will print out which integer has a duplicate and then print out those two.
# that means there must be two loops, the outer loop that goes through the indexes, and another loop that goes through
# and counts and takes in how many numbers.


# we use a dictionary always to find duplicates or repeated integers.

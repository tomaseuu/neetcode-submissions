class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        holder = {}
        
        # Step 1: count how many times each number appears
        for i in range(len(nums)):
            if nums[i] not in holder:
                holder[nums[i]] = 1
            else:
                holder[nums[i]] += 1
        
        # Step 2: make buckets, one per possible frequency
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        
        # Step 3: place each number into the bucket matching its count
        for num in holder:
            c = holder[num]
            buckets[c].append(num)
        
        # Step 4: walk from highest frequency to lowest, collecting numbers
        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
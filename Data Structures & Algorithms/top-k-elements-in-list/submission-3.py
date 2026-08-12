class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        # build freq as a list of empty lists, one per possible count
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])

        # count occurrences of each number
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1

        # place each number into freq at the index matching its count
        for n, c in count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
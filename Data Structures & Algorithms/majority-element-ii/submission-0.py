class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for x in nums:
            count[x] += 1

            if len(count) > 2:
                keysToRemove = []
                for k, v in count.items():
                    count[k] -= 1
                    if count[k] == 0:
                        keysToRemove.append(k)

                for x in keysToRemove:
                    del count[x]
                
                

                

        res = []

        if not count:
            return []

        for n in count:
            if nums.count(n) > math.floor(len(nums) / 3):
                res.append(n)

        return res
        
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]


        for key, v in counts.items():
            buckets[v].append(key)


        res = []

        for x in range(len(buckets) - 1, -1, -1):
            if len(buckets[x]) != 0:
                for y in buckets[x]:
                    res.append(y)
                    if len(res) == k:
                        return res
            


        
        
    

     



        





        
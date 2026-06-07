class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for x in nums:
            dic[x] += 1

        count = []
        for x in dic.values():
            count.append(x)

        count = sorted(count)[-k:]

        return [k for k,v in dic.items() if v in count]
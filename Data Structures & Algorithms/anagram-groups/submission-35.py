class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for x in strs:
            counts = [0] * 26

            for y in x:
                counts[ord(y) % 26] += 1

            key = tuple(counts)

            if key not in dic:
                dic[key] = []

            dic[key].append(x)

        res = []
        for k, v in dic.items():
            res.append(v)
        return res

    



        
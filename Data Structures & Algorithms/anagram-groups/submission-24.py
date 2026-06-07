class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for x in strs:
            res = ' '.join(x for x in sorted(x))
            if res not in dict:
                dict[res] = []
            dict[res].append(x)

        return list(dict.values())
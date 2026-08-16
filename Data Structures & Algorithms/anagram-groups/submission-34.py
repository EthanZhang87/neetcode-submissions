class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for x in strs:
            count = [0] * 26
            for y in x:
                num = ord(y) - ord("a")
                count[num] += 1

            if tuple(count) not in dic:
                dic[tuple(count)] = []

            dic[tuple(count)].append(x)


        return list(dic.values())


    



        
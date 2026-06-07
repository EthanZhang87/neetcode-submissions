class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(list)
        for x in strs:
            arr = [0] * 26
            for i in range(len(x)):
                arr[ord(x[i].lower()) % 26] += 1
            
            dic[tuple(arr)].append(x)

        arr = []
        for k,v in dic.items():
            arr.append(v)

        return arr



        
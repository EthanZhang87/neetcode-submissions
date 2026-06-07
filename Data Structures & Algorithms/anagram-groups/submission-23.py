class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = [[strs[0]]]

        for x in range(1, len(strs)):
            for y in range(len(anagrams)):
                if sorted(strs[x]) == sorted(anagrams[y][0]):
                    anagrams[y].append(strs[x])
                else:
                    alreadyIn = False
                    for i in anagrams:
                        if sorted(strs[x]) == sorted(i[0]):
                            alreadyIn = True
                    if alreadyIn == False:
                        anagrams.append([strs[x]])


        return anagrams
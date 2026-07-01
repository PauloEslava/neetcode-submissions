class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = {}
        resultList = []

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            
            count = tuple(count)
            if count in anagramsDict:
                anagramsDict[count].append(word)
            else:
                anagramsDict[count] = [word]


        
        for key in anagramsDict:
            resultList.append(anagramsDict[key])

        return resultList
        


        
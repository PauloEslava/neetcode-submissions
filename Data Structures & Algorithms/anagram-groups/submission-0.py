class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        AnagramsDict = {}
        for word in strs:
            wordList = []
            for character in word:
                wordList.append(character)
            wordList.sort()
            sortedWord = "".join(wordList)

            if sortedWord not in AnagramsDict:
                AnagramsDict[sortedWord] = []
            AnagramsDict[sortedWord].append(word)
        solutionList = []
        for lista in AnagramsDict.values():
            solutionList.append(lista)
        return solutionList

        
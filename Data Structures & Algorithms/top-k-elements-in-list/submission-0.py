class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbersDict = {}
        for num in nums:
            if num not in numbersDict:
                numbersDict[num] = 1
            elif num in numbersDict:
                numbersDict[num] = numbersDict[num] + 1
        
        sorted_data_desc = dict(sorted(numbersDict.items(), key=lambda item: item[1], reverse = True))
        keyList = list(sorted_data_desc.keys())

        #"Give me elements from index 0 up to (but not including) index k."
        return keyList[:k]

        
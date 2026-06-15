class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        listLength = len(operations)
        for i in range(listLength):
            if operations[i] == "C":
                record.pop()
            elif operations[i] == "D":
                record.append(record[-1] * 2)
            elif operations[i] == "+":
                record.append(record[-1] + record[-2])
            else:
                num = int(operations[i])
                record.append(num)
        return sum(record)


            


        
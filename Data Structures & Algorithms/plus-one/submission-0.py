class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        for digit in digits:
            result = (result * 10) + digit

        result += 1

        digits = []

        while result > 0:
            digits.append(result % 10)
            result = result // 10

        digits.reverse()
        return digits

        
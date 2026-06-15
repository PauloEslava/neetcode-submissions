class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesDict = { ")" : "(", "]" : "[", "}" : "{" }
        for char in s:
            if (char == "(" or char == "[" or char == "{"):
                stack.append(char)
            else:
                if (not stack or stack[-1] != parenthesesDict[char]):
                    return False
                else:
                    stack.pop()
        
        if not stack:
            return True
        return False
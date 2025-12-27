class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def ispair(x, y) -> bool:
            if x == "(" and y == ")":
                return True
            elif x == "{" and y == "}":
                return True
            elif x == "[" and y == "]":
                return True
            else:
                return False

        for sym in s:
            if sym in "{([":
                stack.append(sym)
            else:
                if not stack:
                    return False
                var = stack.pop()
                if not ispair(var, sym):
                    return False
        return len(stack) == 0

    
    
    

        
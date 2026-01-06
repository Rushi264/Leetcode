class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Pass 1: remove invalid ')'
        res = []
        open_count = 0

        for ch in s:
            if ch == '(':
                open_count += 1
                res.append(ch)
            elif ch == ')':
                if open_count == 0:
                    continue  # skip invalid ')'
                open_count -= 1
                res.append(ch)
            else:
                res.append(ch)

        # Pass 2: remove extra '(' from the end (right to left)
        out = []
        for ch in reversed(res):
            if ch == '(' and open_count > 0:
                open_count -= 1  # skip this extra '('
                continue
            out.append(ch)

        return ''.join(reversed(out))

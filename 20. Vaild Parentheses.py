class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '[', '{']
        closing = [')', ']', '}']

        l = []
        for p in s:
            if p in opening:
                l.append(p)
            elif p in closing:
                pos = closing.index(p)
                if not l:
                    return False
                elif l.pop() != opening[pos]:
                    return False
        return l == []

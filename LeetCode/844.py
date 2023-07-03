class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        for c in s:
            if c == '#':
                if len(s_stack) > 0:
                    s_stack.pop()
                continue
            else:
                s_stack.append(c)

        t_stack = []
        for c in t:
            if c == '#':
                if len(t_stack) > 0:
                    t_stack.pop()
            else:
                t_stack.append(c)

        while len(s_stack) > 0 and len(t_stack) > 0:
            s_top = s_stack.pop()
            t_top = t_stack.pop()

            if s_top != t_top:
                return False

        return len(s_stack) == 0 and len(t_stack) == 0

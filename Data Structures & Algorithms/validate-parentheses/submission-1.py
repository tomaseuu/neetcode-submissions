class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

sol = Solution()

s = "[]"
s_1 = "([{}])"
s_2 = "[(])"

print(sol.isValid(s)) # True
print(sol.isValid(s_1)) # True
print(sol.isValid(s_2)) # False
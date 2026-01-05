class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == ".." and stack:
                stack.pop()
            elif part and part not in [".", ".."]:
                stack.append(part)

        return "/" + "/".join(stack)


print(Solution().simplifyPath("/home/"))
print(Solution().simplifyPath("/home//foo/"))
print(Solution().simplifyPath("/home/user/Documents/../Pictures"))
print(Solution().simplifyPath("/../"))
print(Solution().simplifyPath("/.../a/../b/c/../d/./"))
print(Solution().simplifyPath("/."))
print(Solution().simplifyPath("/./"))
print(Solution().simplifyPath("/.."))
print(Solution().simplifyPath("/..."))
print(Solution().simplifyPath("/abc/..."))
print(Solution().simplifyPath("/hello../world"))

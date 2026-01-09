class Solution:
    # todo in the future
    def decodeString(self, s: str) -> str:
        cursor = 0
        result = ""

        while cursor < len(s):
            str_digit = ""
            while s[cursor].isnumeric():
                str_digit += s[cursor]
                cursor += 1

            digit = int(str_digit)

            substr = ""
            if s[cursor] == "[":
                cursor += 1

                while s[cursor] != "]":
                    if s[cursor] == "[":
                        start = cursor
                        while s[cursor] != "]":
                            cursor += 1
                            substr += self.decodeString(s[start + 1 : cursor])
                    else:
                        substr += s[cursor]
                        cursor += 1

            cursor += 1
            result += digit * substr

        return result


# print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))

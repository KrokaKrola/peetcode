def lengthOfTheLongestSubstring(s: str) -> int:
    result = 0
    left = 0
    chars = set()

    for right in range(len(s)):
        curr_char = s[right]

        while curr_char in chars:
            chars.remove(s[left])
            left += 1

        chars.add(curr_char)
        result = max(result, len(chars))

    return result


print(lengthOfTheLongestSubstring("abcabcbb"), 3)
print(lengthOfTheLongestSubstring("bbbbb"), 1)
print(lengthOfTheLongestSubstring("pwwkew"), 3)
print(lengthOfTheLongestSubstring(" "), 1)
print(lengthOfTheLongestSubstring("b"), 1)
print(lengthOfTheLongestSubstring("ba"), 2)
print(lengthOfTheLongestSubstring("aab"), 2)
print(lengthOfTheLongestSubstring("dvdf"), 3)
print(lengthOfTheLongestSubstring("qrsvbspk"), 5)

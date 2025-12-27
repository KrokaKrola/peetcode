def characterReplacement(s: str, k: int) -> int:
    result = 0
    left = 0
    chars_count = dict()

    for right in range(len(s)):
        char = s[right]

        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1

        max_count_char = max(chars_count, key=chars_count.get)
        window_size = right - left + 1
        replace_count = window_size - chars_count[max_count_char]

        if replace_count > k:
            l_char = s[left]
            chars_count[l_char] -= 1

            if chars_count[l_char] == 0:
                del chars_count[l_char]

            left += 1
        else:
            result = max(window_size, result)

    return result


print(characterReplacement("ABAB", 2), 4)
print(characterReplacement("AABABBA", 1), 4)
print(characterReplacement("AABABBA", 0), 2)

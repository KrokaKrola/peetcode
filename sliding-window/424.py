def characterReplacemenet(s: str, k: int) -> int:
    result = 0
    char_count = dict()
    left = 0

    for right in range(len(s)):
        curr_char = s[right]

        if curr_char in char_count:
            char_count[curr_char] += 1
        else:
            char_count[curr_char] = 1

        most_frequent_char = max(char_count, key=char_count.get)
        window_size = right - left + 1
        chars_to_replace = window_size - char_count[most_frequent_char]

        if chars_to_replace > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
        else:
            result = max(result, window_size)

    return result


print(characterReplacemenet("ABAB", 2), 4)
print(characterReplacemenet("AABABBA", 1), 4)
print(characterReplacemenet("AABABBA", 0), 2)

def checkInclusion(str1: str, str2: str) -> bool:
    str1_dict = dict()
    str1_len = len(str1)

    for el in str1:
        if el in str1_dict:
            str1_dict[el] += 1
        else:
            str1_dict[el] = 1

    left = 0

    active_dict = dict()

    for right in range(len(str2)):
        curr_char = str2[right]

        if curr_char in active_dict:
            active_dict[curr_char] += 1
        else:
            active_dict[curr_char] = 1

        curr_window_size = right - left + 1

        if curr_window_size > str1_len:
            l_char = str2[left]

            active_dict[l_char] -= 1
            if active_dict[l_char] == 0:
                del active_dict[l_char]

            left += 1

        if active_dict == str1_dict:
            return True

    return False


print(checkInclusion("ab", "eidbaooo"), True)
print(checkInclusion("ab", "eidboaoo"), False)
print(checkInclusion("adc", "dcda"), True)

def checkInclusion(str1: str, str2: str) -> bool:
    str1_dict = dict()
    window_size = len(str1)

    for el in str1:
        if el in str1_dict:
            str1_dict[el] += 1
        else:
            str1_dict[el] = 1

    left = 0

    str2_dict = dict()

    for right in range(len(str2)):
        right_char = str2[right]

        if right_char in str2_dict:
            str2_dict[right_char] += 1
        else:
            str2_dict[right_char] = 1

        if right - left + 1 > window_size:
            left_char = str2[left]
            str2_dict[left_char] -= 1
            left += 1

            if str2_dict[left_char] == 0:
                del str2_dict[left_char]

        if str1_dict == str2_dict:
            return True

    return False


def checkInclusion2(str1: str, str2: str) -> bool:
    if len(str1) > len(str2):
        return False

    str1_dict = dict()

    for el in str1:
        if el in str1_dict:
            str1_dict[el] += 1
        else:
            str1_dict[el] = 1

    str2_dict = {char: 0 for char in str1_dict}
    matches = 0
    window_size = len(str1)
    left = 0

    for right in range(len(str2)):
        right_char = str2[right]

        if right_char in str1_dict:
            if str2_dict[right_char] == str1_dict[right_char]:
                matches -= 1

            str2_dict[right_char] += 1

            if str2_dict[right_char] == str1_dict[right_char]:
                matches += 1

        if right - left + 1 > window_size:
            left_char = str2[left]

            if left_char in str1_dict:
                if str2_dict[left_char] == str1_dict[left_char]:
                    matches -= 1

                str2_dict[left_char] -= 1

                if str2_dict[left_char] == str1_dict[left_char]:
                    matches += 1

            left += 1

        if matches == len(str1_dict):
            return True

    return False


print(checkInclusion2("ab", "eidbaooo"), True)
print(checkInclusion2("ab", "eidboaoo"), False)
print(checkInclusion2("adc", "dcda"), True)

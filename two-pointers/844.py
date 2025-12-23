def backspaceCompare(str1: str, str2: str) -> bool:
    p1 = len(str1) - 1
    p2 = len(str2) - 1

    skip_count_str1 = 0
    skip_count_str2 = 0

    while p1 >= 0 or p2 >= 0:
        while p1 >= 0:
            if str1[p1] == "#":
                skip_count_str1 += 1
                p1 -= 1
            elif skip_count_str1 > 0:
                skip_count_str1 -= 1
                p1 -= 1
            else:
                break

        while p2 >= 0:
            if str2[p2] == "#":
                skip_count_str2 += 1
                p2 -= 1
            elif skip_count_str2 > 0:
                skip_count_str2 -= 1
                p2 -= 1
            else:
                break

        if p1 >= 0 and p2 >= 0 and str1[p1] != str2[p2]:
            return False

        if (p1 >= 0) != (p2 >= 0):
            return False

        p1 -= 1
        p2 -= 1

    return True


# print(backspaceCompare("ab#c", "ad#c"))
# print(backspaceCompare("ab##", "c#d#"))
# print(backspaceCompare("a#c", "b"))
print(backspaceCompare("a", "aa#a"))

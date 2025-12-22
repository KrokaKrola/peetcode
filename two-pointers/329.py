def isSubsequence(s: str, t: str) -> bool:
    sub_str_pointer = 0

    for og_str_char in t:
        if sub_str_pointer >= len(s):
            break
        if s[sub_str_pointer] == og_str_char:
            sub_str_pointer += 1

    return sub_str_pointer == len(s)


print(isSubsequence("abc", "ahbgdf"))
print(isSubsequence("", "ahbgdf"))
print(isSubsequence("b", "abc"))

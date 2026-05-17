def isPalindrome(s: str) -> bool:
    new_str = []

    for el in s:
        if el.isalnum():
            new_str.append(el.lower())

    right = len(new_str) - 1

    for i in range(len(new_str) // 2):
        if new_str[i] != new_str[right - i]:
            return False

    return True


print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("0P"), "false")
print(isPalindrome("a"), "true")

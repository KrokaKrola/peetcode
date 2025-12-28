def isPalindrome(s: str) -> bool:
    s = "".join(char for char in s.lower() if char.isalnum())

    right = len(s) - 1

    for left in range(len(s) // 2):
        if s[left] != s[right - left]:
            return False

    return True


print(isPalindrome("race a car"), False)
print(isPalindrome(" "), True)
print(isPalindrome("A man, a plan, a canal: Panama"), True)
print(isPalindrome("0P"), False)
print(isPalindrome("a"), True)

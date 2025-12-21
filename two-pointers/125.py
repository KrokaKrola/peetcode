def isPalindrome(s: str) -> bool:
    sanitized_string = "".join(char for char in s.lower() if char.isalnum())

    is_palindrome = True

    if len(sanitized_string) == 0:
        return is_palindrome

    lp = 0
    rp = len(sanitized_string) - 1

    while lp < rp:
        if sanitized_string[lp] != sanitized_string[rp]:
            is_palindrome = False
            break

        lp += 1
        rp -= 1

    return is_palindrome


# print(isPalindrome("race a car"))
# print(isPalindrome(" "))
# print(isPalindrome("A man, a plan, a canal: Panama"))
# print(isPalindrome("0P"), "false")
# print(isPalindrome("a"), "true")

multipliers = [3, 7, 1, 3, 7, 1, 3, 7]


def check_number(number: str) -> bool:
    if len(number) != 9:
        return False

    counter = 0

    for i in range(len(number) - 1):
        counter += int(number[i]) * multipliers[i]

    if (int(number[-1]) + counter) % 10 != 0:
        return False

    return True


print(check_number("012749138"))  # False
print(check_number("012749139"))  # True
print(check_number("013333337"))  # True
print(check_number("012345678"))  # False
print(check_number("012344550"))  # True
print(check_number("1337"))  # False
print(check_number("0127491390"))  # False

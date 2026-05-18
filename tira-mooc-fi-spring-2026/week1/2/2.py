def check_year(input: int) -> bool:
    return pow(input // 100 + input % 100, 2) == input


print(check_year(1995))  # False
print(check_year(2024))  # False
print(check_year(2025))  # True
print(check_year(2026))  # False
print(check_year(3025))  # True
print(check_year(5555))  # False

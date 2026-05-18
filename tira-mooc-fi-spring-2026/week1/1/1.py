def min_count(product_count: int, box_size: int) -> int:
    result = 0

    while product_count > 0:
        product_count -= box_size
        result += 1

    return result


print(min_count(10, 3), "==", 4)
print(min_count(10, 4), "==", 3)
print(min_count(100, 1), "==", 100)
print(min_count(100, 100), "==", 1)
print(min_count(100, 99), "==", 2)
print(min_count(5, 5), "==", 1)
print(min_count(5, 6), "==", 1)

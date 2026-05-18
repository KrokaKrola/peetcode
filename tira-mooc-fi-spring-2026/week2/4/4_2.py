def find_order(n):
    results = []
    circle = []

    for i in range(n):
        circle.append(i + 1)

    offset = 0

    while circle:
        next_circle = []

        for i in range(len(circle)):
            if (i + offset) % 2 == 0:
                next_circle.append(circle[i])
            else:
                results.append(circle[i])

        if len(circle) % 2 == 1:
            offset = (offset + 1) % 2

        circle = next_circle

    return results


# print(find_order(1))  # [1]
# print(find_order(2))  # [2, 1]
# print(find_order(3))  # [2, 1, 3]
print(find_order(6))  # 1 2 3 4 5 6 -> [2, 4, 6] -> [2, 4, 6, 3, 1, 5]
print(
    find_order(7)
)  # 1 2 3 4 5 6 7 -> [2, 4, 6] -> [2, 4, 6, 1, 5] -> [2, 4, 6, 1, 5, 3, 7]

# order = find_order(10**5)
# print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]

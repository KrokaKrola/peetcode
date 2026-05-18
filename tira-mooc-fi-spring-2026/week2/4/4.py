def find_order(n):
    results = []
    tmp = list(range(1, n + 1))
    offset = 0

    while tmp:
        next_round = []
        for i in range(len(tmp)):
            if (i + offset) % 2 == 0:
                next_round.append(tmp[i])
            else:
                results.append(tmp[i])

        if len(tmp) % 2 == 1:
            offset = (offset + 1) % 2

        tmp = next_round

    return results

# print(find_order(1)) # [1]
# print(find_order(2)) # [2, 1]
# print(find_order(3)) # [2, 1, 3]
print(find_order(6)) # [2, 4, 6, 1, 5, 3, 7]
print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

# order = find_order(10**5)
# print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]
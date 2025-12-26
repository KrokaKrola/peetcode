def bestClosingTime(customers: str) -> int:
    result = 0
    prev_penalty = float("inf")
    prefix_N = [0]
    suffix_Y = [0]

    n_count = 0
    for h in range(len(customers)):
        if customers[h] == "N":
            n_count += 1

        prefix_N.append(n_count)

    y_count = 0
    for h in range(len(customers) - 1, -1, -1):
        if customers[h] == "Y":
            y_count += 1

        suffix_Y.append(y_count)

    suffix_Y = suffix_Y[::-1]

    for h in range(len(customers) + 1):
        penalty = prefix_N[h] + suffix_Y[h]

        if penalty < prev_penalty:
            prev_penalty = penalty
            result = h

    return result


print(bestClosingTime("YYNY"), 2)
print(bestClosingTime("NNNNN"), 0)
print(bestClosingTime("YYYY"), 4)

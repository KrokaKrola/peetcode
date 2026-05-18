def find_segments(data: str) -> list[tuple[int, str]]:
    result: list[tuple[int, str]] = []

    tp = bp = 0

    while tp < len(data):
        if data[tp] != data[bp]:
            result.append((tp - bp, data[bp]))
            bp = tp

        tp += 1

    if bp != tp - 1:
        result.append(((tp - bp), data[tp - 1]))

    return result


print(find_segments("aaabbccdddd"))
# [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
# [(20, 'a')]

print(find_segments("abcabc"))
# [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

print(find_segments("kissa"))
# [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]

def maxArea(height: list[int]) -> int:
    max_value = 0

    n = len(height)
    lp = 0
    rp = n - 1

    while lp < rp:
        curr_area = min(height[lp], height[rp]) * (rp - lp)

        max_value = max(curr_area, max_value)

        if height[lp] > height[rp]:
            rp -= 1
        else:
            lp += 1

    return max_value


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))

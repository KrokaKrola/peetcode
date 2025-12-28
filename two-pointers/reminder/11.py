def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    result = 0

    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)

        result = max(result, curr_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return result


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))

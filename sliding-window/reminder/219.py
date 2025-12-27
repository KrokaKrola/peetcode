def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    left = 0
    result = False
    unique_numbers = set()

    for right in range(len(nums)):
        curr_num = nums[right]

        if curr_num not in unique_numbers:
            unique_numbers.add(curr_num)
        else:
            result = True
            break

        window_size = right - left + 1

        if window_size > k:
            l_num = nums[left]
            unique_numbers.remove(l_num)
            left += 1

    return result


print(containsNearbyDuplicate([1, 2, 3, 1], 3), True)
print(containsNearbyDuplicate([1, 0, 1, 1], 1), True)
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2), False)
print(containsNearbyDuplicate([1, 2, 1], 0), False)
print(containsNearbyDuplicate([0, 1, 2, 3, 2, 5], 3), True)
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 1, 3], 1), False)
print(containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 3), True)

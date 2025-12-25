def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    left = 0
    window = set()

    for right in range(len(nums)):
        if nums[right] not in window:
            window.add(nums[right])
        else:
            return True

        if right - left == k:
            window.remove(nums[left])
            left += 1

    return False


print(containsNearbyDuplicate([1, 2, 3, 1], 3), True)
print(containsNearbyDuplicate([1, 0, 1, 1], 1), True)
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2), False)
print(containsNearbyDuplicate([1, 2, 1], 0), False)
print(containsNearbyDuplicate([0, 1, 2, 3, 2, 5], 3), True)
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 1, 3], 1), False)
print(containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 3), True)

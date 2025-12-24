def longestSubarray(nums: list[int]) -> int:
    result = 0
    left = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        if zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        result = max(result, right - left)

    return result


def longestSubarray2(nums: list[int]) -> int:
    """
    Non-shrinking sliding window approach.
    
    Key insight: We only care about the LARGEST valid window size, not maintaining
    a valid window at all times. So instead of shrinking the window when invalid
    (using `while`), we just slide it forward (using `if`).
    
    How it works:
    1. GROWING phase: Window expands while valid (zero_count <= 1)
    2. SLIDING phase: Once we hit an invalid state (zero_count > 1), we move
       `left` by 1 for every `right` move, keeping window size constant
    
    The window acts like a "high water mark" — it never shrinks, only grows or
    slides. At the end, `right - left` gives the largest valid window we ever had.
    
    Why `if` instead of `while`:
    - `while`: shrinks window back to valid state (tracks current valid window)
    - `if`: slides window forward by 1 (preserves maximum window size)
    
    Example: [1, 1, 0, 0, 0]
    - right=0,1,2: window grows to size 2 (valid, one zero allowed)
    - right=3,4: window slides (left moves too), size stays 2
    - Final: right=4, left=2, answer = 4 - 2 = 2 ✓
    """
    left = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        if zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

    return right - left


print(longestSubarray([1, 1, 0, 1]), 3)
print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]), 5)
print(longestSubarray([1, 1, 1]), 2)
print(longestSubarray([1]), 0)
print(longestSubarray([0]), 0)
print(longestSubarray([0, 0, 0]), 0)

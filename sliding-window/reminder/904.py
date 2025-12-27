def totalFruit(fruits: list[int]) -> int:
    result = 0
    left = 0
    fruits_count = dict()

    for right in range(len(fruits)):
        fruit = fruits[right]

        if fruit in fruits_count:
            fruits_count[fruit] += 1
        else:
            fruits_count[fruit] = 1

        while len(fruits_count) > 2:
            l_fruit = fruits[left]
            fruits_count[l_fruit] -= 1
            if fruits_count[l_fruit] == 0:
                del fruits_count[l_fruit]
            left += 1

        result = max(result, right - left + 1)

    return result


print(totalFruit([1, 2, 1]), 3)
print(totalFruit([0, 1, 2, 2]), 3)
print(totalFruit([1, 2, 3, 2, 2]), 4)
print(totalFruit([0]), 1)
print(totalFruit([0, 1]), 2)
print(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]), 5)

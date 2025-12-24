def totalFruit(fruits: list[int]) -> int:
    max_number = 0
    left = 0

    fruits_dict: dict[int, int] = dict({})

    for right in range(len(fruits)):
        fruit_id = fruits[right]

        if fruit_id in fruits_dict:
            fruits_dict[fruit_id] += 1
        else:
            fruits_dict[fruit_id] = 1

        while len(fruits_dict) > 2:
            left_fruit_id = fruits[left]
            left_fruit = fruits_dict[left_fruit_id] - 1

            if left_fruit == 0:
                del fruits_dict[left_fruit_id]
            else:
                fruits_dict[left_fruit_id] = left_fruit
            left += 1

        curr_fruits_count = right - left + 1
        max_number = max(max_number, curr_fruits_count)

    return max_number


print(totalFruit([1, 2, 1]), 3)
print(totalFruit([0, 1, 2, 2]), 3)
print(totalFruit([1, 2, 3, 2, 2]), 4)
print(totalFruit([0]), 1)
print(totalFruit([0, 1]), 2)
print(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]), 5)

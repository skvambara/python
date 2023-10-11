"""
Given an array of numbers, rearrange them in-place so that even numbers appear before odd ones.
The order within the group of even numbers does not matter; same with odd numbers.
So the following are also correct outputs: [4, 2, 1, 3], [2, 4, 1, 3], [2, 4, 3, 1].
"""
import random


def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # pivot = numbers[0]
    left = 0
    right = len(numbers)-1
    while right > left:
        print(left, right)
        if numbers[right] % 2 == 0:
            if numbers[left] % 2 != 0:
                numbers[right], numbers[left] = numbers[left], numbers[right]
            left += 1
        else:
            right -= 1
        print(numbers)
    return numbers


inputlist = random.sample(range(10, 100), 10)
# inputlist = [1, 2, 3, 4]
print("Original list:", inputlist)
segregate_evens_and_odds(inputlist)
print("Sorted list:", inputlist)
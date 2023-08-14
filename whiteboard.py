# Problem 1:
# Two Sum (Easiest Version)
# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2,  as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [0,2]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 0, index2 = 2. We return [0, 2].
# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [0,1]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 0, index2 = 1. We return [0, 1].

def solution(numbers, target):
    
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


def solution(arr, target):
    di = {}
    for num in range(len(arr)): # O(n)
        new_target = target - arr[num]
        if new_target in di:
            return [di[new_target], num]
        di[arr[num]] = num



def solution(numbers, target):
    beg = 0
    end = len(numbers) - 1

    while beg < end:
        sum = numbers[beg] + numbers[end]
        if sum == target:
            return [beg, end]
        elif sum < target:
            beg += 1
        else:
            end -= 1
    
    return "No Solution"
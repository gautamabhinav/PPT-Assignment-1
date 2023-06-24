def twoSum(nums, target):
    numMap = {}  # Dictionary to store the number and its index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in numMap:
            # Found the complement, return the indices
            return [numMap[complement], i]
        numMap[num] = i  # Store the number and its index

    # No solution found, return an empty list
    return []

nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)

if result:
    print([result[0],result[1]])
    # print("Values:", nums[result[0]], ",", nums[result[1]])
else:
    print("No solution found.")

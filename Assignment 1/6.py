def containsDuplicate(nums):
    unique_set = set()

    for num in nums:
        if num in unique_set:
            return True
        unique_set.add(num)

    return False

nums = [1, 2, 3, 1]
result = containsDuplicate(nums)

print("Output:", result)

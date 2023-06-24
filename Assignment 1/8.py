def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate_num = -1
    missing_num = -1

    # Find the duplicate number and store it
    for num in nums:
        if num in num_set:
            duplicate_num = num
        else:
            num_set.add(num)

    # Find the missing number by comparing the set with the range from 1 to n
    for i in range(1, n+1):
        if i not in num_set:
            missing_num = i
            break

    return [duplicate_num, missing_num]

nums = [1, 2, 2, 4]
result = findErrorNums(nums)

print("Output:", result)

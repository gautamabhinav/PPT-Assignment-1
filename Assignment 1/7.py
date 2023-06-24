def moveZeroes(nums):
    zero_pointer = 0  # Pointer to track the position to place the next non-zero element

    # Iterate through the array
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap the non-zero element with the element at zero_pointer
            nums[i], nums[zero_pointer] = nums[zero_pointer], nums[i]
            zero_pointer += 1

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)

print("Output:", nums)

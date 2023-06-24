def removeElement(nums, val):
    left = 0  # Pointer to track the current position
    right = len(nums) - 1  # Pointer to track the end position

    while left <= right:
        if nums[left] == val:
            nums[left] = nums[right]  # Replace with the element at the end
            right -= 1  # Decrease the end pointer
        else:
            left += 1  # Move the current pointer

    return left  # Return the number of elements not equal to val

nums = [3, 2, 2, 3]
val = 3

k = removeElement(nums, val)

print("Output:", k)
print("nums:", nums[:k])

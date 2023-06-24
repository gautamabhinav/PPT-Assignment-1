def plusOne(digits):
    carry = 1  # Initialize carry to 1 since we're incrementing by one
    result = []  # Initialize an empty list to store the resulting digits

    for i in range(len(digits)-1, -1, -1):
        sum = digits[i] + carry
        result.insert(0, sum % 10)  # Insert the least significant digit at the beginning of the result
        carry = sum // 10

    if carry:
        result.insert(0, carry)  # If there's a remaining carry, add it to the result

    return result

digits = [1, 2, 3]
result = plusOne(digits)

print("Output:", result)

def missingNumber(nums):
    n = len(nums)
    # Calculate the expected sum of numbers from 0 to n
    expected_sum = n * (n + 1) // 2
    # Calculate the actual sum of the numbers in the list
    actual_sum = sum(nums)
    # The difference is the missing number
    return expected_sum - actual_sum

# Example usage
nums = [3, 0, 1]
print(missingNumber(nums))  # Output: 2



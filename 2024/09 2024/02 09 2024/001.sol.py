def three_sum(nums):
    result = set()
    
    for i in range(len(nums)):
        seen = set()
        for j in range(i + 1, len(nums)):
            complement = -nums[i] - nums[j] 
            if complement in seen:
                result.add(tuple(sorted([nums[i], nums[j], complement])))
            seen.add(nums[j])
    
    return list(result)

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
output = three_sum(nums)
print(output)  # Output: [(-1, 0, 1), (-1, -1, 2)]

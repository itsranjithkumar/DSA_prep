def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the first string in the array as the initial prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the list
    for s in strs[1:]:
        while not s.startswith(prefix):
            # Shorten the prefix by one character
            prefix = prefix[:-1]
            # If the prefix becomes empty, return an empty string
            print(not prefix,prefix)
            if not prefix:
                return ""
    
    return prefix

# Example usage
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))  # Output: "fl"


"""------------------------------------------------------------------------"""

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the first string in the array as the initial prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the list
    for s in strs[1:]:
        while not s.startswith(prefix):
            # Shorten the prefix by one character
            prefix = prefix[:-1]
            # If the prefix becomes empty, return an empty string
            if not prefix:
                return ""
    
    return prefix

# Example usage
strs = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs))  # Output: ""

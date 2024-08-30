s = "][]"
def isValid( s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping and stack:
            top_element = stack.pop()
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
        
print(isValid(s))



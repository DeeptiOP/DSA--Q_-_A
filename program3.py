def is_balanced(s):
    count = 0

    for ch in s:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1

        # If at any point count becomes negative → unbalanced
        if count < 0:
            return False

    # Balanced only if count ends at 0
    return count == 0

print(is_balanced("(()())")) 
print(is_balanced("(()"))     
print(is_balanced(""))      
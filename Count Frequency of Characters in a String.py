def first_non_repeating_char(s):
    count = {}

    # Count each character
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    # Find the first character with count = 1
    for ch in s:
        if count[ch] == 1:
            return ch

    return None  # if no non-repeating character found

print(first_non_repeating_char("aabbcde"))  
print(first_non_repeating_char("aabb"))      

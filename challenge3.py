def solve(s):
    vowels = "aeiou"
    # the string vowel contains all the lowercase vowels ,each character in the string represents a vowel 
    # this is to check if a given character in the input "s" is a vowel or not 
    consonant_values = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1) if chr(i) not in vowels}
    # for 'for i ... ' it iterates over all the letters from A to Z
    # the chr converts the current i into a corresponding character 
    
    max_consonant_value = 0
    # This variable is used to store the maximum value of consonant substrings encountered so far in the input string. It starts with a value of 0 and will be updated as the program processes the string.
    current_consonant_value = 0
    # This variable is used to keep track of the value of the current consecutive consonant substring being processed in the input string.
    
    for char in s:
        if char in consonant_values:
            current_consonant_value += consonant_values[char]
            max_consonant_value = max(max_consonant_value, current_consonant_value)
        else:
            current_consonant_value = 0
    
    return max_consonant_value
print(solve("strength"))
print(solve("zodiacs"))

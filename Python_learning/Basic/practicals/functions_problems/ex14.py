import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return set(s.lower()) >= alphabet  # Checks if all letters are in the string

# Example
text = "The quick brown fox jumps over the lazy dog"
print("Pangram:", is_pangram(text))  # Output: True

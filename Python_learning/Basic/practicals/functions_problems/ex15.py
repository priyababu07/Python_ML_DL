def sort_hyphen_words(s):
    words = s.split('-')
    words.sort()
    return '-'.join(words)

# Example
input_str = "green-red-yellow-black-white"
result = sort_hyphen_words(input_str)
print("Sorted:", result)  # Output: black-green-red-white-yellow

def sample_function():
    a = 10
    b = 20
    c = 30
    result = a + b + c
    return result

# Count local variables
print("Number of local variables:", sample_function.__code__.co_nlocals)

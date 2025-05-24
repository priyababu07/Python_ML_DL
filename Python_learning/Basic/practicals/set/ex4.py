my_set = {1, 2, 3, 4}
my_set.remove(2)    # Raises error if element not found
my_set.discard(5)   # No error if element not found
print("After removals:", my_set)

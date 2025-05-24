def outer_function():
    print("Outer function")

    def inner_function():
        print("Inner function")

    inner_function()  # Call inner function

outer_function()

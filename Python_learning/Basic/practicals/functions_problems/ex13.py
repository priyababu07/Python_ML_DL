def pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]  # Every row starts with 1
        if triangle:
            last_row = triangle[-1]
            for j in range(1, i):
                # Add the two numbers above
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)  # End each row with 1 if i > 0
        triangle.append(row)

    # Print the triangle
    for row in triangle:
        print(row)
pascals_triangle(5)

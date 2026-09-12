# use of filter(), map(), reduce() tool 


from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
# Step 1: filter even numbers
evens = filter(lambda x: x % 2 == 0, numbers)
# Step 2: square them
squares = map(lambda x: x**2, evens)
# Step 3: sum them
result = reduce(lambda x, y: x + y, squares)

print(result)  # 56 (2² + 4² + 6²)



#  **Key takeaway:**

# Use map() when you want to transform.

# Use filter() when you want to select.

# Use reduce() when you want to combine.
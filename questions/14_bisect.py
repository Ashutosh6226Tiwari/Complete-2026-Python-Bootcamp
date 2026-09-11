import bisect

numbers = [2, 4, 6, 8, 10]
target = 6

# bisect_left finds the position where 'target' should be inserted
# to keep the list sorted (first occurrence if duplicates exist).
index = bisect.bisect_left(numbers, target)

# Safety check: make sure index is within the list length.
# If target is bigger than all elements, index == len(numbers),
# and accessing numbers[index] would cause an error.
if index < len(numbers) and numbers[index] == target:
    print("Found at index", index)   # target exists in the list
else:
    print("Not found")               # target not present

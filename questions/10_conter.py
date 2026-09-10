from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4]

# Counter builds a dictionary-like object with counts of each element
freq = Counter(numbers)

print(freq)                       # shows counts of all numbers
print(f"freq of 4 is {freq[4]}")  # prints how many times 4 appears

# most_common() returns all elements sorted by frequency (highest first)
print(freq.most_common())         # [(3, 3), (2, 2), (1, 1), (4, 1)]

# most_common(1) returns only the single most frequent element
print(freq.most_common(1))        # [(3, 3)]

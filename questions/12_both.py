
#  Final Challenge using both Counter and defaultdict:

from collections import Counter, defaultdict

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Step 1: Use Counter to count frequencies
freq = Counter(words)
print(freq)   # shows counts of all words

# Step 2: Find the most common word
print(freq.most_common(1)[0])   # prints the top word and its count

# (Optional) Step 3: Show how defaultdict could also group words
group = defaultdict(int)
for w in words:
    group[w] += 1
print(group)   # works like Counter but built manually

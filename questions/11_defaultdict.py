# traditionally we use this method 

numbers=(2,4,5,6,6,43,2,1,5,6,)
freq={}
for num in numbers:
    freq[num]=freq.get(num,0)+1
print(freq)

# now we use "defaultdict"
from collections import defaultdict

d=defaultdict(int)
d["a"]+=1
print(d)
# defaultdict(<class 'int'>, {'a': 1})




from collections import defaultdict

pairs = [
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("color", "red"),
    ("color", "blue")
]
groups = defaultdict(list)

for key, value in pairs:
    groups[key].append(value)

print(groups)

# defaultdict(<class 'list'>,
# {'fruit': ['apple', 'banana'], 'color': ['red', 'blue']})
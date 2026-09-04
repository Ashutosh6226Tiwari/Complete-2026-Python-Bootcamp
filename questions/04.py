# find the first number who appear once

numbers = [1, 2, 3, 2, 4, 1, 5, 2, 3]
freq={}
for num in numbers :
    freq[num]=freq.get(num,0)+1
    if freq[num] > 1 :
        print(num)
        break

# find the first number who appear 2 times

numbers = [1, 2, 3, 2, 4, 1, 5, 2, 3]
freq={}
for num in numbers:
    freq[num]=freq.get(num,0)+1
    if freq[num]==2:
        print (num)
        break 
    
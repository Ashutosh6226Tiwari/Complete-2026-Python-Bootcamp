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

<------------------------------------------->
# simple search in list using bisect module 

import bisect 
def search (numbers,target)
    if index<len(numbers)and numbers[index]==target:
        return index
    else:
        return -1
    
numbers =[1,4,6,5,3,1,2]
target=6
index=bisect.bisect_left(numbers, target)
print(search (numbers,target))


<--------------------------------------------->

import bisect
def occured(numbers, target):
    left=bisect.bisect_left(numbers, target)
    right=bisect.bisect_right(numbers, target)
    return right- left 

numbers = [1, 2, 4, 4, 4, 7, 9]
target=int(input("enter the targated number :"))
n=occured(numbers, target)
print(f"target is {target} and occurance is {n}")
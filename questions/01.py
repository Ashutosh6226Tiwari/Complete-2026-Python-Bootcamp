# finding the number which has higest frequency

numbers = [4, 2, 4, 3, 2, 4, 5, 2, 2]
freq={}
for num in numbers :
    freq[num]=freq.get(num,0)+1
print (freq)    

most_freq= None
higest_freq=0

for num , count in freq.items():
    if count >higest_freq :
        higest_freq= count
        most_freq=num
        
print (f"the num is {most_freq} and freequency is {higest_freq}")        
        
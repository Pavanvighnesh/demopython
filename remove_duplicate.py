numbers=[4,7,2,7,1,5,4,2]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
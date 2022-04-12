numbers= [4, 5,9,4,12,62,67,8]
max = numbers[0] #to check the list of numbers from index 0 and to store in max till it find other greater no.
for number in numbers:
    if number > max:
        max = number
print(max)
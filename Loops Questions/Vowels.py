# Count vowels in a string
vowels = 'aeiou'
str = input("Enter any string = ")
count = 0

for char in str:
    if char in vowels:
        count+=1

print(count)
# Print Even numbers
# for i in range(1,100):
#     if i%2 == 0:
#         print("The Even number is : = ",i)


# for i in range(1,100):
#     if i%3 == 0:
#         print(i)

# Counts of Even and odd 
count = 0
oddCount = 0
for i in range(1,100):
    if i%2 == 0:
        count = count+1
    else:
        oddCount = oddCount+1

print(count)
print(oddCount)
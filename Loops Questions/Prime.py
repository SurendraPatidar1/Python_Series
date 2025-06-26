# num = int(input("Enter any Number : "))

# if num > 1:
#     for i in range(2,num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#             print(num, "is a prime number.")
# else:
#     print(num,"is not a prime or positive number")


# Print all prime numbers between 1 to 100
for num in range(2,101):
    is_prime = True
    for i in range (2,int(num**0.5)+1):
        if num%i == 0:
            is_prime = False
            break
    if is_prime:
        print(num,end=" ")
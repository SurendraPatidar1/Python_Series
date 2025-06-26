def value():
    lst = []
    user = int(input("Enter how many numbers of list you want = "))
    for i in range(user):
        add = int(input("Enter number : "))
        lst.append(add)

    print (lst)
    
    maximum = max(lst)
    print("The Maximum number is : ", maximum)
    
    minimum = min(lst)
    print("The minimum number is : ", minimum)
    
value()
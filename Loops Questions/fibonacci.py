# Fibonacci (sum of two preceding ones) -- 0 1 1 2 3 5 8 13 21 34 55 89 144

a = 0
b = 1
print(a,b,end=" ")
for _ in range(10):
    c = a + b 
    print(c,end=" ")
    a,b=b,c

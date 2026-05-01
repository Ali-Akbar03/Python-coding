n = int(input("Enter a positive number "))
fact = 1

if n<=0 :
    print(f"Factorial isn't possible for{n}")
else:
    for x in range(1,n+1,1):
        fact = fact * x

print(f"Factorial of {n} is = ",fact)
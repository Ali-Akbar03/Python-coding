n = 370
temp = n
sum = 0

while n!=0:
    rem = n%10
    n= n//10
    sum = sum+(rem**3)

if sum == temp:
    print(f"{temp} is an Armstrong number")
else:
    print(f"{temp} is not an Armstrong number")
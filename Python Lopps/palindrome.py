n = 121
count = 0
temp = n

while n!=0:
    rem= n%10
    count = count * 10 + rem
    n = n//10


if count == temp:
    print(f"{temp} is a plainfrome number")
else :
    print("Not a palindrome number")
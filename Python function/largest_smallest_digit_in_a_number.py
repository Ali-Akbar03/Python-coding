n=75869

max = 7
min = 9

while n!=0:
    rem = n%10
    n = n//10
    if rem>max :
        max = rem
    if rem<min:
        min = rem


print("the largest digit in the number is ",max)
print("the smallest digit in the number is ",min)
a=int(input("Enter the value of a = "))
b=int(input("Enter the value of b = "))
c=int(input("Enter the value of c = ")) 

if a>b and a>c :
    print(f"a = {a} is the largest number")
elif b>a and b>c:
    print(f"b = {b} is the largest number ")
else:
    print(f"c = {c} is the largest number")

print("=============================It can be done in just only 1 statement ====================================")
print("the largest number is",max(a,b,c))
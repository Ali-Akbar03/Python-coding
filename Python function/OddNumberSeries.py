n = int(input("Enter the value of n = "))
sum= 0

if n%2 != 0:
    for x in range(1,n+1,2):
        sum=sum+x
    print(sum)
else:
    print("Sorry! the program calculate's the series of ODD numbers.Try again.")




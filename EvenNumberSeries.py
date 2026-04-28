n = int(input("Enter the value of n(The last even number of the series) = "))

sum= 0

if n%2 == 0:
    for x in range(2,n+1,2):
        sum=sum+x
    print(sum)
else:
    print("Sorry! the program calculate's the series of even numbers.Try again.")




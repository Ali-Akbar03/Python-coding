def summation(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

summation(10,20)
summation(10,20,30)
summation(10,20,30,40)
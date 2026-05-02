def add(x,y):
    sum = x+y
    return sum
result = add(10,20)
print(result)
print(result * 2)

def large(a,b):
    if a>b:
        return a
    else : 
        return b

result = large (10,4)
print("The largest number is ",result)

def smallest(c,d):
    return min(c,d)
    
minimum = smallest(10,9)
print("The smallest number is ", minimum)
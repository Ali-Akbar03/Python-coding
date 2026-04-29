string="Hello, World!"
count=0
for x in range(0,len(string)-1):
    if string[x].lower() in "aeiou":
        count = count + 1

print("There are",count,"vowels")
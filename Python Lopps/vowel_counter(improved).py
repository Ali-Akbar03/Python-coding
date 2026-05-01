string="Hello, World!"
count=0
for ch in string:
    if ch.lower() in "aeiou":
        count += 1

print(count)
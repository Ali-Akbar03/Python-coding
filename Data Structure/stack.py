list = []

# Append(pushing element)
list.append("C") 
list.append("JAVA")
list.append("C++")
list.append("Python")

print(list)

#pop 
print("The list after using pop function---------------------->")
list.pop()
print(list) #last element "Python" is remeoved from the top of the list list
print(list) #['C', 'JAVA', 'C++']

list.pop()
print(list) #['C', 'JAVA']

list.pop()
print(list) #['C']

list.pop()
if not list:
    print("Nohting is left")
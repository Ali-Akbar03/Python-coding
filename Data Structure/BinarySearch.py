arr = [1,2,3,4,5]
target = 4
found = False

first = 0
last = len(arr)-1

while first <= last :
    mid = (first+last)//2
    if arr[mid]==target:
        found = True
        break
    elif arr[mid]<target:
        first= mid+1
    elif arr[mid]>target:
        last= mid-1

if found:
    print(f"{target} found at index number {mid}")
else :
    print("not found")

from collections import deque
bank=deque(["person1","person2","person3"])

print(bank) #[deque(["person1","person2","person3"])]
bank.popleft()
print(bank) #deque(['person2', 'person3']) 

bank.popleft()
print(bank) #deque(['person3'])

bank.popleft()
if not bank:
    print("No elements left ")
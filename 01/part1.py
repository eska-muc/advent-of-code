list1 = []
list2 = []
with open('input.txt','r') as f:
    for line in f:
        [ n1, n2 ] = line.split()
        list1.append(n1)
        list2.append(n2)

print(f"LIST 1 : {list1}")
print(f"LIST 2 : {list2}")
list1.sort()
list2.sort()
print(f"LIST 1 : {list1}")
print(f"LIST 2 : {list2}")

index = 0
total = 0
for e in list1:
    e1 = int(list1[index])
    e2 = int(list2[index])
    d = abs(e2-e1)
    total = total + d    
    index = index + 1 

print(f"TOTAL: {total}")
    

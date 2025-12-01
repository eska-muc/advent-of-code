list1 = []
list2 = []
filename = "input.txt"
with open(filename, "r") as f:
    for line in f:
        [n1, n2] = line.split()
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
    e1 = list1[index]
    n = list2.count(e1)
    d = int(e1) * n
    total = total + d
    index = index + 1

print(f"TOTAL: {total}")

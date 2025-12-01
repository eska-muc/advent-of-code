import re

# filename = 'sample.txt'
filename = "input.txt"

r1 = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)")
r2 = re.compile("\d{1,3}")

with open(filename, "r") as f:
    input = f.read()
    sum = 0
    for m in r1.findall(input):
        print(f"match {m}")
        numbers = r2.findall(m)
        sum = sum + int(numbers[0]) * int(numbers[1])
    print(f"SUM: {sum}")

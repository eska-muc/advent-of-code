import re

#filename = 'sample2.txt'
filename = 'input.txt'

rmul = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)")
rnum = re.compile("\d{1,3}")
rdo = re.compile("do\(\)")
rdont = re.compile("don\'t\(\)")
scan = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)")

def calc(inputs):
    sum = 0
    for m in rmul.findall(inputs):
        #print (f"match {m}")
        numbers = rnum.findall(m)        
        sum = sum + int(numbers[0])*int(numbers[1])
    return sum

# 01234567890123456789012345678901234567
# mul(x,y)xxxdon't()mul(a,b)do()mul(i,j)
#            |
#                           |

with open(filename,'r') as f:
    input = f.read()
    sum = 0
    sub = ""
    skip = False
    for s in scan.findall(input):
        print(f"{s}")
        if rdont.match(s):
            skip = True
        if rdo.match(s):
            skip = False
        if rmul.match(s) and not skip:
            sub = sub + s
    print(f"{sub}")
    sum = calc(sub)
    print (f"SUM: {sum}")
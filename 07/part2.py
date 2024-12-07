import time

#filename = 'sample.txt'
filename = 'input.txt'
debug = False

operators = [ '+' , '*' , '||']

def calc(a,b,op):
    if op == '+':
        return a+b
    elif op == '*':
        return a*b
    elif op == '-':
        # not used
        return a-b
    elif op == '||':
        return int(str(a)+str(b))
    elif op == '/':
        # not used
        return a/b
    print(f"invalid op {op}")
    return 0
    
# applies ops to numbers 
# e.g nums = [ 1 , 2 ], ops = [ '+' ] => 3
# e.g nums = [ 1 , 2 , 3 ], ops = [ '+','*' ] => 9
def apply(nums,ops):
    res = nums[0]
    for pos in range(len(ops)):
        newres = calc(res,nums[pos+1],ops[pos])
        res = newres
    if debug:
        print(f"{nums} {ops} => {res}")
    return res


def parseinputline(linestr):
    colonpos = linestr.index(':')
    testvalue = int(linestr[0:colonpos])
    numbers = list(map(int,linestr[colonpos+1:].split()))
    return (testvalue,numbers)

# converts a number to string of total length total (with leading zeros)
# input int value
# output value in base 3
#
# e.g 1 => 001
# e.g 2 => 002
# e.g 3 => 010
# e.g 4 => 011
def int2base3(inn,total):
    base = 3
    digits = ['0','1','2']
    res = ""
    if inn==0:
        res = '0'*total
    else:
        n = inn
        while n:     
            res = digits[n % 3] + res
            n = n // 3
        res = '0'*(total-len(res))+res
    if debug:
        print (f"{inn}_3 => {res}")
    return res


# get an array of lists with num op combinations
# e.g. num = 1, ops = ['+', '*' ]
# [ ['+'] , ['*'] ]
# e.g. num = 2, ops = ['+', '*' ]
# [ ['+','+'] , ['+','*'], ['*','+'] , ['*','*'] ]
#     0   0       0   1      1   0       1   1      -> indices in ops array
# e.g. num = 3, ops = ['+', '*' ]
# [ ['+','+','+'] , ['+','+','*'], ['+','*','*'] , ['*','*','*'] , ['*','*','+'] , ['*','*','+'], ['*','+','+'] , ['*','+','*'] ]
def opgen(num,ops):
    result = []
    sizeresult = len(ops)**num
    for r in range(0,sizeresult):
        sublist = ['.'] * num
        result.append(sublist)        
        indices = int2base3(r,num)
        for i in range(0,num):
            sublist[i]=ops[int(indices[i])]
    return result

if __name__ == '__main__' :

    starttime = time.time()

    input = []
    oplists = {}

    with open(filename,'r') as f:
        lines = f.readlines()
        for l in lines:        
            (testresult,listofnumbers) = parseinputline(l.rstrip())
            calibration = {}
            calibration['result']=testresult
            calibration['numbers']=listofnumbers
            oplistkey = len(listofnumbers)-1
            if not oplistkey in oplists:
                oplists[oplistkey]=opgen(oplistkey,operators)            
            input.append(calibration)
            
    print (f"Inputs   : {len(input)}")
    print (f"Operator lists: {len(oplists)} {oplists.keys}")


    totalsum = 0
    for inp in input:
        listlen = len(inp['numbers'])
        check = False
        for oplist in oplists[listlen-1]:
            res = apply(inp['numbers'],oplist)
            if res == inp['result'] and not check:
                check = True
                totalsum = totalsum + res
                print(f"Match: {res} : {inp['numbers']}")
    
    executiontime = time.time()-starttime
    print(f"time {executiontime}")
    print(f"# total sum {totalsum}")
                


def isSafe(report):
    diffs = []
    first = True
    for e in report:
        if not first:
            diffs.append(int(e)-last)
        else:
            first = False
        last = int(e)
    if all(d>0 and abs(d) in [1,2,3] for d in diffs) or all(d<0 and abs(d) in [1,2,3] for d in diffs):
        print(f"Report {report} is safe. Diffs: {diffs}")
        return True
    return False

def canBeDamped(rep):
    for i in range (0,len(rep)):
        testlist = rep.copy()
        del testlist[i]
        if isSafe(testlist):
            return True
    return False

filename = 'input.txt'

with open(filename,'r') as f:
    count = 0
    for line in f:
        report = line.split()
        if isSafe(report):
            count = count + 1
        elif canBeDamped(report):
            count = count + 1
    print(f"# SAFE: {count}")


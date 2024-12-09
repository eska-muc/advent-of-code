import re

# filename = 'sample.txt'
filename = "input.txt"

rulere = re.compile("^([0-9]+)\|([0-9]+)")
pagesre = re.compile("^([0-9]+),([0-9]+)*")

rules = []
pages = []

rulecount = 0
pagelistcount = 0


def checkorder(rule, pagelist):
    start = rule["start"]
    end = rule["end"]
    if start in pagelist and end in pagelist:
        if pagelist.index(start) > pagelist.index(end):
            return False
    return True


def checklist(rules, pagelist):
    for rule in rules:
        if checkorder(rule, pagelist) == False:
            return False
    return True


def summiddlenumbers(correctlists):
    sum = 0
    for list in correctlists:
        midindex = int(len(list) / 2)
        midval = list[midindex]
        print(f"value at {midindex} of {list}: {midval}")
        sum = sum + int(midval)
    return sum


with open(filename, "r") as f:
    lines = f.readlines()
    for l in lines:
        line = l.rstrip()
        rulematch = rulere.match(line)
        pagesmatch = pagesre.match(line)
        if rulematch:
            rulecount = rulecount + 1
            rule = {}
            (rule["start"], rule["end"]) = rulematch.groups()
            rules.append(rule)
        if pagesmatch:
            pagelistcount = pagelistcount + 1
            pagelist = line.split(",")
            pages.append(pagelist)

print(f"{rulecount} rules: {rules}")
print(f"{pagelistcount} pagelists: {pages}")

correctlists = []
for pagelist in pages:
    if checklist(rules, pagelist):
        correctlists.append(pagelist)

print(f"correct lists: {correctlists}")
result = summiddlenumbers(correctlists)
print(f"RESULT: {result}")

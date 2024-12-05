

#filename = 'sample.txt'
filename = 'input.txt'

matrix = []

def printmat(mat,w,h):
    for r in range(0,h):
        for c in range(0,w):
            print(f"{mat[r][c]} ",end='')
        print()


def countwords(wlist):
    ctr = 0
    for wrd in ['MAS','SAM']:
        for w in wlist:
            if w == wrd:
                ctr = ctr + 1
    return ctr

def countcross(submat,w,h):
    ctr = 0
    words = []
    crossword1 = ""
    crossword2 = ""    
    for y in range(0,h):
        for x in range(0,w):            
            if x==y:
                crossword1= crossword1 + submat[y][x]
                crossword2= crossword2 + submat[h-y-1][x]        
    words.append(crossword1)
    words.append(crossword2)
    print(f"crosswords: {crossword1} {crossword2}")
    print(f"words: {words}")        
    return countwords(words)

with open(filename,'r') as f:
    lines = f.readlines()
    row = 0
    for l in lines:
        line = l.rstrip()
        colarr = []
        for c in line:
            colarr.append(c)
        matrix.append(colarr)
        row = row + 1
    rows = row
    cols = len(line)
    print(f"r: {rows} c: {cols}")
    print(f"{matrix}")


# get 4x4 matrices
submatrix = [['.' for x in range(3)] for y in range(3)]
count = 0
smcount = 0
for r in range(0,rows-2):
    for c in range(0,cols-2):        
        # count diagonal words
        for sr in range(0,3):
            for sc in range(0,3):
                submatrix[sr][sc]=matrix[r+sr][c+sc]
        smcount = smcount + 1
        printmat(submatrix,3,3)
        if countcross(submatrix,3,3) == 2:
            count = count + 1
        print()
    print()

print(f"SUBMAT: {smcount}")
print(f"TOTAL: {count}")
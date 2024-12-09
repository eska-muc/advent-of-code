# filename = 'sample.txt'
# filename = 'samplex.txt'
filename = "input.txt"

matrix = []


def printmat(mat, w, h):
    for r in range(0, h):
        for c in range(0, w):
            print(f"{mat[r][c]} ", end="")
        print()


def countwords(wlist):
    ctr = 0
    for wrd in ["XMAS", "SAMX"]:
        for w in wlist:
            if w == wrd:
                ctr = ctr + 1
    return ctr


def countcross(submat, w, h):
    ctr = 0
    words = []
    crossword1 = ""
    crossword2 = ""
    for y in range(0, h):
        for x in range(0, w):
            if x == y:
                crossword1 = crossword1 + submat[y][x]
                crossword2 = crossword2 + submat[h - y - 1][x]
    words.append(crossword1)
    words.append(crossword2)
    print(f"crosswords: {crossword1} {crossword2}")
    print(f"words: {words}")
    return countwords(words)


def countlinewords(row, maxcol):
    words = []
    for startcol in range(0, maxcol):
        word = ""
        for delta in range(0, 4):
            word = word + matrix[row][startcol + delta]
        words.append(word)
    print(f"line {row} => {words}")
    return countwords(words)


def countcolwords(col, maxrow):
    words = []
    for startrow in range(0, maxrow):
        word = ""
        for delta in range(0, 4):
            word = word + matrix[startrow + delta][col]
        words.append(word)
    print(f"col {col} => {words}")
    return countwords(words)


with open(filename, "r") as f:
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
submatrix = [["." for x in range(4)] for y in range(4)]
count = 0
smcount = 0
for r in range(0, rows - 3):
    for c in range(0, cols - 3):
        # count diagonal words
        for sr in range(0, 4):
            for sc in range(0, 4):
                submatrix[sr][sc] = matrix[r + sr][c + sc]
        smcount = smcount + 1
        printmat(submatrix, 4, 4)
        count = count + countcross(submatrix, 4, 4)
        print()
    print()
for r in range(0, rows):
    count = count + countlinewords(r, cols - 3)
for c in range(0, cols):
    count = count + countcolwords(c, rows - 3)

print(f"SUBMAT: {smcount}")
print(f"TOTAL: {count}")

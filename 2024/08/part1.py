# filename = 'sample.txt'
filename = "input.txt"


def printmap(m):
    global x
    global y
    # rows
    for r in range(0, h):
        # columns
        for c in range(0, w):
            char = m[r][c]
            print(f"{char}", end="")
        print()


def checkandsetantinode(map, antinodemap, c, ax, ay):
    if ax >= 0 and ax < w and ay >= 0 and ay < h:
        if map[ay][ax] != c or map[ay][ax] == ".":
            antinodemap[ay][ax] = "#"


def setantinodes(frequencies, antinodemap):
    for k in frequencies.keys():
        tuples = frequencies[k]
        # get pairs
        for i in range(0, len(tuples)):
            for j in range(0, len(tuples)):
                if i != j:
                    x1 = tuples[i]["c"]
                    x2 = tuples[j]["c"]
                    y1 = tuples[i]["r"]
                    y2 = tuples[j]["r"]
                    xdiff = x2 - x1
                    ydiff = y2 - y1
                    if x1 > x2:
                        a1x = x1 + abs(xdiff)
                        a2x = x2 + abs(xdiff)
                    else:
                        a1x = x1 - abs(xdiff)
                        a2x = x2 - abs(xdiff)

                    if y1 > y2:
                        a1y = y1 + abs(ydiff)
                        a2y = y2 + abs(ydiff)
                    else:
                        a1y = y1 - abs(ydiff)
                        a2y = y2 - abs(ydiff)

                    checkandsetantinode(map, antinodemap, k, a1x, a1y)
                    checkandsetantinode(map, antinodemap, k, a2x, a2y)
                    print(
                        f"Pair {k} {i}({x1},{y1}) {j}({x2},{y2}) => {xdiff} {ydiff} a1 ({a1x},{a1y}) a2 ({a2x},{a2y})"
                    )


def countmap(map, chr):
    count = 0
    for line in map:
        for c in line:
            if c == chr:
                count = count + 1
    return count


if __name__ == "__main__":

    map = []
    antinodemap = []
    frequencies = {}

    with open(filename, "r") as f:
        lines = f.readlines()
        row = 0
        for l in lines:
            mapline = list(l.rstrip())
            map.append(mapline)
            antinodemapline = []
            col = 0
            for c in mapline:
                antinodemapline.append(".")
                if c != ".":
                    tuple = {"r": row, "c": col}
                    if not c in frequencies:
                        frequencies[c] = []
                    frequencies[c].append(tuple)
                col = col + 1
            row = row + 1
            antinodemap.append(antinodemapline)
        w = len(map[0])
        h = len(map)
        print(f"Map ({w},{h})")
        printmap(map)
        print(f"Frequencies {frequencies}")
        setantinodes(frequencies, antinodemap)
        print("Anti Node Map")
        printmap(antinodemap)
        x = countmap(antinodemap, "#")
        print(f"Result: {x}")

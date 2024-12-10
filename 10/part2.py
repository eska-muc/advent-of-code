import time

# filename = "sample.txt"
filename = "input.txt"

debug = False

map = []
# width
w = 0
# height
h = 0
scores = []


def appendpoint(list, x, y):
    point = {}
    point["x"] = x
    point["y"] = y
    list.append(point)


def findtrailheads():
    listoftrailheads = []
    for y in range(0, h):
        for x in range(0, w):
            if map[y][x] == 0:
                appendpoint(listoftrailheads, x, y)
    return listoftrailheads


def findpath(ox, oy, x, y):
    currentval = map[y][x]
    candidates = []
    if currentval != 9:
        # check right
        if x < w - 1:
            if map[y][x + 1] == currentval + 1:
                appendpoint(candidates, x + 1, y)
        # check left
        if x > 0:
            if map[y][x - 1] == currentval + 1:
                appendpoint(candidates, x - 1, y)
        # check up
        if y > 0:
            if map[y - 1][x] == currentval + 1:
                appendpoint(candidates, x, y - 1)
        # check down
        if y < h - 1:
            if map[y + 1][x] == currentval + 1:
                appendpoint(candidates, x, y + 1)
        cc = 0
        for c in candidates:
            cc = cc + 1
            if debug:
                print(
                    f"{cc}: {ox},{oy}: {x},{y} ({map[y][x]})=> {c['x']},{c['y']} ({map[c['y']][c['x']]})"
                )
            findpath(ox, oy, c["x"], c["y"])
    else:
        key = f"{x}_{y}"
        if key not in scores[oy][ox]:
            scores[oy][ox][key] = 1
        else:
            old_score = scores[oy][ox][key]
            scores[oy][ox][key] = old_score + 1


def printscoremap(m):
    result1 = 0
    result2 = 0
    for r in m:
        for c in r:
            print(f"{len(c.keys())} ", end="")
            result1 = result1 + len(c.keys())
            for k in c.keys():
                result2 = result2 + c[k]
        print()
    return (result1, result2)


if __name__ == "__main__":

    starttime = time.time()

    with open(filename, "r") as f:
        lines = f.readlines()
        rowcount = 0
        for l in lines:
            maprow = []
            scorerow = []
            line = l.rstrip()
            for c in range(0, len(line)):
                maprow.append(int(line[c]))
                # initialize scores with
                scorerow.append({})
            map.append(maprow)
            scores.append(scorerow)
            rowcount = rowcount + 1
    w = len(map[0])
    h = rowcount

    print(f"Map size: {w} x {h}")

    loth = findtrailheads()

    if debug:
        print(f"Trailheads {loth}")
    for p in loth:
        findpath(p["x"], p["y"], p["x"], p["y"])

    (result1, result2) = printscoremap(scores)
    endtime = time.time()
    print(f"Time    : {endtime-starttime}")
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")

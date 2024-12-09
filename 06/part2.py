import copy
import time

# filename = 'sample.txt'
filename = "input.txt"

map = []

# position
x = 0
y = 0
startx = 0
starty = 0

# up, down, left, right
up = "^"
down = "v"
left = "<"
right = ">"

stepcount = 0
poscount = 0
direction = down

newdir = {up: right, right: down, down: left, left: up}
opposite = {up: down, down: up, left: right, right: left}


def printmap(m, output=True):
    global x, y, startx, starty
    # rows
    for r in range(0, h):
        # columns
        for c in range(0, w):
            char = m[r][c]
            if char == up:
                startx = c
                starty = r
            if output:
                print(f"{char}", end="")
        if output:
            print()


def newpos(curx, cury, dir):
    if dir == up:
        return (curx, cury - 1)
    elif direction == down:
        return (curx, cury + 1)
    elif direction == left:
        return (curx - 1, cury)
    elif direction == right:
        return (curx + 1, cury)
    return (curx, cury)


def checkbounds(x, y):
    return x >= 0 and x < w and y >= 0 and y < h


def step(m):
    global stepcount, poscount, direction, x, y, loopfound
    cont = True
    (nx, ny) = newpos(x, y, direction)
    if checkbounds(nx, ny):
        # check for obstacles
        obj = m[ny][nx]
        if obj == "." or obj in (up, down, left, right):
            # print (f"{direction}")
            stepcount = stepcount + 1
            m[y][x] = direction
            if direction == up:
                upmap[y][x] = upmap[y][x] + 1
            if direction == down:
                downmap[y][x] = downmap[y][x] + 1
            if direction == left:
                leftmap[y][x] = leftmap[y][x] + 1
            if direction == right:
                rightmap[y][x] = rightmap[y][x] + 1
            if (
                upmap[y][x] > 1
                or downmap[y][x] > 1
                or leftmap[y][x] > 1
                or rightmap[y][x] > 1
            ):
                poscount = poscount + 1
                loopfound = True
                cont = False
            x = nx
            y = ny
        elif obj == "#":
            # change direction
            direction = newdir[direction]
            m[y][x] = "X"
    else:
        cont = False
    return cont


if __name__ == "__main__":

    starttime = time.time()

    with open(filename, "r") as f:
        lines = f.readlines()
        for l in lines:
            map.append(list(l.rstrip()))

    # height
    h = len(map)
    # width
    w = len(map[0])

    printmap(map)
    direction = map[y][x]
    count = 0

    # init direction maps
    directionmap = []
    for n in range(0, h):
        directionmap.append([0 for c in range(0, w)])

    for cy in range(0, h):
        for cx in range(0, w):
            testmap = copy.deepcopy(map)
            count = count + 1
            print(
                f"Testing position ({cx:03d},{cy:03d}): positions which causes a loop: {poscount:04d}"
            )
            stepcount = 0
            obj = testmap[cy][cx]
            if obj == ".":
                testmap[cy][cx] = "#"
                upmap = copy.deepcopy(directionmap)
                downmap = copy.deepcopy(directionmap)
                rightmap = copy.deepcopy(directionmap)
                leftmap = copy.deepcopy(directionmap)
                printmap(testmap, False)
                x = startx
                y = starty
                direction = testmap[starty][startx]
                stepcount = 0
                loopfound = False
                while step(testmap) and stepcount < w * h:
                    pass
            else:
                print(f"field at ({cx},{cy}) already occupied with {obj}")
            testmap = None
            upmap = None
            downmap = None
            rightmap = None
            leftmap = None

    executiontime = time.time() - starttime
    print(f"Execution time: {executiontime}")
    print(f"# Position for obstacleas which causes a loop: {poscount}")

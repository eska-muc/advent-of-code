# filename = 'sample.txt'
filename = "input.txt"

map = []

# position
x = 0
y = 0

# up, down, left, right
up = "^"
down = "v"
left = "<"
right = ">"

stepcount = 0
poscount = 1
direction = down

newdir = {up: right, right: down, down: left, left: up}


def printmap(m):
    global x
    global y
    # rows
    for r in range(0, h):
        # columns
        for c in range(0, w):
            char = m[r][c]
            if char in (up, down, left, right):
                x = c
                y = r
            print(f"{char}", end="")
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
    global stepcount, poscount, direction, x, y
    cont = True
    (nx, ny) = newpos(x, y, direction)
    if checkbounds(nx, ny):
        # check for obstacles
        obj = m[ny][nx]
        if obj == "." or obj == "X":
            stepcount = stepcount + 1
            if obj == ".":
                poscount = poscount + 1
            m[y][x] = "X"
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

    while step(map):
        print(f"{stepcount}", end=" ")

    print()
    printmap(map)
    print(f"Distinct positions: {poscount}")

import time

filename = 'sample.txt'
# filename = "input.txt"

debug = True

def getblocks(diskmap):
    blocklist = []
    blockstr = ""
    fileid = 0
    for i in range(0, len(diskmap), 2):
        size = int(diskmap[i])
        for f in range(0, size):
            fileblock = {}
            fileblock["t"] = "file"
            fileblock["id"] = fileid
            blocklist.append(fileblock)
        freespace = int(diskmap[i + 1]) if i + 1 < len(diskmap) else 0
        for f in range(0, freespace):
            freeblock = {}
            freeblock["t"] = "free"
            blocklist.append(freeblock)
        blockstr = blockstr + str(fileid) * size + "." * freespace
        fileid = fileid + 1
    return (blockstr, blocklist)


def printblocklist(blocklist):
    for b in blocklist:
        if b["t"] == "file":
            print(str(b["id"]), end="")
        else:
            print(".", end="")
    print()


def compact(blocklist):
    # find first free block
    firstfree = 0
    for i in range(0, len(blocklist)):
        if blocklist[i]["t"] == "free":
            firstfree = i
            break
    # find last occupied
    for i in range(len(blocklist) - 1, 0, -1):
        if blocklist[i]["t"] == "file":
            lastoccupied = i
            break
    finished = firstfree > lastoccupied
    if not finished:
        swap = blocklist[lastoccupied]
        blocklist[lastoccupied] = blocklist[firstfree]
        blocklist[firstfree] = swap
    return finished


def checksum(blocklist):
    sum = 0
    for pos in range(0, len(blocklist)):
        if blocklist[pos]["t"] == "file":
            sum = sum + pos * blocklist[pos]["id"]
    return sum

if __name__ == "__main__":

    starttime = time.time()

    with open(filename, "r") as f:
        input = list(f.readline().rstrip())
    (blockstr, blocklist) = getblocks(input)
    finished = False
    while not finished:
        finished = compact(blocklist)
        if debug:
            printblocklist(blocklist)

    result = checksum(blocklist)
    endtime = time.time()
    print(f"Result: {result}")
    print(f"Time  : {endtime-starttime}")
    

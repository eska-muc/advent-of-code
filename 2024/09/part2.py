import time

# filename = "sample.txt"
filename = "input.txt"

debug = "NONE"
# debug = "BLOCKLIST"
# debug = "ALL"

def getblocks(diskmap):
    blocklist = []
    blockstr = ""
    fileid = 0
    blockid = 0
    filelist = []
    freelist = []
    for i in range(0, len(diskmap), 2):
        size = int(diskmap[i])
        startblock = blockid
        for f in range(0, size):
            fileblock = {}
            fileblock["t"] = "file"
            fileblock["id"] = fileid
            blockid = blockid + 1
            blocklist.append(fileblock)
        file = {}
        file["id"] = fileid
        file["size"] = size
        file["startblock"] = startblock
        file["endblock"] = blockid - 1
        filelist.append(file)
        freespace = int(diskmap[i + 1]) if i + 1 < len(diskmap) else 0
        if freespace > 0:
            startfree = blockid
            for f in range(0, freespace):
                freeblock = {}
                freeblock["t"] = "free"
                blockid = blockid + 1
                blocklist.append(freeblock)
            free = {}
            free["startblock"] = startfree
            free["endblock"] = blockid - 1
            free["size"] = freespace
            freelist.append(free)
        blockstr = blockstr + str(fileid) * size + "." * freespace
        fileid = fileid + 1
    return (blockstr, blocklist, filelist, freelist)


def printblocklist(blocklist):
    for b in blocklist:
        if b["t"] == "file":
            print(str(b["id"]), end="")
        else:
            print(".", end="")
    print()


def move(file, newstart, blocklist):
    oldstart = file["startblock"]
    oldend = file["endblock"]
    if debug == "ALL":
        print(f"Move file {file} to {newstart}")
    for b in range(newstart, newstart + file["size"]):
        fileb = {}
        fileb["t"] = "file"
        fileb["id"] = file["id"]
        blocklist[b] = fileb
    for f in range(oldstart, oldstart + file["size"]):
        freeb = {}
        freeb["t"] = "free"
        blocklist[f] = freeb


def updatefreelist(freelist, blocklist):
    blockid = 0
    freecount = 0
    freestart = 0
    freefound = False
    freelist.clear()
    for b in blocklist:
        if b["t"] == "free":
            if not freefound:
                freefound = True
                freestart = blockid
                freecount = 1
            else:
                freecount = freecount + 1
        if b["t"] == "file":
            if freefound:
                freefound = False
                free = {}
                free["startblock"] = freestart
                free["endblock"] = blockid
                free["size"] = freecount
                freelist.append(free)
        blockid = blockid + 1
    if freefound:
        free = {}
        free["startblock"] = freestart
        free["endblock"] = blockid
        free["size"] = freecount
        freelist.append(free)
    if debug == "ALL":
        print(f"freelist {freelist}")


def compact(blocklist, filelist, freelist):
    for file in filelist[::-1]:
        if debug == "ALL":
            print(f"file {file['id']} with size {file['size']}")
        # find matching freespace
        freeindex = 0
        freefound = False
        for free in freelist:
            if free["size"] >= file["size"]:
                freefound = True
                break
            freeindex = freeindex + 1
        if freefound and freelist[freeindex]["startblock"] < file["startblock"]:
            newstartblock = freelist[freeindex]["startblock"]
            if debug == "ALL":
                print(f"Move file {file['id']} to block {newstartblock}")
            move(file, newstartblock, blocklist)
            if debug == "BLOCKLIST" or debug == "ALL":
                printblocklist(blocklist)
            oldfreesize = freelist[freeindex]["size"]
            oldfreestartblock = freelist[freeindex]["startblock"]
            updatefreelist(freelist, blocklist)
            # update file information (not required)
            file["startblock"] = newstartblock
            file["endblock"] = newstartblock + file["size"]


def getstats(blocklist):
    occ = 0
    free = 0
    files = {}
    for b in blocklist:
        if b["t"] == "file":
            occ = occ + 1
            if b["id"] not in files:
                files[b["id"]] = 1
            else:
                files[b["id"]] = files[b["id"]] + 1
        if b["t"] == "free":
            free = free + 1
    return (occ, free, files)


def getstatfreelist(freelist):
    sum = 0
    for fb in freelist:
        sum = sum + fb["size"]
    return sum


def getstatfilelist(filelist):
    sum = 0
    for fb in filelist:
        sum = sum + fb["size"]
    return sum


def checksum(blocklist):
    sum = 0
    for pos in range(0, len(blocklist)):
        if blocklist[pos]["t"] == "file":
            sum = sum + pos * blocklist[pos]["id"]
    return sum


def printtable(rows):
    colwidths = []
    # get max width
    for r in range(0, len(rows)):
        for c in range(0, len(rows[r])):
            if r == 0:
                colwidths.append(0)
            if len(rows[r][c]) > colwidths[c]:
                colwidths[c] = len(rows[r][c])
    for r in rows:
        for c in range(0, len(r)):
            pads = " " * (colwidths[c] - len(r[c]))
            print(f"{r[c]}{pads} ", end="")
        print()


if __name__ == "__main__":

    starttime = time.time()

    with open(filename, "r") as f:
        input = list(f.readline().rstrip())
    (blockstr, blocklist, filelist, freelist) = getblocks(input)

    if debug == "ALL":
        for fi in filelist:
            print(
                f"file {fi['id']} blocks {fi['startblock']} - {fi['endblock']} (size {fi['size']}) "
            )
        for fr in freelist:
            print(
                f"free blocks {fr['startblock']} - {fr['endblock']} (size {fr['size']}) "
            )

    (o, f, filesdict) = getstats(blocklist)
    ofilelist = getstatfilelist(filelist)
    ffreelist = getstatfreelist(freelist)
    oldfilelistlen = len(filelist)
    oldfreelistlen = len(freelist)
    oldblocklistlen = len(blocklist)

    compact(blocklist, filelist, freelist)
    endtime = time.time()

    (o2, f2, filesdict2) = getstats(blocklist)
    o2filelist = getstatfilelist(filelist)
    f2freelist = getstatfreelist(freelist)

    # Some stats - helped debugging part 2
    tablerows = []
    tablerows.append(["", "Before", "After"])
    tablerows.append(["Blocklist", f"{oldblocklistlen}", f"{len(blocklist)}"])
    tablerows.append(
        [
            "# of files in blocklist",
            f"{len(filesdict.keys())}",
            f"{len(filesdict2.keys())}",
        ]
    )
    tablerows.append(["Filelist", f"{oldfilelistlen}", f"{len(filelist)}"])
    tablerows.append(["Freelist", f"{oldfreelistlen}", f"{len(freelist)}"])
    tablerows.append(["Used (blocklist)", f"{o}", f"{o2}"])
    tablerows.append(["Used (filelist)", f"{ofilelist}", f"{o2filelist}"])
    tablerows.append(["Free (blocklist)", f"{f}", f"{f2}"])
    tablerows.append(["Free (freelist)", f"{ffreelist}", f"{f2freelist}"])
    printtable(tablerows)

    result = checksum(blocklist)

    print(f"Result: {result}")
    print(f"Time  : {endtime-starttime}")

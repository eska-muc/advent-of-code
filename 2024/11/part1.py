import argparse
import copy
import time

parser = argparse.ArgumentParser(prog="part1.py",
                                     description="Advent of Code 2024 - Day 11, Part 1. See https://adventofcode.com/2024/day/11")
parser.add_argument("-f filename","--filename", default="sample.txt", help="Input filename. Default is 'sample.txt'")
parser.add_argument("-d","--debug", default=False, help="Enable debug output",action="store_true")
parser.add_argument("-n","--times", default=25 , help="Number of times to blink")

def log(message):
    if args.debug:
        print(message)

def compact(instr):    
    return str(int(instr))

def iteration(stones):
    output = []
    for s in stones:
        if s == "0":
            output.append("1")
        elif len(s)%2 == 0:
            half = int(len(s)/2)
            output.append(compact(s[:half]))
            output.append(compact(s[half:]))
        else:
            output.append(compact(f"{int(s)*2024}"))
    return output
                    

if __name__ == "__main__":
    args = parser.parse_args()
    with open(args.filename,"r") as f:
        input = f.readline().rstrip()
    print(f"Input: {input}")
    starttime = time.time()
    stones = input.split()
    for i in range(0,int(args.times)):
        newstones = iteration(stones)
        log(f"{i} {len(newstones)}")
        stones = copy.deepcopy(newstones)
    endtime = time.time()
    print(f"Time: {endtime-starttime}")
    print(f"Result: {len(stones)}")

    
    
    

    

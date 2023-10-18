import sys, os

factor = float(sys.argv[1])
inputfile = sys.argv[2]
outputfile = sys.argv[3]

lines = open(inputfile,"r").read().split("\n")
for index, line in enumerate(lines):
    parts = line.split(" ")
    for pindex, part in enumerate(parts):
        for letter in ["X", "Y", "Z", "I", "J", "K" ]:
            if letter in part:
                parts[pindex] = "%s%s" % (letter, round(float(part.split(letter)[1]) * factor , 4))
    lines[index] = " ".join(parts)

print("\n".join(lines))
open(outputfile,"w").write("\n".join(lines))

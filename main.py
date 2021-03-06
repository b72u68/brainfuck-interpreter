import sys
from brainfuck import run, parse

if len(sys.argv) < 2:
    raise Exception("Missing brainfuck file.")

fname = sys.argv[1]
extension = fname.split(".")[-1]

if extension != "bf":
    raise Exception("Unsupported file type (brainfuck file has to end with '.bf').")

try:
    file = open(fname, 'r')
    raw = "".join(file.readlines())

    PROG = parse(raw)

    run(PROG)

except Exception as e:
    print(e)

import sys

CELL_SIZE = 30000

COMMANDS = ["+", "-", ".", ",", ">", "<", "[", "]"]
SPACE_CHARS = [' ', '\t', '\n']
CELLS = [0] * CELL_SIZE
PTR = 0
BEGIN_LOOP_IDX = []


def brainfuck(PROG):
    global CELLS, PTR, BEGIN_LOOP_IDX

    idx = 0
    while idx < len(PROG):

        command = PROG[idx]

        if command == ">":
            PTR = (PTR + 1) % CELL_SIZE

        elif command == "<":
            PTR = (CELL_SIZE + PTR - 1) % CELL_SIZE

        elif command == "+":
            CELLS[PTR] = CELLS[PTR]+1 if CELLS[PTR] < 255 else 0

        elif command == "-":
            CELLS[PTR] = CELLS[PTR]-1 if CELLS[PTR] > 0 else 255

        elif command == ".":
            sys.stdout.write(chr(CELLS[PTR]))

        elif command == ",":
            CELLS[PTR] = ord(sys.stdin.read(1))

        elif command == "[":
            if CELLS[PTR] == 0:
                open = 1
                temp_idx = idx + 1
                while temp_idx < len(PROG) and open != 0:
                    if PROG[temp_idx] == "[":
                        open += 1

                    elif PROG[temp_idx] == "]":
                        open -= 1

                    if open < 0:
                        raise Exception('Too many "]"')

                    temp_idx += 1
                if open > 0:
                    raise Exception(f'Missing "]" for "[" in position {idx}')
                idx = temp_idx
            else:
                BEGIN_LOOP_IDX.append(idx)

        elif command == "]":
            if not BEGIN_LOOP_IDX:
                raise Exception(f'Missing "[" for "]" in position {idx}')

            if CELLS[PTR] != 0:
                idx = BEGIN_LOOP_IDX.pop()
                continue
            else:
                BEGIN_LOOP_IDX.pop()

        idx += 1


if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise Exception("Missing brainfuck file.")

    fname = sys.argv[1]
    extension = fname.split(".")[-1]

    if extension != "bf":
        raise Exception("Unsupported file (brainfuck file has to end with '.bf').")

    PROG = []

    try:
        file = open(fname, 'r')

        while True:
            char = file.read(1)

            if not char:
                break

            if char in COMMANDS:
                PROG.append(char)

            elif char not in SPACE_CHARS:
                raise Exception(f'Invalid character: {char}')

        brainfuck(PROG)

    except Exception as e:
        print(e)

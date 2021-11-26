import sys

COMMANDS = ["+", "-", ".", ",", ">", "<", "[", "]"]
SPACE_CHARS = [' ', '\t', '\n']

# standard cell size for brainfuck
CELL_SIZE = 30000

# standard unsigned 8-bit integer
VALUE_MIN = 0
VALUE_MAX = 255

CELLS = [0] * CELL_SIZE
PTR = 0
BEGIN_LOOP_IDX = []


def run(PROG):

    global CELLS, PTR, BEGIN_LOOP_IDX

    idx = 0

    while idx < len(PROG):

        command = PROG[idx]

        if command == ">":
            PTR = (PTR+1) % CELL_SIZE

        elif command == "<":
            PTR = (CELL_SIZE+PTR-1) % CELL_SIZE

        elif command == "+":
            CELLS[PTR] = (CELLS[PTR]+1) if CELLS[PTR] < VALUE_MAX else VALUE_MIN

        elif command == "-":
            CELLS[PTR] = CELLS[PTR]-1 if CELLS[PTR] > VALUE_MIN else VALUE_MAX

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
                    temp_idx += 1

                if open != 0:
                    raise Exception(f'Missing "]" for "[" in position {idx}.')

                idx = temp_idx + 1

                continue

            BEGIN_LOOP_IDX.append(idx)

        elif command == "]":
            if not BEGIN_LOOP_IDX:
                raise Exception(f'Missing "[" for "]" in position {idx}.')

            if CELLS[PTR] != 0:
                idx = BEGIN_LOOP_IDX.pop()
                continue

            BEGIN_LOOP_IDX.pop()

        idx += 1


def parse(raw):

    PROG = []
    ctr = 0
    open_loops = 0

    for char in raw:
        if not char:
            break

        ctr += 1

        if char in COMMANDS:
            if char == "[":
                open_loops += 1
            elif char == "]":
                open_loops -= 1
            PROG.append(char)

        elif char in SPACE_CHARS:
            continue

        else:
            raise Exception(f'Invalid character at position {ctr}: {char}.')

    if open_loops != 0:
        raise Exception('Mismatch number of "[" and "]".')

    return PROG

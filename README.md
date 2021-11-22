# Brainfuck Interpreter

Interpreter for Brainfuck in Python

## About Brainfuck

You can read about Brainfuck on this Wikipedia page: [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck).

## Usage

Simply run

```bash
python3 main.py [filename]
```

There are sample brainfuck files in `/examples` directory if you want to play with this.
Note: brainfuck files have to end with `.bf` extension.

## How it works

At the start of the program, initialize a char array `CELLS` of size 30000, a pointer
`PTR` at index 0, and an empty array `BEGIN_LOOP_IDX` to store the address or
index of begin loop command (`[`) in the brainfuck file. Scan each command in
the file, if the command is

- `>`: increase `PTR`. If it is larger than 30000, reset it to 0 (wrap around).
- `<`: decrease `PTR`. If it is smaller than 0, assign it to 30000 - 1 (wrap around).
- `+`: increase the value at `PTR` in `CELLS` by 1.
- `-`: decrease the value at `PTR` in `CELLS` by 1.
- `,`: get the user input and store it in `CELLS` at the location of `PTR`.
- `.`: put the value in `CELLS` at the location of `PTR` to the output stream.
- `[`: if the value at pointer is 0, scan through the file and find its matching
  `]`. Run the command next to its matching `]`. Else store its location in
  `BEGIN_LOOP_IDX` and run the command in the loop.
- `]`: if `BEGIN_LOOP_IDX` is empty, raise error because there isn't any matching
  `[`. Else, if the value at `PTR` if not 0, get the location of matching `[` in
  `BEGIN_LOOP_IDX` and jump to it, else continue to next command.

## Future plan

Might write this interpreter in Ocaml (because I love Ocaml).

- [ ] Create a shell for brainfuck.

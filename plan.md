# Plans for brainfuck shell

## Commands

### Brainfuck

Brainfuck commands can only contain `<`, `>`, `+`, `-`, `.`, `,`, `[`, `]`.

### High-level commands

High-level commands have to start with `#`.

- `clear`: clear values in `CELLS` (keep the position of `PTR`).
- `reset`: clear values in `CELLS` and set `PTR` to 0.
- `CELL_SIZE=[num]`: set `CELL_SIZE` to input `num`. Doing this would reset the
  cells and pointer.
- `CELLS`: print the values in `CELLS`.
- `PTR`: print the value of `PTR`.

# Specification: roman-cli

_The approved specification of run 14d32e0e (2026-10-20), kept up to date by agent-platform. Edit it freely and commit the edit: the next run reads it as it is._

A Python command-line tool that converts integers 1-3999 to Roman numerals and Roman numerals back to integers. It rejects invalid input with a clear error message and a non-zero exit code.

## User stories

Stories marked _not implemented yet_ are specified but not built: their tasks haven't run or didn't get done. The next run on this project plans them again.

### US-1 (must) · not implemented yet

As **CLI user**, I want **to convert an integer from 1 to 3999 to a Roman numeral**, so that I can get its Roman representation.

Acceptance criteria:

- Given 4 the output is IV; 9 -> IX; 14 -> XIV; 1994 -> MCMXCIV; 3999 -> MMMCMXCIX; 1 -> I
- Output is printed to stdout alone on one line, exit code 0
- 0, negative numbers and 4000 or more are rejected with an error message stating the valid range 1-3999
- Non-integer input (e.g. 'abc', '3.5', empty string) is rejected with a clear error

### US-2 (must) · not implemented yet

As **CLI user**, I want **to convert a Roman numeral to an integer**, so that I can read Roman numerals as numbers.

Acceptance criteria:

- MCMXCIV -> 1994; IV -> 4; MMMCMXCIX -> 3999; I -> 1
- Lowercase input is accepted and treated as uppercase
- Output is the integer on stdout, exit code 0
- Invalid characters (e.g. 'ABC') are rejected with an error naming the problem
- Non-canonical forms such as IIII, VX, IC, IIX, VV, MMMM are rejected as invalid Roman numerals
- Empty string is rejected

### US-3 (must) · not implemented yet

As **CLI user or script**, I want **errors reported clearly on stderr with a non-zero exit code**, so that I can tell failures from successes and understand them.

Acceptance criteria:

- Every rejected input prints a one-line human-readable message to stderr, no stack trace
- Exit code is non-zero (2) for invalid input and nothing is written to stdout
- The CLI auto-detects direction: digits means integer to Roman, letters means Roman to integer
- Running with no arguments or with too many prints a usage message and exits non-zero

## Non-functional requirements

- Python 3 standard library only
- Conversion logic is separate from CLI handling so it can be unit tested
- Round trip: converting every integer 1-3999 to Roman and back returns the original value

## Out of scope

- Numbers above 3999 (vinculum/overline notation)
- Zero (nulla) and negative numbers
- Interactive mode or batch/file input
- Lenient parsing of non-canonical numerals

## Open questions and assumptions

- Should the direction be auto-detected or use subcommands/flags? Assumed: auto-detected from a single positional argument.
- Should lowercase Roman input be accepted? Assumed: yes.
- Should non-canonical numerals like IIII be rejected? Assumed: yes, only canonical forms are valid.

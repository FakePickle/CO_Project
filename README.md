# Assembly Language Interpreter

This Python script serves as an interpreter for a custom assembly-like language. It reads a series of assembly-like instructions, performs parsing, executes operations, and handles different types of instructions.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Input Handling](#input-handling)
- [Memory and Registers](#memory-and-registers)
- [Output and Line Formatting](#output-and-line-formatting)
- [Floating Point Operations](#floating-point-operations)
- [Utility Functions](#utility-functions)
- [Execution Loop](#execution-loop)
- [Opcode Definitions](#opcode-definitions)
- [Execution Flow](#execution-flow)
- [Final Output](#final-output)
- [Contributors](#contributors)

## Features

- **Parsing and Validation:** The script parses the input assembly-like code, validates syntax, checks for errors, and handles different types of instructions.
  
- **Execution of Operations:** Executes various types of operations (arithmetic, bitwise, memory-related) based on the provided instructions.
  
- **Error Handling:** Provides detailed error messages for various scenarios such as invalid syntax, undefined variables/labels, illegal register usage, etc.

## Usage

1. **Input:** The assembly-like code needs to be provided either through standard input or by reading from a file.

2. **Execution:** Run the Python script providing the assembly code input.

3. **Output:** The script generates output displaying the state of registers after each instruction execution and final memory content.

## Input Handling

- **Terminal Inputs:** Reads assembly-like code from standard input.
- **File Inputs:** Option to read assembly code from a file by uncommenting the corresponding code block.

## Memory and Registers

- **Memory (mem):** Represents memory with 128 elements, each a 16-bit string.
- **Registers (Reg_File):** Holds registers from '000' to '111', each associated with a 16-bit value.

## Output and Line Formatting

- **Line Output (line_output):** Prints the program counter and the state of registers after executing each line of code.

## Floating Point Operations

- **Floating Point Conversion:** Functions to convert floating-point numbers to binary and vice versa using IEEE 754 standard.

## Utility Functions

- **Binary to Decimal Conversion (bin_to_dec):** Converts a binary string to a decimal integer.
- **Decimal to Binary Conversion (dec_to_bin):** Converts a decimal integer to a binary string.
- **Floating Point Operations:** Functions for floating-point arithmetic operations and register manipulations.

## Execution Loop

- **Execution (execution):** Splits the line, determines the type of instruction, and executes it accordingly.
- **Program Counter (PC):** Controls the execution flow by incrementing and jumping based on instructions.

## Opcode Definitions

- **Opcode Dictionary (opcode):** Holds opcodes mapped to their respective functions and types for execution.
- **Types (A to E):** Categorizes instructions based on their formats for efficient execution.

## Execution Flow

- **Loop (while loop):** Continuously executes instructions until encountering the 'hlt' instruction.

## Final Output

- **Line Output and Memory Dump:** Displays the final state of registers after execution and prints the updated memory content.

## Contributors

- [Harsh Mistry](https://github.com/FakePickle)
- [Aditya Jagadale](https://github.com/jaagss)
- [Hemanth Dindigallu](https://github.com/hemanthdindigallu)
- [Anushka Korlapati](https://github.com/anushka-korlapati)

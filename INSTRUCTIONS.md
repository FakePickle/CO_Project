# Custom 16-bit ISA and Assembly Language

## Overview

This repository contains a custom 16-bit Instruction Set Architecture (ISA) along with an assembly language supporting various instructions, addressing modes, and binary encodings. The ISA comprises six instruction types (A to F), each with specific opcodes, syntax, and semantics.

## Instruction Set Architecture (ISA)

The ISA provides a diverse set of instructions categorized into six types:

### Type A Instructions (3-register type)

- **Instructions:** Addition, Subtraction, Multiply, XOR, OR, AND
- **Syntax:** `add reg1 reg2 reg3`, `sub reg1 reg2 reg3`, ...
- **Semantics:** Performs arithmetic and bitwise operations on registers.

### Type B Instructions (register and immediate type)

- **Instructions:** Move Immediate, Right Shift, Left Shift
- **Syntax:** `mov reg1 $Imm`, `rs reg1 $Imm`, ...
- **Semantics:** Moves immediate value or performs shifts on registers.

### Type C Instructions (2-register type)

- **Instructions:** Move Register, Invert, Compare
- **Syntax:** `mov reg1 reg2`, `not reg1 reg2`, ...
- **Semantics:** Manipulates register contents.

### Type D Instructions (register and memory address type)

- **Instructions:** Load, Store
- **Syntax:** `ld reg1 mem_addr`, `st reg1 mem_addr`
- **Semantics:** Loads data from memory to register, stores data from register to memory.

### Type E Instructions (memory address type)

- **Instructions:** Unconditional Jump, Jump If Less Than, Jump If Greater Than, Jump If Equal
- **Syntax:** `jmp mem_addr`, `jlt mem_addr`, ...
- **Semantics:** Directs program flow based on conditions.

### Type F Instructions (halt)

- **Instruction:** Halt
- **Syntax:** `hlt`
- **Semantics:** Stops the machine from executing until reset.

## Register and Flag Details

- **Registers:** R0 to R6, FLAGS
- **FLAGS Register Semantics:** Overflow (V), Less than (L), Greater than (G), Equal (E).

## Binary Encoding for Instructions

The ISA employs six encoding types (A to F) with distinct formats, each being 16 bits long. Encoding styles vary based on instruction types.

## Executable Binary Syntax

The executable binary follows this format:


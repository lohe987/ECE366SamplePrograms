
# Authors: Trung Le, Wenjing Rao
# This program is a simulator packed with both assembler and disassembler.
# Simulator has 2 modes:
#            Debug mode:  Execute program every # steps and
#                         output the state of each reg, and PC
#            Normal mode: Execute program all at once

Parameters:
d_mem.txt   Data memory containing 16-bits binary each line
i_mem.txt   Instr memory containing the assembly instr for simulation

Behavior:
In Simulation's debugging mode, program will run for every # steps ( provided by user ), and outputting
current PC , and state of all registers. At 'finish' instruction, program terminates and write
everything back into d_mem.txt

In Simulation's normal mode, program runs without interruption and output state of all registers
at the end. At 'finish' instruction, program terminates and write everything back into d_mem.txt


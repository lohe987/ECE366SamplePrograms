
# Authors: Trung Le, Wenjing Rao
# This program is a simulator packed with both assembler and disassembler.
# Simulator has 2 modes:
#            Debug mode:  Execute program every # steps and
#                         output the state of each reg, and PC
#            Normal mode: Execute program all at once

![alt text](https://github.com/lohe987/ECE366SamplePrograms/blob/master/sample_ISA_package/github.png)
Parameters:
d_mem.txt   Data memory containing 16-bits binary each line
i_mem.txt   Instr memory containing the assembly instr for simulation

Behavior:
In Simulation's debugging mode, program will run for every # steps ( provided by user ), and outputting
current PC , and state of all registers. At 'finish' instruction, program terminates and write
everything back into d_mem.txt

In Simulation's normal mode, program runs without interruption and output state of all registers
at the end. At 'finish' instruction, program terminates and write everything back into d_mem.txt

Files:
d_mem.txt       Currently contains example data memory, where 
                P in mem[0],  T in mem[3], pattern array in mem[8:107]
        
i_mem.txt       Currently contains the program 6^P%17. This is just the basic 
                add-substract algorithm to calculate power/modulus manually. 
                This was meant for example of how ISA would work.
                
Simulator.py    Python file with simulator packed with assembler/disassembler in 1 package.
                If 'disassembler' mode is chosen, input file should be in binary format
                
input.txt       Example of how input file for disassembler would look like


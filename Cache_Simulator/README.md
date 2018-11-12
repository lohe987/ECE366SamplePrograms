# Project: Cache Simulation       
## * Authors: Trung Le, Wenjing Rao*  
This Python program reads in MIPS instruction in hex and simulates its architecture, outputing  the result of registers, cache hit/miss and Dynamic Instruction Count (DIC).  
Note: This program also simulates the STORE_WORD (sw) instruction , which you do not need to do for your Project 4.

## Settings:  
Instructions supported: add, sub, addi, beq, bne, slt, lw ,sw.  
Registers supported: 8 registers from $0 - $7, where $0 is always 0  
Data memory range: 0x2000 - 0x3000  
Instruction memory range: 0x0000 - 0x1000  
Deadloop at "0x1000ffff"

## Files:
```
cache.py
```
Python file to simulates MIPS ISA with limited instructions supported
<br />
  
  
```
i_mem.txt
```
Currently contains example of an MIPS assembly file, which is located in Project4_example.asm


## Simulation vs MARS:
Result of simulation after running example i_mem.txt:  
![alt text](https://github.com/lohe987/ECE366SamplePrograms/blob/master/Cache_Simulator/githubp4new.png)
  
Result of MARS:  
![alt text](https://github.com/lohe987/ECE366SamplePrograms/blob/master/Cache_Simulator/githubp4_1.png)

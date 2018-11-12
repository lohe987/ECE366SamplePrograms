# Project: MIPS_sim     
## * Authors: Trung Le, Wenjing Rao*  
These sample Python programs show how to read in a file of i_mem.txt (MIPS instruction in hex) and simulates its architecture, outputing  the result of registers, cache hit/miss and Dynamic Instruction Count (DIC).  

## Settings:  
Instructions supported: add, sub, addi, beq, bne, slt, lw ,sw.  
Registers supported: 8 registers from $0 - $7, where $0 is always 0  
Data memory range: 0x2000 - 0x3000  
Instruction memory range: 0x0000 - 0x1000  
Deadloop at "0x1000ffff"

## Files:
```
cache.py
mips_sim.py
```
Python files to simulates MIPS ISA, and cache hit/miss with limited instructions supported
<br />
  
  
```
i_mem.txt
```
Currently contains example of an MIPS assembly file, which is located in Project4_example.asm


## Simulation vs MARS:
Result of simulation after running example i_mem.txt:  
![alt text](https://github.com/lohe987/ECE366SamplePrograms/blob/master/MIPS_sim/githubp4new.png)
  
Result of MARS:  
![alt text](https://github.com/lohe987/ECE366SamplePrograms/blob/master/MIPS_sim/githubp4_1.png)

### As you can see, your MIPS_sim should be able to output of what the MARS' results are as well

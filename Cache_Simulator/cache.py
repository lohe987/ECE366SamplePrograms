
# Authors: Trung Le, Weijing Rao

# This Python program simulates cache behavior from a valid MARS program 
# and output simple statistics such as DIC, hit/miss rate of cache.
# Settings:
#       Single-Cycle CPU
#       Total of 4096 memory spaces
#       Direct-mapped cache, block size 32 bits ,total 8 blocks
# NOTE: Since this is a simple Cache simulator *WITHOUT* replacement policy (Least Recently Used, etc),
#       cache hit/miss will also write into memory along with cache, that way if a block is replaced the memory
#       still has most recently updated value. 
#  
#       Implementing LRU policy should be pretty good idea for extra credit though. 

import math
# For sake of simple example, let's have all the settings as global-variables 
# instead of seperate config file
blk_size = 32    # each block is 32 bits
total_blk = 8    # 8 blocks in cache
blk_offset = int(math.log(total_blk,2))
mem_space = 4096 # Memory addr starts from 2000 , ends at 3000.  Hence total space of 4096


def simulate(Instruction,InstructionHex):
    print("***Starting simulation***")
    print("Settings:")
    print('Cache block size: '+ str(blk_size) +' bits')
    print("Number of total blocks: "+ str(total_blk))

    Register = [0,0,0,0,0,0,0,0]    # initialize all values in registers to 0
    Memory = [0 for i in range(mem_space)] 
    Valid =  [0 for i in range(total_blk)]              # valid bit
    Tag   =  ['0' for i in range(total_blk)]            # Tag for cache
    Cache =  [0 for i in range(total_blk)]              # Cache data
    Misses = 0
    Hits = 0
    PC = 0
    DIC = 0
    finished = False
    while(not(finished)):
    
        DIC += 1
        fetch = Instruction[PC]
        if (fetch[0:32] == '00010000000000001111111111111111'):
            print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " : Deadloop. Ending program")
            finished = True
        elif (fetch[0:6] == '000000' and fetch[26:32] == '100000'): # ADD
            print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "add $" + str(int(fetch[16:21],2)) + ",$" +str(int(fetch[6:11],2)) + ",$" + str(int(fetch[11:16],2)) )
            PC += 1
            Register[int(fetch[16:21],2)] = Register[int(fetch[6:11],2)] + Register[int(fetch[11:16],2)]

        elif(fetch[0:6] == '000000' and fetch[26:32] == '100010'): # SUB
            print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "sub $" + str(int(fetch[16:21],2)) + ",$" +str(int(fetch[6:11],2)) + ",$" + str(int(fetch[11:16],2)) )
            PC += 1
            Register[int(fetch[16:21],2)] = Register[int(fetch[6:11],2)] - Register[int(fetch[11:16],2)]
        elif(fetch[0:6] == '001000'): # ADDI
            imm = int(fetch[16:32],2) if fetch[16]=='0' else -(65535 -int(fetch[16:32],2)+1)
            print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "addi $" + str(int(fetch[16:21],2)) + ",$" +str(int(fetch[6:11],2)) + ",$" + str(imm) )
            PC += 1
            Register[int(fetch[11:16],2)] = Register[int(fetch[6:11],2)] + imm
        elif(fetch[0:6] == '000100'): # BEQ
            imm = int(fetch[16:32],2) if fetch[16]=='0' else -(65535 -int(fetch[16:32],2)+1)
            print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "beq $" + str(int(fetch[6:11],2)) + ",$" +str(int(fetch[11:16],2)) + "," + str(imm) )
            PC += 1
            PC = PC + imm if (Register[int(fetch[6:11],2)] == Register[int(fetch[11:16],2)]) else PC
        elif(fetch[0:6] == '000101'): # BNE
            imm = int(fetch[16:32],2) if fetch[16]=='0' else -(65535 -int(fetch[16:32],2)+1)
            print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "bne $" + str(int(fetch[6:11],2)) + ",$" +str(int(fetch[11:16],2)) + "," + str(imm) )
            PC += 1
            PC = PC + imm if Register[int(fetch[6:11],2)] != Register[int(fetch[11:16],2)] else PC
        elif(fetch[0:6] == '000000' and fetch[26:32] == '101010'): # SLT
            print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "slt $" + str(int(fetch[16:21],2)) + ",$" +str(int(fetch[6:11],2)) + ",$" + str(int(fetch[11:16],2)) )
            PC += 1
            Register[int(fetch[16:21],2)] = 1 if Register[int(fetch[6:11],2)] < Register[int(fetch[11:16],2)] else 0
        elif(fetch[0:6] == '101011'): # SW
            #Sanity check for word-addressing 
            if ( int(fetch[30:32])%4 != 0 ):
                print("Runtime exception: fetch address not aligned on word boundary. Exiting ")
                print("Instruction causing error:", hex(int(fetch,2)))
                exit()
            imm = int(fetch[16:32],2)
            print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "sw $" + str(int(fetch[6:11],2)) + "," +str(imm + Register[int(fetch[6:11],2)] - 8192) + "(0x2000)" )
            PC += 1
            
            index = int(fetch[32-blk_offset-2:32-2],2)
            if ( Valid[index] == 0): # Cache miss
                Misses += 1
                Memory[imm + Register[int(fetch[6:11],2)] - 8192]= Register[int(fetch[11:16],2)] # Store word into memory
                Cache[index] = Register[int(fetch[11:16],2)]    # update latest value of cache
                Valid[index] = 1    # Since we have cache miss, valid bit is now 1 after cache has updated value
                Tag[index] = fetch[16:32-blk_offset-2]
            else: # Valid bit is 1, now check if tag matches
                if(Tag[index] == fetch[16:32-blk_offset-2]): # Cache hit
                    Cache[index] = Register[int(fetch[11:16],2)] 
                    Hits += 1
                else: # Tag doesnt match, cache miss
                    Misses += 1
                    Memory[imm + Register[int(fetch[6:11],2)] - 8192]  =Register[int(fetch[11:16],2)] # Store word into memory
                    Cache[index] = Register[int(fetch[11:16],2)]    # update latest value of cache
                    Tag[index] = fetch[16:32-blk_offset-2]                             # Update tag
        elif(fetch[0:6] == '100011'): # ********LOAD WORD********
            #Sanity check for word-addressing 
            if ( int(fetch[30:32])%4 != 0 ):
                print("Runtime exception: fetch address not aligned on word boundary. Exiting ")
                print("Instruction causing error:", hex(int(fetch,2)))
                exit()
            imm = int(fetch[16:32],2)
            print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "lw $" + str(int(fetch[6:11],2)) + "," +str(imm + Register[int(fetch[6:11],2)] - 8192) + "(0x2000)" )
            PC += 1
            
            # Cache access: 
            # First check cache for any hit based on valid bit and index of cache
            index = int(fetch[32-blk_offset-2:32-2],2)
            if ( Valid[index] == 0): # Cache miss
                Misses += 1
                Cache[index] = Memory[imm + Register[int(fetch[6:11],2)] - 8192] # Load memory into cache data
                Register[int(fetch[11:16],2)] = Cache[index]    # Load cache data into register 
                Valid[index] = 1    # Since we have cache miss, valid bit is now 1 after cache has updated value
                Tag[index] = fetch[16:32-blk_offset-2]
            else: # Valid bit is 1, now check if tag matches
                if(Tag[index] == fetch[16:32-blk_offset-2]): # Cache hit
                    
                    Register[int(fetch[11:16],2)] = Cache[index]
                    Hits += 1
                else: # Tag doesnt match, cache miss
                    Misses += 1
                    Cache[index] = Memory[imm + Register[int(fetch[6:11],2)] - 8192] # Load memory into cache data
                    Register[int(fetch[11:16],2)] = Cache[index]                    # Load cache data into register
                    Tag[index] = fetch[16:32-blk_offset-2]                             # Update tag

            



    print("***Finished simulation***")

    print("Registers:",Register)
    print("PC:",PC*4)
    print("DIC:",DIC)
    print("Cache misses:",Misses)
    print("Cache hits:",Hits)
    print("Cache Hit Rate:", 100*(float(Hits)/float(Hits + Misses)))
    print("Cache data:",Cache)
    




def main():
    I_file = open("i_mem.txt","r")
    Instruction = []    # array containing all instructions to execute         
    InstructionHex = []
    for line in I_file:
        if (line == "\n" or line[0] =='#'):              # empty lines,comments ignored
            continue
        line = line.replace('\n','')
        InstructionHex.append(line)
        line = format(int(line,16),"032b")
        Instruction.append(line)
        
    
    simulate(Instruction,InstructionHex)



if __name__ == "__main__":
    main()




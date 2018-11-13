
# Authors: Trung Le, Weijing Rao

# This Python program simulates a restricted subset of MIPS instructions
# and output 
# Settings: Multi-Cycle CPU, i.e lw takes 5 cycles, beq takes 3 cycles, others are 4 cycles

mem_space = 4096 # Memory addr starts from 2000 , ends at 3000.  Hence total space of 4096


def simulate(Instruction,InstructionHex,debugMode):
    print("***Starting simulation***")
    print("Settings:")
    Register = [0,0,0,0,0,0,0,0]    # initialize all values in registers to 0
    Memory = [0 for i in range(mem_space)] 
    PC = 0
    DIC = 0
    Cycle = 1
    threeCycles = 0 # frequency of how many instruction takes 3 cycles
    fourCycles = 0  #                                         4 cycles
    fiveCycles = 0  #                                         5 cycles

    finished = False
    while(not(finished)):
    
        DIC += 1
        fetch = Instruction[PC]
        if (fetch[0:32] == '00010000000000001111111111111111'):
            print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " : Deadloop. Ending program")
            finished = True

        elif (fetch[0:6] == '000000' and fetch[26:32] == '100000'): # ADD
            if(debugMode):
                print("Cycles " + str(Cycle) + ":")
                print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "add $" + str(int(fetch[16:21],2)) + ",$" +str(int(fetch[6:11],2)) + ",$" + str(int(fetch[11:16],2)) )
                print("Taking 4 cycles \n")
            PC += 1
            Cycle += 4
            fourCycles += 1
            Register[int(fetch[16:21],2)] = Register[int(fetch[6:11],2)] + Register[int(fetch[11:16],2)]
           

        elif(fetch[0:6] == '001000'):                               # ADDI
            imm = int(fetch[16:32],2) if fetch[16]=='0' else -(65535 -int(fetch[16:32],2)+1)
            if(debugMode):
                print("Cycles " + str(Cycle) + ":")
                print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "addi $" + str(int(fetch[16:21],2)) + ",$" +str(int(fetch[6:11],2)) + ",$" + str(imm) )
                print("Taking 4 cycles \n")
            PC += 1
            Cycle += 4
            fourCycles += 1
            Register[int(fetch[11:16],2)] = Register[int(fetch[6:11],2)] + imm

        elif(fetch[0:6] == '000100'):                               # BEQ
            imm = int(fetch[16:32],2) if fetch[16]=='0' else -(65535 -int(fetch[16:32],2)+1)
            if(debugMode):
                print("Cycles " + str(Cycle) + ":")
                print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "beq $" + str(int(fetch[6:11],2)) + ",$" +str(int(fetch[11:16],2)) + "," + str(imm) )
                print("Taking 3 cycles \n")
            Cycle += 3
            PC += 1
            threeCycles += 1
            PC = PC + imm if (Register[int(fetch[6:11],2)] == Register[int(fetch[11:16],2)]) else PC

        elif(fetch[0:6] == '000000' and fetch[26:32] == '101010'): # SLT
            if(debugMode):
                print("Cycles " + str(Cycle) + ":")
                print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "slt $" + str(int(fetch[16:21],2)) + ",$" +str(int(fetch[6:11],2)) + ",$" + str(int(fetch[11:16],2)) )
                print("Taking 4 cycles \n")
            Cycle += 4
            PC += 1
            fourCycles += 1
            Register[int(fetch[16:21],2)] = 1 if Register[int(fetch[6:11],2)] < Register[int(fetch[11:16],2)] else 0

        elif(fetch[0:6] == '101011'):                               # SW
            #Sanity check for word-addressing 
            if ( int(fetch[30:32])%4 != 0 ):
                print("Runtime exception: fetch address not aligned on word boundary. Exiting ")
                print("Instruction causing error:", hex(int(fetch,2)))
                exit()
            imm = int(fetch[16:32],2)
            if(debugMode):
                print("Cycles " + str(Cycle) + ":")
                print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "sw $" + str(int(fetch[6:11],2)) + "," +str(imm + Register[int(fetch[6:11],2)] - 8192) + "(0x2000)" )
                print("Taking 4 cycles \n")
            PC += 1
            Cycle += 4
            fourCycles += 1
            Memory[imm + Register[int(fetch[6:11],2)] - 8192]= Register[int(fetch[11:16],2)] # Store word into memory

        elif(fetch[0:6] == '100011'):                               # LW
            #Sanity check for word-addressing 
            if ( int(fetch[30:32])%4 != 0 ):
                print("Runtime exception: fetch address not aligned on word boundary. Exiting ")
                print("Instruction causing error:", hex(int(fetch,2)))
                exit()
            imm = int(fetch[16:32],2)
            if(debugMode):
                print("Cycles " + str(Cycle) + ":")
                print("PC =" + str(PC*4) + " Instruction: 0x" +  InstructionHex[PC] + " :" + "lw $" + str(int(fetch[6:11],2)) + "," +str(imm + Register[int(fetch[6:11],2)] - 8192) + "(0x2000)" )
                print("Taking 5 cycles \n")
            PC += 1
            Cycle += 5
            fiveCycles += 1
            Register[int(fetch[11:16],2)] = Memory[imm + Register[int(fetch[6:11],2)] - 8192] # Load memory into register
 
    print("***Finished simulation***")
    print("Total # of cycles: " + str(Cycle))
    print("Dynamic instructions count: " +str(DIC) + ". Break down:")
    print("                    " + str(threeCycles) + " instructions take 3 cycles" )
    print("                    " + str(fourCycles) + " instructions take 4 cycles" )
    print("                    " + str(fiveCycles) + " instructions take 5 cycles" )
    print("Registers: " + str(Register))
     
   


def main():
    print("Welcome to ECE366 sample MIPS_sim, choose the mode of running i_mem.txt: ")
    debugMode =True if  int(input("1 = debug mode         2 = normal execution\n"))== 1 else False

    I_file = open("i_mem.txt","r")
    Instruction = []            # array containing all instructions to execute         
    InstructionHex = []
    for line in I_file:
        if (line == "\n" or line[0] =='#'):              # empty lines,comments ignored
            continue
        line = line.replace('\n','')
        InstructionHex.append(line)
        line = format(int(line,16),"032b")
        Instruction.append(line)
        
    
    simulate(Instruction,InstructionHex,debugMode)



if __name__ == "__main__":
    main()




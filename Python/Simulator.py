
# Authors: Trung Le, Wenjing Rao
# This program is a simulator packed with both assembler and disassembler.
# Simulator has 2 modes:
#            Debug mode:  Execute program every # steps and
#                         output the state of each reg, and PC
#            Normal mode: Execute program all at once

def disassemble(I,Nlines):
    print("ECE366 Fall 2018 ISA Design: Disassembler")
    print("")
    #print(I)

    for i in range(Nlines):
        fetch = I[i]
        print(fetch)
        if(fetch[0:2]=="00"):   # init
            Rx = int(fetch[2:4])
            imm = int(fetch[4:8],2)
            print("init R"+str(Rx) + "," + str(imm))
        elif(fetch[0:4]=="0100"):   # load
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("load R" + str(Rx) +",(R" + str(Ry) + ")")
        elif(fetch[0:4]=="0101"):   # store
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("stre R" + str(Rx) +",(R" + str(Ry) + ")")
        elif(fetch[0:4]=="0110"):   # add
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("add R" + str(Rx) +",R" + str(Ry) )
        elif(fetch[0:4]=="0111"):   # sub
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("sub R" + str(Rx) +",R" + str(Ry) )
        elif(fetch[0:4]=="1000"):   # addi
            Rx = int(fetch[4:6],2)
            imm = int(fetch[6:8],2)
            print("addi R" + str(Rx) +"," + str(imm) )
        elif(fetch[0:4]=="1001"):   # xor
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("xor R" + str(Rx) +",R" + str(Ry) )
        elif(fetch[0:4]=="1010"):   # sltR0
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("sltR0 R" + str(Rx) +",R" + str(Ry) )
        elif(fetch[0:4]=="1011"):   # bezR0
            Rx = int(fetch[4:8],2) 
            if ( Rx  > 7 ):
                Rx = Rx - 16
            print("bezR0 " + str(Rx) )
        elif(fetch[0:4]=="1100"):   # jump
            Rx = int(fetch[4:8],2) 
            if ( Rx  > 7 ):
                Rx = Rx - 16
            print("jump " + str(Rx) )
        print()

def assemble(I,Nlines):
    print("ECE366 Fall 2018 ISA Design: Assembler")
    print("")
    
    for i in range(Nlines):
        fetch = I[i]
        print()
        print(fetch)
        fetch = fetch.replace("R","")
        if (fetch[0:4] == "init"):
            fetch = fetch.replace("init ","")
            fetch = fetch.split(",")
            R = format(int(fetch[0]),"02b")
            imm = format(int(fetch[1]),"04b")
            op = "00"
            print(op + " " + R + " " + imm)
        elif (fetch[0:4] == "addi"):
            fetch = fetch.replace("addi ","")
            fetch = fetch.split(",")
            R = format(int(fetch[0]),"02b")
            imm = format(int(fetch[1]),"02b")
            op = "1000"
            print(op + " " + R + " " + imm)
        elif (fetch[0:4] == "add "):
            fetch = fetch.replace("add ","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "0110"
            print(op + " " + Rx + " " + Ry)

        elif (fetch[0:4] == "sub "):
            fetch = fetch.replace("sub ","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "0111"
            print(op + " " + Rx + " " + Ry)
        elif (fetch[0:4] == "xor "):
            fetch = fetch.replace("xor ","")
            fetch = fetch.split(",")      
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "1001"
            print(op + " " + Rx + " " + Ry)
            
        elif (fetch[0:4] == "load"):
            fetch = fetch.replace("load ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "0100"
            print ( op + " " + Rx + " " + Ry)
            
        elif (fetch[0:4] == "stre"):
            fetch = fetch.replace("stre ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "0101"
            print ( op + " " + Rx + " " + Ry)
        elif (fetch[0:4] == "slt0"):  # why "slt0" instead of "sltR0" ? 
                                    # --> because all the 'R' is deleted at fetch to make things simplier. 
            fetch = fetch.replace("slt0 ","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "1010"
            print ( op + " " + Rx + " " + Ry)
            
        elif (fetch[0:4] == "bez0"):
            fetch = fetch.replace("bez0 ","")
            fetch = fetch.split(",")
            imm = int(fetch[0])
            
            if ( imm < 0):
                imm = format(15 - abs(imm) + 1,"04b")
            else:
                imm = format(imm,"04b")
            op = "1011"
            print(op + " " + imm)
            
        elif (fetch[0:4] == "jump"):
            fetch = fetch.replace("jump ","")
            fetch = fetch.split(",")
            imm = int(fetch[0])
            if ( imm < 0):
                imm = format(15 - abs(imm) + 1,"04b")
            else:
                imm = format(imm,"04b")
            op = "1100"
            print(op + " " + imm)
        elif(fetch[0:6] == "finish"):
            op = "11111111"
            print(op)


def simulate(I,Nsteps):
    print("ECE366 Fall 2018 ISA Design: Simulator")
    print()
    PC = 0              # Program-counter
    DIC = 0
    Reg = [0,0,0,0]     # 4 registers, init to all 0
    Memory = [0 for i in range(10)] # data memory, 10 spaces all init to 0.
    print("******** Simulation starts *********")
    finished = False
    while(not(finished)):
        fetch = I[PC]
        DIC += 1
        print(fetch)
        fetch = fetch.replace("R","")       # Delete all the 'R' to make things simpler
        if (fetch[0:4] == "init"):
            fetch = fetch.replace("init ","")
            fetch = fetch.split(",")
            R = int(fetch[0])
            imm = int(fetch[1])
            Reg[R] = imm
            PC += 1
        elif (fetch[0:4] == "addi"):
            fetch = fetch.replace("addi ","")
            fetch = fetch.split(",")
            R = int(fetch[0])
            imm = int(fetch[1])
            Reg[R] = Reg[R] + imm
            PC += 1
        elif (fetch[0:4] == "add "):
            fetch = fetch.replace("add ","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] + Reg[Ry]
            PC += 1
        elif (fetch[0:4] == "sub "):
            fetch = fetch.replace("sub ","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] - Reg[Ry]
            PC += 1
        elif (fetch[0:4] == "xor "):
            fetch = fetch.replace("xor ","")
            fetch = fetch.split(",")      
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] ^ Reg[Ry]
            PC += 1
        elif (fetch[0:4] == "load"):
            fetch = fetch.replace("load ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Memory[Ry]
            PC += 1
        elif (fetch[0:4] == "stre"):
            fetch = fetch.replace("stre ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Memory[Ry] = Reg[Rx]
            PC += 1
        elif (fetch[0:4] == "slt0"):  # why "slt0" instead of "sltR0" ? 
                                    # --> because all the 'R' is deleted at fetch to make things simplier. 
            fetch = fetch.replace("slt0 ","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            if( Reg[Rx] < Reg[Ry] ):
                Reg[0] = 1
            else:
                Reg[0] = 0
            PC += 1
        elif (fetch[0:4] == "bez0"):
            fetch = fetch.replace("bez0 ","")
            fetch = fetch.split(",")
            imm = int(fetch[0])
            if ( Reg[0] == 0):
                PC = PC + imm
            else:
                PC += 1
        elif (fetch[0:4] == "jump"):
            fetch = fetch.replace("jump ","")
            fetch = fetch.split(",")
            imm = int(fetch[0])
            PC = PC + imm
        elif(fetch[0:6] == "finish"):
            finished = True
        if ( (DIC % Nsteps) == 0):
            print("Registers R0-R3: ", Reg)
            print("Memory: ",Memory)
            print()
        
    print("******** Simulation finished *********")
    print("Dynamic Instr Count: ",DIC)
    print("Registers R0-R3: ",Reg)
    print("Memory :",Memory)


def main():
    input_file = open("input.txt","r")
    debug_mode = False  # is machine in debug mode?  
    Nsteps = 3          # How many cycle to run before output statistics
    Nlines = 0          # How many instrs total in input.txt  
    Instruction = []    # all instructions will be stored here
    mode = 1            # 1 = Simulation 
                        # 2 = disassembler
                        # 3 = assembler
    for line in input_file:
        if (line == "\n" or line[0] =='#'):              # empty lines,comments ignored
            continue
        line = line.replace("\n","")
        Instruction.append(line)                        # Copy all instruction into a list
        Nlines +=1

    if(mode == 1):   # Check wether to use disasembler or assembler or simulation 
        simulate(Instruction,Nsteps)
    elif(mode == 2):
        disassemble(Instruction,Nlines)
    else:
        assemble(Instruction,Nlines)

    
    
    
if __name__ == "__main__":
    main()

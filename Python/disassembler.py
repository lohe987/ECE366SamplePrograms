# Authors: Trung Le, Wenjing Rao

# processHex convert a MIPS instruction of Hex into binary 
# return result as a string
def processHex(line):
    string = ''
    for i in range(2,10):
        string = string + ' ' + format(int(line[i:i+1],16),'04b')
        # Explaination:
        # ---line[i:i+1]                       takes each hex character as input
        # ---int(line[i:i+1],16)               convert hex character into integer of base 16
        # ---format(int(line[i:i+1],16))       format integer into 4-bit binary
          
    return string


# processAddr takes an integer (addr) , and converts it into an 8-digit hex string
def processAddr(addr):
    string =format(addr,'08x')
    return string

# processBin explains what a MIPS instruction (in binary) is doing
# param: addr = (integer form) current instruction address (=PC)
#        binary = a MIPS instruction in machine code binary
# output: 
#       Print out each instruction's functionality, current PC, next PC
# Supported instrs:
#   ADD,ADDI,SUB,XOR,SLT, BEQ, BNE, J

def processBin(addr,binary):
    cur_PC = addr
    next_PC= 0
    binary = binary.replace(' ','')
    if(binary[0:6] == "000000"):    # ALU instructions
        funct = binary[26:32]       # slice the funct portion of instruction
        rs = str(int(binary[6:11],2))   # slice the rs,rt,rd
        rt = str(int(binary[11:16],2))
        rd = str(int(binary[16:21],2))
        op = ""
        if  (funct == "100000"):    # ADD instr
            op = "add"
            next_PC = cur_PC + 4
        elif (funct == "100010"):   # SUB instr
            op = "sub"
            next_PC = cur_PC + 4
        elif (funct == "100110"):   # XOR instr
            op = "xor"
            next_PC = cur_PC + 4
        elif (funct == "101010"):  # SLT instr
            op = "slt"
            next_PC = cur_PC + 4
        else:
            print("Instruction not yet supported")
            exit()
        print("Instruction: "+op + " $" + rd+",$"+rs+",$"+rt)
        print("next_PC = 0x"+ format(next_PC,'08x'))

    elif(binary[0:6] == "001000"):  # ADDI instr
        rs = str(int(binary[6:11],2))
        rt = str(int(binary[11:16],2))
        imm = int(binary[16:32],2)
        op = "addi"
        next_PC = cur_PC + 4
        if(binary[16]=='1'):        # negative number processing
            imm = 65535 - imm + 1
            imm = str(-imm)
        else:
            imm = str(imm)
        
        print("Instruction: "+op + " $" + rt +",$"+rs+","+imm)
        print("next_PC = 0x"+ format(next_PC,'08x'))

    elif(binary[0:6] == "000100"): # BEQ instr
        rs = str(int(binary[6:11],2))
        rt = str(int(binary[11:16],2))
        imm = int(binary[16:32],2)
        if(binary[16]=='1'):        # negative imm part processing
            imm = 65535 - imm + 1
            imm = str(-imm)
        else:
            imm = str(imm)

        op = "beq"
        
        print("Instruction: "+op + " $" + rs +",$"+rt+","+imm)
        print("If $"+rs+" == $"+rt+", then next_PC = 0x"+ format(cur_PC+(int(imm)<<2)+4,'08x'))
        print("Else next_PC = 0x", format(cur_PC + 4,'08x'))

    elif(binary[0:6] == "000101"): # BNE instr
        rs = str(int(binary[6:11],2))
        rt = str(int(binary[11:16],2))
        imm = int(binary[16:32],2)
        if(binary[16]=='1'):        # negative imm part processing
            imm = 65535 - imm + 1
            imm = str(-imm)
        else:
            imm = str(imm)
       
        op = "bne"
        
        print("Instruction: "+op + " $" + rs +",$"+rt+","+ imm)
        print("If $"+rs+" != $"+rt+", then next_PC = 0x"+ format(cur_PC+(int(imm)<<2)+4,'08x'))
        print("Else next_PC = 0x", format(cur_PC + 4,'08x'))

    elif(binary[0:6] == "000010"): # JUMP instr
        offset = str(int(binary[6:32],2))

        op = "j"

        print("Instruction: "+op +" " + offset)
        print("next_PC = 0x"+ format((int(offset)<<2),'08x'))
    
    print()




input_file = open("MIPS_hex.txt", "r")
#output_file = open("MIPS_machine_code.txt","w")
print("ECE366 Fall 2018 mini MIPS disassembler")
print("----------")
print("ADDRESS   :  BINARY  ")

addr = 0
for line in input_file:
    if (line == "\n"):              # empty lines ignored
        continue

    
    if(line[0:2] == '0x'):
        address = processAddr(addr) # convert from int to hex in form of string
        binary  = processHex(line)  # process each line of hex to output binary
        print( '0x' + address + ': ' +  binary )
        
        processBin(addr,binary)
        addr = addr + 4
    

input_file.close()
#output_file.close()

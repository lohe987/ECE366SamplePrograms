#ECE 366 Sample Program 1
# Author: Trung Le,  Wenjing Rao
#
#This program checks the numbers in memory (array1 with 15 words) 
#and stores back the absolute value of each number in array1.


# setting: memory configuration -> Compact (Text section begins at 0, Data begins at 0x2000)
.data
	array1: .word -1, -2, 3, 5, -6, 0, 7, -2, 4, -7, -10, 1, -9, 11, 14
	

.text
		addi $t0,$0,0x2000		# 'array1' starts at 0x2000, use $t0 for base address
		addi $t1,$0,15			# $t1 as counter: 15, 14, 13, ...1, 0
		
begin:
		lw $a0,0($t0)			# Load each number in 'array1' to $a0
		slt $a1, $a0, $0		# Compare if number < 0   ( NEGATIVE ) , then convert to absolute number
						# Otherwise skip
		bne $a1, $0, convert		
_convert:	sw $a0,0($t0)			# Store number back to array
		addi $t0,$t0,4			# increment array1's base address
		addi $t2,$t2,1			# increment count
		beq $t1,$t2,exit		# Are we finished?   If so exit, else loop back
		j begin
	
convert: 
		sub $a0,$0, $a0
		j _convert

exit:
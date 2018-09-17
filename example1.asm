#ECE 366 Sample Program 1
# Author: Trung Le,  Wenjing Rao
#
#This program checks the numbers in memory (array1 with 15 words) 
#and stores back the absolute value of each number in array1.


# setting: memory configuration -> 
# Compact (Text section begins at 0, Data begins at 0x2000)
.data
	array1: .word -1, -2, 3, 5, -6, 0, 7, -2, 4, -7, -10, 1, -9, 11, 14
	

.text
		addi $t0,$0,0x2000		# array1 starts @ 0x2000, $t0 (=$9) for base address
		addi $t1,$0,15			# $t1 as counter: 15, 14, 13, ...1, 0
		
begin:
		lw $s0,0($t0)			# Load each number in 'array1' to $s0
		slt $s1, $s0, $0		# Compare if number < 0   ( NEGATIVE )				
		bne $s1, $0, convert		# if so go to "convert" 

_convert:	sw $s0,0($t0)			# Store number back to array
		addi $t0,$t0,4			# increment address by 4 to get ready for the next number
		subi $t1,$t1,1			# decrement counter
		beq $t1,$0,exit			# Are we finished?   If so (counter == 0) goto exit 
		j begin				# else loop back

convert: 
		sub $s0,$0, $s0
		j _convert

exit:		j exit				# program finished: dead loop 
						# to stay here forever, prevent PC from +4

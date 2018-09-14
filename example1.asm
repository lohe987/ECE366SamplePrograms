#ECE 366 Sample Program 1
# Author: Trung Le,  Wenjing Rao
#
#This program loads numbers in array ( total of 15 elements) and calculate
#absolute value of each, then proceed to store back into array
.data
	array1: .word -1, -2, 3, 5, -6, 0, 7, -2, 4, -7, -10, 1, -9, 11, 14
	

.text
		addi $t0,$t0,0x10010000		# 'array1' starts at 0x10010000.   Store base address to $t0
		addi $t1,$t1,15			# There are total 15 elements in array1.   Store count to $t1
		
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
	
	
exit: 		li $v0,10			# End program execution
		syscall				# 
	
	
	
	
	
	
	
	
convert: 
		sub $a0,$0, $a0
		j _convert

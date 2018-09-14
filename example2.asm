#ECE 366 Sample Program 2
# Author: Trung Le,  Wenjing Rao

#	This program loads 2 numbers from data memory (say, X and Y ) and find the
#	modulo of X%Y by substracting operation

.data 
		array1: .word 2, 5		# X is first number,  Y is second number in the array
	
.text
		addi $t0, $t0, 0x10010000	# Base address of 'array1' stored in $t0
		lw $t1, 0($t0)			# $t1 stores X
		lw $t2, 4($t0)			# $t2 stores Y
loop:	
		sub $t3,$t1,$t2			# t3 = t1 - t2 = X - Y
		slt $a0, $t3,$0			# If X-Y < 0 , then we found the X%Y result
		bne $a0,$0, finish
		sub $t1,$t1,$t2			# Else, we have not found the result yet, continue substracting
						# until finished
		j loop


exit:		li $v0,10			# End program execution
		syscall	

				
finish:		sw $t1,8($t0)
		j exit


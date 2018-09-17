# ECE 366 Sample Program 2
# Author: Trung Le,  Wenjing Rao
#
#	This program loads 2 numbers from data memory (say, X and Y ) 
# 	finds the modulo of X%Y by substracting operation
#	and store back the result into data memory (Z).

.data 
		x: .word 240	# Mem[0x2000]
		y: .word 42	# Mem[0x2004]
		z: .word -1	# Mem[0x2008]
	
.text
		addi $t0, $t0, 0x2000		# address of x = 0x2000 => $t0
		lw $t1, 0($t0)			# now $t1 stores X (@ Mem[0x2000])
		lw $t2, 4($t0)			# now $t2 stores Y (@ Mem[0x2004])
loop:	
		sub $t3,$t1,$t2			# $t3 = X - Y
		slt $s0, $t3,$0			# If X-Y < 0 , then we should stop
		bne $s0,$0, done
		add $t1,$t3,$0			# Else, update X = X-Y 
		j loop				# continue substracting Y

done:		sw $t1,8($t0)			# current X is solution => Mem[0x2008]
exit:		j exit				# loop forever to stop here


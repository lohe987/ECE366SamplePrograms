#ECE 366 Sample Program 2
# Author: Trung Le,  Wenjing Rao

#	This program loads 2 numbers from data memory (say, X and Y ) 
# 	finds the modulo of X%Y by substracting operation
#	and store back the result into data memory (Z).

.data 
		x: .word 240
		y: .word 42	
		z: .word -1	
	
.text
		addi $t0, $t0, 0x2000		# address of x = 0x2000 => $t0
		lw $t1, 0($t0)			# now $t1 stores X (@ Mem[0x2000])
		lw $t2, 4($t0)			# now $t2 stores Y (@ Mem[0x2004])
loop:	
		sub $t3,$t1,$t2			# t3 = t1 - t2 = X - Y
		slt $s0, $t3,$0			# If X-Y < 0 , then we found the X%Y result
		bne $s0,$0, done
		sub $t1,$t1,$t2			# Else, we have not found the result yet, continue substracting
						# until finished
		j loop


exit:		j exit

				
done:		
		sw $t1,8($t0)			# z is at Mem[0x2008]
		j exit


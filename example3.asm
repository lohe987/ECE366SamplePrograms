#ECE 366 Sample Program 3
# Author: Trung Le,  Wenjing Rao

#	This program contains 3 arrays: A , B, C
#	It calculates C[i] = A[i] XOR B[i]	
#	and stores back into array C

.data
	A:	.word	0, -1, 0xFFFF0000, 0x0F0F0F0F, 0x33333333, 0xCCCCCCCC, 
			0x66666666, 0xFFFF, 0x99999999
	B:	.word 	5,8,-2,-3215,433,77,12,-85,2
	C:	.word	-1, -2, -3, -4, -5, -6, -7, -8, -9
	D: 	.word	0xAABBCCDD	# marker of boundary. 

.text
	addi $t0,$t0,0x2000		# Base address of array A
	addi $t1,$t0,36			# Base address of array B  
	addi $t2,$t0,72			# Base address of array C
	addi $t3,$0,9			# init counter = 9 (# in each array) 	

loop:	
	lw $s0,0($t0)			# Load number of array A[i] into $s0
	lw $s1,0($t1)			# Load number of array B[i] into $s1
	xor $s3,$s1,$s2			# C[i] = A[i] XOR B[i]
	sw $s3,0($t2)			# store C[i] back into array

	addi $t0,$t0,4			# Increment i for A[i], B[i], C[i]
	addi $t1,$t1,4
	addi $t2,$t2,4
	
	subi $t3,$t3,1			# Decrement counter
	beq $t3,$0,exit
	j loop


exit:	j exit			# deadloop after finishing

#ECE 366 Sample Program 2
# Author: Trung Le,  Wenjing Rao

#	This program contains 3 arrays: A , B, C
#	It calculates C[i] = A[i] XOR B[i]	
#	and stores back into array C

.data
	A:	.word	1,2,7,9,11,713,69,0,-1
	B:	.word 	5,8,-2,-3215,433,77,12,-85,2
	C:	.word	-1, -2, -3, -4, -5, -6, -7, -8, -9
	D: 	.word	0xAABBCCDD	# marker of boundary. This SHOULD NOT BE MODIFIED

.text
	addi $t0,$t0,0x2000		# Base address of array A
	addi $t1,$t0,36			# Base address of array B  
	addi $t2,$t0,72			# Base address of array C
	addi $t3,$0,9			# Each array contains 9 elements each	

loop:	
	lw $s0,0($t0)			# Load number of array A into $a0
	lw $s1,0($t1)			# Load number of array B into $a1
	xor $s3,$s1,$s2			# C = A XOR B
	sw $s3,0($t2)			# store C back into array
	subi $t3,$t3,1			# Decrement count
	addi $t0,$t0,4			# Increment address of A,B and C
	addi $t1,$t1,4
	addi $t2,$t2,4
	
	beq $t3,$0,exit
	j loop


exit:	j exit			# deadloop after finishing

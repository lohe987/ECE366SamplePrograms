
.data
	T: .word 0
	
.text
loop:	
	
	addi $2,$3,-1
	sw $2,T 
	sw $2,T+4
	sw $2,T+8
	sw $2,T+12
	sw $2,T+16
	sw $2,T+20
	sw $2,T+24
	sw $2,T+28
	sub $6,$2,$5
	add $4,$6,$6
	lw $5,T+8
	addi $5,$5,20
	sw $5,T+4
	lw $5,T+8
        slt $5,$2,$3
	addi $2,$3,-1
	sub $7,$5,$2
	addi $5,$2,-25
	sw $2,T+20
	lw $2,T+4
	lw $3,T+8
	lw $4,T+12
	lw $4,T+16
	lw $5,T+20
	lw $6,T+24
	lw $7,T+28
	
label:  beq $0,$0,label
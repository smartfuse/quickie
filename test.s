li $t1, 23
li $t2, 7
slt $t3, $t1, $t2 
beq $t3, $0, compute
j return
	
compute: sub $t1, $t1, $t2  
slt $t3, $t1, $t2  
beq $t3, $0, compute
j return

return: disp $t1
add $t1, $t2, $t3
disp $t2
disp $t3
disp $t1
addi $t1, $t2, 1
disp $t1
and $t2, $t1, $t1
disp $t2
andi $t2, $t1, 0
disp $t2
ori $t2, $t2, 256
disp $t2
or $t2, $t3, $t1
disp $t2
li $t0, 3
li $t1, 2
mult $t2, $t0, $t1
disp $t2
jal hi
disp $t2
j exit
hi: disp $0
jr $ra
exit: disp $t1


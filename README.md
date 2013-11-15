quickie
=======

quickie is a MIPS runtime written in python. it lets you run MIPS code on your computer. it runs on any machine that has python 3.

<b>introduction to using quickie:</b>
all data in quickie is word addressed. as this is written in python, each word is of unlimited size. also all operations are signed.

<b>valid instructions:</b>

addi	$r1, $r2, imm
adds the value in $r2 to the immediate and stores it in $r1.

add	$r1, $r2, $r3
adds the value in $r2 to the value in $r3 and stores it in $r1.

andi	$r1, $r2, imm
performs logical and between $r2 and the immediate and stores it in $r1.

and	$r1, $r2, $r3
performs logical and between $r2 and $r3 and stores it in $r1.

ori	$r1, $r2, imm
performs logical or between $r2 and the immediate and stores it in $r1.

or	$r1, $r2, $r3
performs logical or between $r2 and $r3 and stores it in $r1.

beq	$r1, $r2, label
if $r1 and $r2 are equal, then we jump to the label.

bne	$r1, $r2, label
if $r1, and $r2 are not equal, then we jump to the label.

slt	$r1, $r2, $r3
if the value in $r2 is less than the value in $r3, then $r1 is set to 1, otherwise $r1 is set to 0.

slti	$r1, $r2, imm
if the value in $r2 is less than the immediate, then $r1 is set to 1, otherwise $r1 is set to 0.

sub	$r1, $r2, $r3
subtracts the value in $r3 from the value in $r2, then stores it in $r1.

mult	$r1, $r2, $r3
multiplies the value in $r2 by the value in $r3 and stores it in $r1.

lw	$r1, offset($r2)
loads the word from memory specified by $r2 + offset and stores it in $r1. note: everything is word-addressed.

sw	$r1, $r2
stores $r1 into memory specified by $r2 + offset. note: everything is word-addressed.

sll	$r1, $r2, $r3
shifts the value in $r2 left by the value in $r3 and stores it in $r1.

sra	$r1, $r2, $r3
does an unsigned shift to the right with the value in $r2 and $r3 and stores it in $r1.

li	$r1, imm
loads the immediate into $r1.

j	label
jumps to the label.

disp	$r1
prints the value in $r1.

jal	label
jumps to the label and stores the return address in $31.

jr	$r1
jumps to the address specified in $r1.

<b>registers: </b>
all standard 32 registers are supported. names like $t0, $s0, and $ra are also supported. the zero register is protected (read-only and always 0).

<b>usage: </b>
quickie is a python script so run it with:
<code>python3 quickie.py</code>

this will run it in interactive mode where code is entered manually. to have quickie read code from a file, run it with the filename:
<code>python3 quickie.py filename</code>

you can also add "-v" to the end of it to print out all the registers and memory like
<code>python3 quickie.py filename -v</code>
or 
<code>python3 quickie.py -v</code>

</b>go bears!</b>

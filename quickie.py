#! /usr/bin/env python
# quickie 1.0
# MIPS Runtime Evironment in Python

import sys
import os

register_map = {
"zero": 0,
"at" : 1,
"v0" : 2,
"v1" : 3,
"a0" : 4,
"a1" : 5,
"a2" : 6,
"a3" : 7,
"t0" : 8,
"t1" : 9,
"t2" : 10,
"t3" : 11,
"t4" : 12,
"t5" : 13,
"t6" : 14,
"t7" : 15,
"s0" : 16,
"s1" : 17,
"s2" : 18,
"s3" : 19,
"s4" : 20,
"s5" : 21,
"s6" : 22,
"s7" : 23,
"t8" : 24,
"t9" : 25,
"k0" : 26,
"k1" : 27,
"gp" : 28,
"sp" : 29,
"fp" : 30,
"ra" : 31
}

class quickie_evironment:
    def __init__(self):
        self.registers = [0] * 32
        self.memory = [0] * 256

global_env = quickie_evironment()

def exec_mips(code, evironment = global_env):
    assert type(evironment) != None, "quickie requires a valid evironment"
    labels = dict()
    instructions = code.split("\n")
    for i in range(len(instructions)):
        element = instructions[i]
        comment = element.find("#")
        if comment != -1:
            instructions[i] = element[:comment]

            
    instructions = list(filter(lambda s: s.strip() != "", instructions))
    for i in range(len(instructions)):
        element = instructions[i]
        label = element.find(":")
        if label != -1:
            labels[element[:label].strip()] = i
            instructions[i] = element[label + 1:]

    for i in range(len(instructions)):
        element = instructions[i]
        for label in labels:
            if element.find(label) != -1 and element.find("beq") == -1 and element.find("bne") == -1:
                instructions[i] = element.replace(label, str(labels[label]))
            if element.find(label) != -1 and element.find("beq") != -1 or element.find("bne") != -1:
                instructions[i] = element.replace(label, str(labels[label] - i - 1)) 

    exit = False
    program_counter = 0
    return_value = None
    if program_counter == len(instructions):
        return None
    while not exit:
        instruction = instructions[program_counter] 
        instruction = instruction + " "
        instruction = instruction.lstrip()
        function_marker = min(instruction.find(" "), instruction.find("\t"))
        if instruction.find(" ") == -1:
           function_marker = instruction.find("\t")
        if instruction.find("\t") == -1:
            function_marker = instruction.find(" ")  
        if instruction.find(" ") == -1 and instruction.find("\t") == -1:
            print("error in line " + str(program_counter + 1) + ".")  
            break
        function = instruction[0:function_marker]
        if function.find("$") != -1 or function.find(",") != -1:
            print("error in line " + str(program_counter + 1) + ".")   
            break
        function = function.strip()
        instruction = instruction[function_marker:]
        instruction = instruction.lstrip()
        if function != "jal" and function != "jr" and function != "j" and function != "disp":
            arg1_marker = instruction.find(",")
            arg1 = instruction[:arg1_marker]
            arg1 = arg1.strip()
            instruction = instruction[arg1_marker + 1:]
            instruction = instruction.lstrip()
            arg2_marker = instruction.find(",")
            arg2 = instruction[:arg2_marker]
            arg2 = arg2.strip()
            instruction = instruction[arg2_marker + 1:]
            instruction = instruction.lstrip()
            arg3 = instruction.strip()

            if function == "addi":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = evironment.registers[arg2] + arg3
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "add":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                arg3 = arg3.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                if arg3 in register_map:
                    arg3 = register_map[arg3]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = evironment.registers[arg2] + evironment.registers[arg3]
                return_value = (evironment.registers[2], evironment.registers[3])


            if function == "andi":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = evironment.registers[arg2] & arg3
                return_value = (evironment.registers[2], evironment.registers[3])
 
            if function == "and":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                arg3 = arg3.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                if arg3 in register_map:
                    arg3 = register_map[arg3]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = evironment.registers[arg2] & evironment.registers[arg3]
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "ori":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = evironment.registers[arg2] | arg3
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "or":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                arg3 = arg3.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                if arg3 in register_map:
                    arg3 = register_map[arg3]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = evironment.registers[arg2] | evironment.registers[arg3]
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "beq":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                boolean = evironment.registers[arg1] == evironment.registers[arg2]
                return_value = (evironment.registers[2], evironment.registers[3])
                if boolean and program_counter + arg3 + 1< len(instructions):
                    program_counter = program_counter + 1 + arg3
                    continue

            if function == "bne":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                boolean = evironment.registers[arg1] != evironment.registers[arg2]
                return_value = (evironment.registers[2], evironment.registers[3])
                if boolean and program_counter + arg3 + 1< len(instructions):
                    program_counter = program_counter + 1 + arg3
                    continue

            if function == "slt":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                arg3 = arg3.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                if arg3 in register_map:
                    arg3 = register_map[arg3]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = int(evironment.registers[arg2] < evironment.registers[arg3])
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "slti":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = int(evironment.registers[arg2] < arg3)
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "sub":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                arg3 = arg3.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                if arg3 in register_map:
                    arg3 = register_map[arg3]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = evironment.registers[arg2] - evironment.registers[arg3]
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "mult":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                arg3 = arg3.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                if arg3 in register_map:
                    arg3 = register_map[arg3]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = evironment.registers[arg2] * evironment.registers[arg3]
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "lw":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = evironment.memory[evironment.registers[arg2]]
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "sw":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.memory[evironment.registers[arg2]] = evironment.registers[arg1]  
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "sll":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                arg3 = arg3.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                if arg3 in register_map:
                    arg3 = register_map[arg3]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = evironment.registers[arg2] << evironment.registers[arg3]
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "sra":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                arg3 = arg3.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                if arg3 in register_map:
                    arg3 = register_map[arg3]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    arg3 = int(arg3)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break 
                evironment.registers[arg1] = evironment.registers[arg2] >> evironment.registers[arg3]
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "li":
                arg1 = arg1.strip("$")
                arg2 = arg2.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                if arg2 in register_map:
                    arg2 = register_map[arg2]
                try:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                evironment.registers[arg1] = arg2
                return_value = (evironment.registers[2], evironment.registers[3])
            
        else:
            arg1 = instruction.strip()
            if function == "j":
                try:
                    arg1 = int(arg1)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                return_value = (evironment.registers[2], evironment.registers[3])
                if arg1 < len(instructions) and arg1 >= 0:
                    program_counter = arg1
                    continue
    
            if function == "disp":
                arg1 = arg1.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                try:
                    arg1 = int(arg1)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                print(evironment.registers[arg1])
                return_value = (evironment.registers[2], evironment.registers[3])

            if function == "jal":
               try:
                   arg1 = int(arg1)
               except Exception as e:
                   print("error in line " + str(program_counter + 1) + ".")  
                   break  
               return_value = (evironment.registers[2], evironment.registers[3])
               if arg1 < len(instructions) and arg1 >= 0:
                   evironment.registers[31] = program_counter + 1
                   program_counter = arg1
                   continue

            if function == "jr":
                arg1 = arg1.strip("$")
                if arg1 in register_map:
                    arg1 = register_map[arg1]
                try:
                   arg1 = int(arg1)
                except Exception as e:
                    print("error in line " + str(program_counter + 1) + ".")  
                    break  
                return_value = (evironment.registers[2], evironment.registers[3])
                if evironment.registers[arg1] < len(instructions) and evironment.registers[arg1] >= 0:
                    program_counter = evironment.registers[arg1]
                    continue

        evironment.registers[0] = 0
        if program_counter + 1 < len(instructions):
            program_counter = program_counter + 1
        else:
            exit = True
    return return_value
     
args = sys.argv
verbose = False 

if len(args) > 1 and args[1] == "-v":
    verbose = True

if len(args) == 2 and args[1] == "-?":
    os.system("clear")
    print("\nquickie\n\nrun your MIPS code with quickie. quickie runs in interactive mode (where code is entered manually) by default. to make quickie run code from a file put the filename as the first command line argument. in addition, you can also make quickie print out the values of registers and memory in both interactive and file mode by adding a \"-v\" option at the end.\n\nexamples:\npython3 quickie.py file.s\npython3 quickie.py file.s -v\npython3 quickie.py\npython3 quickie.py -v\n")
elif len(args) == 1 or verbose:
    while True:
        os.system("clear")
        print("\nquickie\n\nenter code below. then press ctrl-d twice to run or press ctrl-c to exit.\n")
        code = sys.stdin.read()
        print("\nrunning code. output displayed below. \n\n")
        env = quickie_evironment()
        return_values = exec_mips(code, env)
        if return_values == None:
            print("no return value")
        elif verbose:
            registers = env.registers
            memory = env.memory
            print("\nREGISTERS")
            for i in range(len(registers)):
                print(str(i) + "\t" + str(registers[i]))
            print("\n")
            print("MEMORY")
            for i in range(len(memory)):
                print(str(i) + "\t" + str(memory[i])) 
            print("\n")
        else:
            print("\nv0 = " + str(return_values[0]))
            print("v1 = " + str(return_values [1]))
            print("\n")
        input("press enter to continue")
else:
    os.system("clear")
    print("\nquickie\n\nrunning code. output displayed below. \n\n")
    if len(args) > 2 and args[2] == "-v":
        verbose = True
    env = quickie_evironment()
    return_values = exec_mips(open(args[1], "r").read(), env)
    if return_values == None:
        print("no return value")
    elif verbose:
        registers = env.registers
        memory = env.memory
        print("\nREGISTERS")
        for i in range(len(registers)):
            print(str(i) + "\t" + str(registers[i]))
        print("\n")
        print("MEMORY")
        for i in range(len(memory)):
            print(str(i) + "\t" + str(memory[i])) 
        print("\n")
    else:
        print("\nv0 = " + str(return_values[0]))
        print("v1 = " + str(return_values [1]))
        print("\n")
        	

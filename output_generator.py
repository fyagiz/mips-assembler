from instructions import instruction_table
from instructions import pseudo_table
from registers import register_table
from label import label_list
from os import _exit as exit
import binary_handle

output = list()

def decode(instructions):

    # Check the assembler start batch mod or not.
    # If Is it batch mode this if block will be executed.
    if type(instructions) is list:
        # Decode the instructions by one by
        for i in instructions:
            flag = 0
            # Check insruction exist in instruction table.
            if i[0] in instruction_table:
                flag = 1
            # Check instruction exist in pseudo instruction table.
            elif i[0] in pseudo_table:
                flag = 2
            # If the instruction not found set the flag to -1.
            else:
                flag = -1
            # If instruction is real instruction.
            if flag == 1:
                ins_type = instruction_table[i[0]]
                if ins_type[0] == "R":
                    r_type_decoder(i, ins_type)
                elif ins_type[0] == "I":
                    i_type_decoder(i, ins_type)
            # If instruction is pseudo instruction.
            elif flag == 2:
                print("Pseudo!")
            # If instruction is not found.
            else:
                # If the Instruction not found, exit.
                print("{} not found!".format(i[0]))
                print("Available instructions: ")
                print(instruction_table.keys())
                print("Available pseudo instructions: ")
                print(pseudo_table.keys())
                print("Exiting...")
                exit(1)
    # Execute these block if the program runs interactive mod.
    else:
        flag = 0
        instructions = instructions.split(" ")
        get_rid_of_coma(instructions)
        if instructions[0] in instruction_table:
            flag = 1
        # Check instruction exist in pseudo instruction table.
        elif instructions[0] in pseudo_table:
            flag = 2
        # If the instruction not found set the flag to -1.
        else:
            flag = -1
        # If instruction is real instruction.
        if flag == 1:
            ins_type = instruction_table[instructions[0]]
            if ins_type[0] == "R":
                r_type_decoder(instructions, ins_type)
            elif ins_type[0] == "I":
                i_type_decoder(instructions, ins_type)
        # If instruction is pseudo instruction.
        elif flag == 2:
            print("Pseudo!")
        else:
            print("Instruction could not detected!")
            print("Please try these instructions or load a look-up table.")
            print("Your instruction: {}".format(instructions[0]))
            print("Available instructions: ")
            print(instruction_table.keys())
            print("Available pseudo instructions: ")
            print(pseudo_table.keys())

# Auxiliary function to get rid of commas in the list.
def get_rid_of_coma(instruction):
    i = 0
    while i < len(instruction):
        instruction[i] = instruction[i].replace(",", "")
        i = i + 1

# R-Type Instruction Decoder
def r_type_decoder(i, ins_type):
    get_rid_of_coma(i)
    fun = ins_type[1]

    # Check which R-Type Instructions
    if ins_type[2] == "d" and ins_type[3] == "s":
        shamt = '00000'
        try:
            d = bin(register_table[i[1]])
        except KeyboardInterrupt:
            register_not_found(i[1])
        try:
            s = bin(register_table[i[2]])
        except KeyboardInterrupt:
            register_not_found(i[2])
        try:
            t = bin(register_table[i[3]])
        except KeyboardInterrupt:
            register_not_found(i[3])
    elif ins_type[2] == "d" and ins_type[3] == "t":
        try:
            d = bin(register_table[i[1]])
        except KeyboardInterrupt:
            register_not_found(i[1])
        try:
            t = bin(register_table[i[2]])
        except KeyboardInterrupt:
            register_not_found(i[2])
        shamt = bin(int(i[3]))
        s = '00000'
    elif ins_type[2] == "s":
        try:
            s = bin(register_table[i[1]])
        except KeyboardInterrupt:
            register_not_found(i[1])
        t = '00000'
        d = '00000'
        shamt = '00000'
        fun = '001000'
    final = binary_handle.r_type(s,t,d,shamt,fun)
    output.append(final)

# I-Type Instruction Decoder
def i_type_decoder(i, ins_type):
    get_rid_of_coma(i)
    opcode = ins_type[1]

    # Check whcih I-Type Instructions
    if ins_type[2] == 't' and ins_type[3] == 's':
        try:
            t = bin(register_table[i[1]])
        except KeyboardInterrupt:
            register_not_found(i[1])
        try:
            s = bin(register_table[i[2]])
        except KeyboardInterrupt:
            register_not_found(i[1])
        imm = int(i[3])
        check_imm(imm)

    elif ins_type[2] == 't' and ins_type[3] == 'i16(s)':
        print("lw")

    elif ins_type[2] == 's' and ins_type[3] == 't':
        print("beq")

    final = binary_handle.i_type(opcode,s,t,imm)
    output.append(final)

# Auxiliary function to give error if the register not found
def register_not_found(r):
    print("Register {} not found!".format(r))
    print("Available registers:")
    for register in register_table:
        print(register)
        print("Exiting...")
        exit(1)

# Auxiliary function to check shamt is in range or not
def check_shamt(shamt):
    if shamt < 0 or shamt > 31:
        print("Shamt must be in -32 < shamt < +31")
        print("Your shamt: {}".format(shamt))
        print("Exiting...")
        exit(1)

 # Auxiliary function to check immediate is in range or not       

# Auxiliary function to check immediate is in range or not
def check_imm(imm):
    imm_max = (2**15)-1
    imm_min = -(2**15)
    if imm < imm_min or imm > imm_max:
        print("Immediate must be in {} < imm < {}".format(imm_min, imm_max))
        print("Your immediate: {}".format(imm))
        print("Exiting...")
        exit(1)

if __name__ == "__main__":
    print("Please start assembler.py to start assembler!")
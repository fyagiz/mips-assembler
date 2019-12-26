from instructions import instruction_table
from instructions import pseudo_table
from registers import register_table
from label import label_list
from os import _exit as exit
import binary_handle

output = list()

def decode(instructions, mod):

    # Check the assembler start batch mod or not.
    # If Is it batch mode this if block will be executed.
    if mod == -1:
        # Decode the instructions by one by
        for idx, item in enumerate(instructions):
            flag = 0
            # Check insruction exist in instruction table.
            if item[0] in instruction_table:
                flag = 1
            # Check instruction exist in pseudo instruction table.
            elif item[0] in pseudo_table:
                flag = 2
            # If the instruction not found set the flag to -1.
            else:
                flag = -1
            # If instruction is real instruction.
            if flag == 1:
                ins_type = instruction_table[item[0]]
                if ins_type[0] == "R":
                    r_type_decoder(item, ins_type)
                elif ins_type[0] == "I":
                    i_type_decoder(item, ins_type, idx)
                elif ins_type[0] == "J":
                    j_type_decoder(item, ins_type, idx)
                else:
                    print("Instruction type could not detected!")
                    print("Exiting...")
                    exit(1)
            # If instruction is pseudo instruction.
            elif flag == 2:
                ins_type = pseudo_table[item[0]]
                ins_type = instruction_table[ins_type[0]]
                pseudo_handle(item, ins_type, idx)
            # If instruction is not found.
            else:
                # If the Instruction not found, exit.
                print("{} not found!".format(item[0]))
                print("Available instructions: ")
                print(instruction_table.keys())
                print("Available pseudo instructions: ")
                print(pseudo_table.keys())
                print("Exiting...")
                exit(1)
    # Execute these block if the program runs interactive mod.
    else:
        flag = 0
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
                i_type_decoder(instructions, ins_type, mod)
            elif ins_type[0] == "J":
                j_type_decoder(item, ins_type, idx)
            else:
                print("Instruction type could not detected!")
                print("Exiting...")
                exit(1)
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
def r_type_decoder(item, ins_type):
    get_rid_of_coma(item)
    fun = ins_type[1]

    # Check which R-Type Instructions
    if ins_type[2] == "d" and ins_type[3] == "s":
        shamt = '00000'
        try:
            d = bin(register_table[item[1]])
        except KeyboardInterrupt:
            register_not_found(item[1])
        try:
            s = bin(register_table[item[2]])
        except KeyboardInterrupt:
            register_not_found(item[2])
        try:
            t = bin(register_table[item[3]])
        except KeyboardInterrupt:
            register_not_found(item[3])
    elif ins_type[2] == "d" and ins_type[3] == "t":
        try:
            d = bin(register_table[item[1]])
        except KeyboardInterrupt:
            register_not_found(item[1])
        try:
            t = bin(register_table[item[2]])
        except KeyboardInterrupt:
            register_not_found(item[2])
        shamt = bin(int(item[3]))
        s = '00000'
    elif ins_type[2] == "s":
        try:
            s = bin(register_table[item[1]])
        except KeyboardInterrupt:
            register_not_found(item[1])
        t = '00000'
        d = '00000'
        shamt = '00000'
        fun = '001000'
    final = binary_handle.r_type(s,t,d,shamt,fun)
    output.append(final)

# I-Type Instruction Decoder
def i_type_decoder(item, ins_type, idx):
    get_rid_of_coma(item)
    opcode = ins_type[1]

    # Check whcih I-Type Instructions
    if ins_type[2] == 't' and ins_type[3] == 's':
        try:
            t = bin(register_table[item[1]])
        except KeyboardInterrupt:
            register_not_found(item[1])
        try:
            s = bin(register_table[item[2]])
        except KeyboardInterrupt:
            register_not_found(item[1])
        imm = int(item[3])
        check_imm(imm)

    elif ins_type[2] == 't' and ins_type[3] == 'i16(s)':
        try:
            t = bin(register_table[item[1]])
        except KeyboardInterrupt:
            register_not_found(item[1])
        temp = item[2].split("(")
        temp[1] = temp[1].replace(")","")
        try:
            s = bin(register_table[temp[1]])
        except KeyboardInterrupt:
            register_not_found(temp[1])
        imm = int(temp[0])
        check_imm(imm)

    elif ins_type[2] == 's' and ins_type[3] == 't':
        try:
            s = bin(register_table[item[1]])
        except KeyboardInterrupt:
            register_not_found(item[1])
        try:
            t = bin(register_table[item[2]])
        except KeyboardInterrupt:
            register_not_found(item[2])
        imm = branch_label_handle(item[3], idx)
        check_imm(imm)

    final = binary_handle.i_type(opcode,s,t,imm)
    output.append(final)

# J-Type Instruction Decoder
def j_type_decoder(item, ins_type, idx):
    get_rid_of_coma(item)
    opcode = ins_type[1]
    label = item[1]
    label_adress = jump_label_handle(label,idx)
    final = binary_handle.j_type(opcode,label_adress)
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

# Auxiliary function to handle branch label is in range or not
def branch_label_handle(label, idx):
    # Started location.
    pc = "0x80001000"
    # Check label is avialable or not.
    if label in label_list:
        # Get Available position of label.
        id = label_list[label]
        # Calculate label adress
        label_adress = int(pc,16) + 4*(id)
        # Calculate current pc
        real_pc = int(pc,16) + 4*(idx) + 4
        # Calculate label adress
        label_number = int((label_adress - real_pc) / 4)
        return label_number
    else:
        print("Label not found!")
        print("Your label is {}".format(label))
        print("Available lable(s) are: ")
        print(label_list.keys())
        exit(1)

# Auxiliary function to handle jump label
def jump_label_handle(label, idx):
    # Started location.
    pc = "0x80001000"
    # Check label is avialable or not.
    if label in label_list:
        # Get Available position of label.
        id = label_list[label]
        # Calculate label adress
        label_adress = bin(int(pc,16) + 4*(id))
        label_adress = label_adress.replace("0b","")
        # Get rid of first 4 and last 2 bits.
        label_adress = label_adress[4:-2]
        return label_adress
    else:
        print("Label not found!")
        print("Your label is {}".format(label))
        print("Available lable(s) are: ")
        print(label_list.keys())
        exit(1)

# Auxiliary function to handle pseudo
def pseudo_handle(item, ins_type, idx):
    if item[0] == 'move':
        temp = 'or'+" "+item[1]+" "+item[2]+", "+"$zero"
        temp = temp.split(" ")
        r_type_decoder(temp,ins_type)
        
if __name__ == "__main__":
    print("Please start assembler.py to start assembler!")
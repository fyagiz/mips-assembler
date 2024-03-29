 # Format: Type, Opcode/Function, operands

instruction_table = {
    'or' : ['R', '100101', 'd', 's', 't'],
    'div' : ['R', '011010', 's', 't'],
    'add'   : ['R', '100000', 'd', 's', 't'],
    'sll'  : ['R', '000000', 'd', 't', 'i5'],
    'slt'   : ['R', '101010', 'd', 's', 't'],
    'jr' : ['R', '001000', 's'],
    'bgez'  : ['I', '000001', 's', '1'],
    'bgtz'  : ['I', '000111', 's', '0'],
    'bltzal'  : ['I', '000001', 's', '16'],
    'addi'  : ['I', '001000', 't', 's', 'i16'],
    'slti'  : ['I', '001010', 't', 's', 'i16'],
    'sw' : ['I', '101011', 't', 'i16(s)'],
    'beq' :  ['I', '000100', 's', 't', 'i16'],
    'bne' :  ['I', '000101', 's', 't', 'i16'],
    'lw' : ['I', '100011', 't', 'i16(s)'],
    'jal' : ['J', '000011', 'i26'],
    'j' : ['J', '000010', 'i26'],
}


pseudo_table = {
    'move' : ['or', 't', 's', '$zero']
}

if __name__ == "__main__":
    print("Please start assembler.py to start assembler!")
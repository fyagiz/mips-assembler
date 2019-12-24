 # Format: Type, Opcode/Function, operands

instruction_table = {
    'addi'  : ['I', '001000', 't', 's', 'i16'],
    'slt'   : ['R', '101010', 'd', 's', 't'],
    'slti'  : ['I', '001010', 't', 's', 'i16'],
    'sll'  : ['R', '000000', 'd', 't', 'i5'],
    'add'   : ['R', '100000', 'd', 's', 't'],
    'sw' : ['I', '101011', 't', 'i16(s)'],
    'beq' :  ['I', '000100', 's', 't', 'i16'],
    'bne' :  ['I', '000101', 's', 't', 'i16'],
    'lw' : ['I', '100011', 't', 'i16(s)'],
    'jal' : ['J', '000011', 'i26'],
    'j' : ['J', '000010', 'i26'],
    'jr' : ['R', '001000', 's']
}


pseudo_table = {
    'move' : ['add', 't', 's', '$zero']
}

if __name__ == "__main__":
    print("Please start assembler.py to start assembler!")
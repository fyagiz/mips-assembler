import instructions
from os import _exit as exit

def lookup_table_handler(file_name):
    try:
        instructions = list()
        with open(file_name) as f:
            for line in f:
                instructions.append(line.strip())            
    # If the file could not open, error message will be written.
    except FileNotFoundError:
        print("File not found, please check file name or locations.")
        print("Look-Up Table is not added!")
    parser(instructions)

def parser(ins):
    for i in range(0,len(ins)):
        tmp = ins[i].rsplit(";")
        if tmp[0] not in instructions.instruction_table:
            instructions.instruction_table[tmp[0]] = tmp[1:]
        else:
            print("{} instruction is already loaded.".format(tmp[0]))
            pass

if __name__ == "__main__":
    print("Please start assembler.py to start assembler!")
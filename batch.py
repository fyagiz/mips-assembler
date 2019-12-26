from os import _exit as exit
import label
import output_generator

instruction_list = list()

def batch_mode(file_name):
    # Try to Open File
    try:
        instructions = list()
        with open(file_name) as f:
            for line in f:
                instructions.append(line.strip())
                
    # If the file could not open, error message will be written.
    except FileNotFoundError:
        print("File not found, please check file name locations.")
        print("Assembler wil be terminated.")
        exit(1)
    # Detext Labels
    label.detector(instructions)
    # Generate Outputs
    output_generator.decode(instructions,-1)
    
    for i in output_generator.output:
        print(i)

if __name__ == "__main__":
    print("Please start assembler.py to start assembler!")
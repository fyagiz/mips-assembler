from registers import register_table
from os import _exit as exit
import sys
import batch
import output_generator
import label
import lookup_handle


def main(argv):

    python_version_check()
    idx = 0
    print("Welcome to the Assembler!")
    if len(argv) == 0:
        print("Interactive Mod!")
        choice = 0
        while choice != "3":
            # Interactive Menu
            print("1. Assemble the Instruction")
            print("2. Load Lookup Table")
            print("3. Exit")
            print("Choice: ", end="")
            
            choice = input()

            if choice == "3":
                print("You choice exit Bye!")
            elif choice == "1":
                print("Instruction: ")
                instruction = input()
                instruction = label.interactive_detector(instruction, idx)
                output_generator.decode(instruction, idx)
                idx = idx + 1
                if len(output_generator.output) > 0: 
                    print(output_generator.output[-1])
            elif choice == "2":
                print("Look-up Table Directory: ", end="")
                file_name = input()
                lookup_handle.lookup_table_handler(file_name)
                
            else:
                print("Command does not understand!")
    else:
        print("Batch Mod Started!")
        if (len(argv) > 1):
            lookup_handle.lookup_table_handler(argv[1])
        batch.batch_mode(argv[0])

# To check Pyton version.
def python_version_check():

    if sys.version_info[0] < 3:
        print("Sorry, this assembler is only for Python3.")
        exit(1)

# Main function declaration.
if __name__ == "__main__":
    # Send sys.argv list to main from index 1 to end. 
    main(sys.argv[1:])
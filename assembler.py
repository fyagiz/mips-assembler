from registers import register_table
from os import _exit as exit
import sys
import batch
import output_generator


def main(argv):

    python_version_check()
    print("Welcome to the Assembler!")
    if len(argv) == 0:
        print("Interactive Mod!")
        choice = 0
        while int(choice) != 3:
            # Interactive Menu
            print("1. Load Lookup Table")
            print("2. Assemble the Instruction")
            print("3. Exit")
            print("Choice: ", end="")
            
            choice = input()

            if int(choice) == 3:
                print("You choice exit Bye!")
            elif int(choice) == 2:
                print("Instruction: ")
                instruction = input()
                output_generator.decode(instruction)
                print(output_generator.output[-1])
            elif int(choice) == 1:
                print("To be completed!")
            else:
                print("Command does not understand!")
    else:
        print("Batch Mod Started!")
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
label_list = dict()

# This function will detect labels and add to label dictionary. 
def detector(instructions):
    for idx, item in enumerate(instructions):
        flag = item.find(":")
        if flag != -1:
            label_name = item.rsplit(":")[0]
            instructions[idx] = item.rsplit(":")[1].strip()
            label_list[label_name] = idx
        instructions[idx] = instructions[idx].rsplit(" ")
def interactive_detector(instruction, idx):
    flag = instruction.find(":")
    if flag != -1:
        label_name = instruction.rsplit(":")[0]
        instruction = instruction.rsplit(":")[1].strip()
        label_list[label_name] = idx
    instruction = instruction.rsplit(" ")
    return instruction

if __name__ == "__main__":
    print("Please start assembler.py to start assembler!")
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



if __name__ == "__main__":
    print("Please start assembler.py to start assembler!")
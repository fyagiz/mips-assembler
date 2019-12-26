# Check R-Type Instructions Bits and Convert to Hex
def r_type(s,t,d,shamt,fun):
    s = s.replace("0b","")
    t = t.replace("0b","")
    d = d.replace("0b","")
    shamt = shamt.replace("0b","")
    if len(s) < 5:
        s = s.zfill(5-len(s) + len(s)) 
    if len(t) < 5:
        t = t.zfill(5-len(t) + len(t))
    if len(d) < 5:
        d = d.zfill(5-len(d) + len(d))
    if len(shamt) < 5:
        shamt = shamt.zfill(5-len(shamt) + len(shamt))
    
    final = '000000' + s + t + d + shamt + fun
    final = int(final,2)
    final = hex(final).replace("0x", "")
    final = last_check(final)
    return final

# Check I-Type Instructions Bits and Convert to Hex
def i_type(opcode,s,t,imm):
    s = s.replace("0b","")
    t = t.replace("0b","")

    # Check immediate value is negative or not
    if imm >= 0:
        imm = bin(imm)
        imm = imm.replace("0b","")
        if len(imm) < 16:
            imm = imm.zfill(16-len(imm) + len(imm))
    else:
        imm = bin(imm)
        imm = imm.replace("-0b","")
        if len(imm) < 16:
            imm = imm.zfill(16-len(imm) + len(imm))     
        imm = twos_complement(imm,16)   
        
    if len(s) < 5:
        s = s.zfill(5-len(s) + len(s)) 
    if len(t) < 5:
        t = t.zfill(5-len(t) + len(t))

    final = opcode + s + t + imm
    final = int(final,2)
    final = hex(final).replace("0x", "")
    final = last_check(final)
    return final

# Check J-Type Instructions Bits and Convert to He
def j_type(opcode,label_adress):
    final = opcode + label_adress
    final = int(final,2)
    final = hex(final).replace("0x", "")
    final = last_check(final)
    return final
    
# To take Two's Complement
def twos_complement(imm, bit_length):
    imm_list = list(imm)
    i = bit_length-1
    flag = 0
    while (i>=0):
        if flag == 0:
            if imm_list[i] == '0':
                pass
            else:
                flag=1
        else:
            if imm_list[i] == '0':
                imm_list[i] = '1'
            else:
                imm_list[i] = '0'
        i = i-1
    imm = ''.join(map(str,imm_list))
    return imm

# To check Leading Zeros
def last_check(final):
    if len(final) < 8:
        final = final.zfill(8-len(final) + len(final))
        final = "0x" + final
    else:
        final = "0x" + final
    return final

if __name__ == "__main__":
    print("Please start assembler.py to start assembler!")
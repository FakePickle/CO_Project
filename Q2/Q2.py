from sys import stdin,stdout,exit

PC = 0
mem = ['0'*16] * 256

overflow = 2**16 - 1
underflow = 0

text = ["1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","1000000000001010","0101000000000000"]

commands = []

for i in range(len(text)):
    text[i] = text[i].strip()
    commands.append(text[i])

commands = list(filter(lambda a: a != "",commands))

Reg_File = {'000' : 0, '001' : 0, '010' : 0, '011' : 0, '100' : 0, '101' : 0, '110' : 0, '111' : 0}

def mem_store():
    for i in range(len(commands)):
        mem[i] = commands[i]
    print(mem)
mem_store()
#Adi part
def bin_convert():
    number = bin(number)[2:]
    return number


def add(r1,r2,r3):
    result = Reg_File[r1] + Reg_File[r2]
    if result > overflow:
        Reg_File['111'] += 8
        result = result % (overflow + 1)
    Reg_File[r3] = result
  

def sub(r1,r2,r3):
    result = Reg_File[r1] - Reg_File[r2]
    if result < underflow:
        Reg_File['111'] += 8
        result = 0
    Reg_File[r3] = result

def mul(r1,r2,r3):
    result = Reg_File[r1] * Reg_File[r2]
    if result > overflow:
        Reg_File['111'] += 8
        result = result % (overflow + 1)
    Reg_File[r3] = result

def xor(r1,r2,r3):
    Reg_File[r3] = Reg_File[r1] ^ Reg_File[r2]

def or_(r1,r2,r3):
    Reg_File[r3] = Reg_File[r1] | Reg_File[r2]

def and_(r1,r2,r3):
    Reg_File[r3] = Reg_File[r1] & Reg_File[r2]

def mov_i(reg,imm):
    Reg_File[reg] = imm

def mov_r(r1,r2):
    Reg_File[r2] = Reg_File[r1]

def right(reg,imm):
    result = Reg_File[reg] >> imm
    if result > overflow:
        result = result % (overflow + 1)
    Reg_File[reg] = result

def left(reg,imm):
    Reg_File[reg] = Reg_File[reg] << imm


opcode = {"00000": [add,"A"],"00001":[sub,"A"],"00010":[mov_i,"B"],'00011':[mov_r,'C'],"00100":[load,"D"],
          "00101":[store,"D"],"00110":[mul,"A"],"00111":[div,"C"],"01000":[right,"B"],
		  "01001":[left,"B"],"01010":[xor,"A"],"01011":[or_,"A"],"01100":[and_,"A"],
		  "01101":[not_,"C"],"01110":[cmp,"C"],"01111":[jmp,"E"],"11100":[jlt,"E"],
		  "11101":[jgt,"E"],"11111":[je,"E"],"11010":["hlt","F"]}
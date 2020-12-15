from  Helpers.GetInput import get_input_split_lines
import re

def intToBinString(intVal):
    if intVal == 0:
        return "0"*36
    strVal = ""
    while intVal > 0:
        if intVal%2!=0:
            strVal="1"+strVal
        else:
            strVal="0"+strVal
        intVal=int(intVal/2)
    while len(strVal)<36:
        strVal="0"+strVal
    return strVal


def bin_add(*args): return bin(sum(int(x, 2) for x in args))[2:]


def find_permutations(string):
    x_count = string.count('X')
    binary=""
    bin_c=""
    perms=[]
    temp=""
    for x in range(x_count):
        binary += '0'
    while len(binary) <= x_count:
        bin_c = binary
        temp = list(string)
        while len(bin_c)<x_count:
            bin_c="0"+bin_c
        for x in range(len(string)-1,-1,-1):
            if temp[x]=='X':
                temp[x]=bin_c[len(bin_c)-1]
                bin_c=bin_c[:-1]
        perms.append(temp)
        binary = bin_add(binary, "1")
        while len(binary) < x_count:
            binary = "0" + binary
        print(binary)
    return perms


def day_14_1(raw_input):
    Addresses={}
    mask=""
    mask_pattern=r"(mask\s=\s)([01X]+)"
    mem_pattern=r"(mem\[)([0-9]+)(\])\s=\s([0-9]+)"
    for x in raw_input:
        mask_re=re.match(mask_pattern,x)
        mem_re=re.match(mem_pattern,x)
        if mask_re is not None:
            mask=mask_re[2]
            print(f"mask:{mask}")
        if mem_re is not None:
            after=""
            binary=intToBinString(int(mem_re[4]))
            for z in range(len(mask)):
                if mask[z]=="X":
                    after=after+binary[z]
                else:
                    after=after+mask[z]
            Addresses[int(mem_re[2])]=int(after, 2)
            print(f"mem:{mem_re[2]}, value:{int(after, 2)}")
    sum=0
    for x, y in Addresses.items():
        sum+=y
    print(sum)


def day_14_2(raw_input):
    Addresses = {}
    mask = ""
    sum=0
    mask_pattern = r"(mask\s=\s)([01X]+)"
    mem_pattern = r"(mem\[)([0-9]+)(\])\s=\s([0-9]+)"
    for x in raw_input:
        mask_re = re.match(mask_pattern, x)
        mem_re = re.match(mem_pattern, x)
        if mask_re is not None:
            mask = mask_re[2]
            print(f"mask:{mask}")
        if mem_re is not None:
            after = ""
            add=intToBinString(int(mem_re[2]))
            for z in range(len(mask)):
                if mask[z]=="0":
                    after=after+add[z]
                elif mask[z]=='1':
                    after=after+mask[z]
                elif mask[z]=='X':
                    after=after+'X'
            perms=find_permutations(after)
            for x in perms:
                z="".join(x)
                Addresses[int(z,2)]=int(mem_re[4])
    for x, y in Addresses.items():
        sum+=y
    print(sum)


if __name__ == '__main__':
    raw_input = get_input_split_lines(14)
    day_14_2(raw_input)

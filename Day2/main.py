import re


def day_2_1():
    valid=0
    pattern="([0-9]+)-([0-9]+)\s([1-z]):\s(\w*)[\\n]?"
    with open('Day2\input.txt', 'r') as input:
        list=input.readlines()
        for x in list:
            z=re.match(pattern, x)
            valid+=1 if z is not None and int(z[1]) <= z[4].count(z[3]) <= int(z[2]) else 0
    print(valid)


def day_2_2():
    valid = 0
    pattern = "([0-9]+)-([0-9]+)\s([1-z]):\s(\w*)[\\n]?"
    with open('Day2\input.txt', 'r') as input:
        list = input.readlines()
        for x in list:
            z = re.match(pattern, x)
            valid += 1 if ( (z[4][int(z[1])-1]==z[3] or z[4][int(z[2])-1]==z[3]) and z[4][int(z[2])-1] != z[4][int(z[1])-1] ) else 0
    print(valid)


if __name__ == '__main__':
    day_2_2()

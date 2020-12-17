from Helpers.GetInput import get_input_split_lines,get_file_split_lines
import re

def check_invalid_part1(ranges,line):
    line=line.split(",")
    rate=0
    for z in line:
        included=[]
        for x in ranges:
            included.append(x[1]<=int(z)<=x[2] or x[3]<=int(z)<=x[4])
        if not any(included):
            rate+=int(z)
    return rate


def day_16_1(rules, tickets):
    ranges=[]
    valid=[]
    rate=0
    for z in rules:
        k=re.findall(r"([\s\w]+):\s([0-9]+)-([0-9]+)\sor\s([0-9]+)-([0-9]+)", z)
        ranges.append((k[0][0],int(k[0][1]),int(k[0][2]),int(k[0][3]),int(k[0][4])))
    for line in tickets:
        rate += check_invalid_part1(ranges, line)
        #if check_invalid_part1(ranges, line):
        #valid.append(line.split("\n"))
    print(rate)
    #207175 too high



def find_valid(ranges,line,pos):
    line=line.split(",")
    rate=0
    found={}
    for z in line:
        for k in ranges:
            if not (k[1] <= int(z) <= k[2] or k[3] <= int(z) <= k[4]):
                print(int(z))
                print(line.index(z))
                if line.index(z) in pos[k[0]]:
                    pos[k[0]].remove(line.index(z))



def remove_invalid(ranges,line):
    line=line.split(",")
    rate=0
    for z in line:
        included=[]
        for x in ranges:
            included.append(x[1]<=int(z)<=x[2] or x[3]<=int(z)<=x[4])
        if not any(included):
            return True


def fix_list(pos, remove):
    definitive=True
    for x,y in pos.items():
        for z in remove:
            if z[1] in y and x!=z[0]:
                pos[x].remove(z[1])
    for x, y in pos.items():
        if len(y) == 1:
            remove.append((x, y[0]))
    if all([len(y)==1 for x,y in pos.items()]):
        return
    fix_list(pos, remove)


def day_16_2(rules, tickets):
    pos = {}
    ranges = []
    valid = []
    points = []
    remove = []
    dep_score = 1
    for x in range(0, 20):
        points.append(x)
    for z in rules:
        k=re.findall(r"([\s\w]+):\s([0-9]+)-([0-9]+)\sor\s([0-9]+)-([0-9]+)", z)
        ranges.append((k[0][0], int(k[0][1]), int(k[0][2]), int(k[0][3]), int(k[0][4])))
    for x in ranges:
        pos[x[0]] = points.copy()

    for z in range(len(tickets)):
        if not remove_invalid(ranges,tickets[z]):
            valid.append(tickets[z])
    for line in valid:
        #rate += check_invalid_part2(ranges, line)
        find_valid(ranges, line, pos)

    for x, y in pos.items():
        if len(y) == 1:
            remove.append((x, y[0]))
    fix_list(pos,remove)
    print(pos)
    valid[0]=valid[0].split(",")
    for x, y in pos.items():
        if "departure" in x:
            dep_score*=int(valid[0][y[0]])
    print(dep_score)



if __name__ == '__main__':
    tickets = get_input_split_lines(16)
    rules = get_file_split_lines("Day16\\rules.txt")
    day_16_2(rules, tickets)

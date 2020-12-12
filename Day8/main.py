
all = {}
jmps = []


def run_loop():
    visited = []
    acc = 0
    current = 0
    changed = False
    while current not in visited:
        if current>635:
            break
        visited.append(current)
        k=all[current].split(" ")
        if "acc" in all[current]:
            acc += int(k[1])
            current += 1
            continue
        if "jmp" in all[current]:
            current+=int(k[1])
            continue
        if "nop" in all[current]:
            current += 1
            continue
    if current>635:
        return True, acc
    else:
        return False, acc


def day_8_1():
    with open('Day8\input.txt', 'r') as input:
        lines="".join(input.readlines()).split("\n")
        for x in range(0, len(lines)):
            all[x]=lines[x]
    visited = []
    acc = 0
    current = 0
    changed = False
    while current not in visited:
        visited.append(current)
        k = all[current].split(" ")
        if "acc" in all[current]:
            acc += int(k[1])
            current += 1
            continue
        if "jmp" in all[current]:
            current += int(k[1])
            continue
        if "nop" in all[current]:
            current += 1
            continue
    for x in visited:
        if all[x].split(" ")[0] == "jmp":
            jmps.append(x)
    for x in jmps:
        z=all[x]
        all[x] = "nop +0"
        res=run_loop()
        if res[0]:
            print(res[1])
            break
        all[x]=z

if __name__ == '__main__':
    day_8_1()
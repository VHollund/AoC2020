def get_input(day):
    with open(f'Day{day}\input.txt', 'r') as input:
        lines = "".join(input.readlines()).split("\n")
        results = list(map(int, lines))
        results.append(0)
        return results


def day_10_1(raw):
    raw = sorted(raw)
    raw.append(raw[len(raw)-1]+3)
    print(raw)
    permutations=1
    jolts = 0
    oneJolt=0
    inARow = 0
    ThreeJolt=0
    for x in range(0, len(raw)):
        if raw[x]-raw[x-1] == 1:
            oneJolt+=1
            inARow += 1
        if raw[x]-raw[x-1] == 3:
            ThreeJolt += 1
            permutations *= GetPermutations(inARow)
            inARow = 0
    print(oneJolt*ThreeJolt)
    print(permutations)


def GetPermutations(n):
    tList = [0,0,1]
    t1, t2, t3 = 0, 0, 0
    if n < 2: return 1
    elif n == 2: return 2
    else:
        for i in range(3,n+3):
            t1, t2, t3 = int(tList[i-3]),int(tList[i-2]),int(tList[i-1])
            tList.append(t1+t2+t3)
    return tList[-1]


if __name__ == '__main__':
    raw_input = get_input(10)
    day_10_1(raw_input)

import typing

all = {}

def day_9_1():
    for x in range(26,len(all)):
        valid=False
        curr=all[x]
        for f in range(x-25,x):
            l=[y for z,y in all.items() if z in range(x-25,x)]
            if all[x]-all[f] in l:
                valid=True
            if valid:
                break
        if not valid:
            return x, all[x]

def sum_dict(start,r):
    l = [y for z, y in all.items() if z in range(start, start+r)]
    return sum(l)


def day_9_2():
    num=0
    with open('Day9\input.txt', 'r') as input:
        lines = "".join(input.readlines()).split("\n")
        for x in range(0, len(lines)):
            all[x] = int(lines[x])
    num=day_9_1()
    t_sum=0
    for x in range(2, 100):
         for z in range(0,num[0]):
             if sum_dict(z, x)==num[1]:
                k=[h for g,h in all.items() if g in range(z,z+x)]
                k.sort()
                print(max(k)+min(k))

if __name__ == '__main__':
    day_9_2()
input = [0,14,6,20,1,4]

def day_15(part):
    x=len(input)
    known={}
    for z in range(len(input)-1):
        known[input[z]]=z+1
    lastEntry=input[len(input)-1]
    p=0
    while x<=part+1:
        if lastEntry not in known.keys():
            known[lastEntry]=x
            lastEntry=0
        elif lastEntry in known.keys():
            p=x-known[lastEntry]
            known[lastEntry] = x
            lastEntry=p
        x+=1
    for x,y in known.items():
        if y==part:
            print(x)

if __name__ == '__main__':
    part1 = 2020
    part2 = 30000000
    day_15(part1)

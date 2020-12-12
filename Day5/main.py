def day_5_1():
    seats=[]
    seatIds=[]
    my_seats=[]
    with open('Day5\input.txt', 'r') as input:
        seats=input.readlines()
        for x in range(0,len(seats)):
            seats[x]=seats[x].replace("\n", "")
    for x in seats:
        print(x)
        r=6
        c=2
        rup = 127
        rlow = 0
        cup = 7
        clow = 0
        for z in x:
            if z=='F':
                rup = rup - 2 ** r
            if z=='B':
                rlow = rlow + 2 ** r
            if z == 'R':
                clow = clow + 2**c
                c -= 1
            if z == 'L':
                cup = cup - 2**c
                c -= 1
            r-=1

            print(f"{rlow}-{rup}, {clow}-{cup}")
        print((rup*8)+cup)
        if rup != 127 and rup != 0:
            seatIds.append((rup*8)+cup)
    print(max(seatIds))
    for x in seatIds:
        if x+2 in seatIds and x+1 not in seatIds:
            print(x+1)
        if x-2 in seatIds and x-1 not in seatIds:
            print(x-1)




if __name__ == '__main__':
    day_5_1()
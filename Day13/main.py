from functools import reduce


def get_input_tuple(day):
    with open(f'Day{day}\input.txt', 'r') as input:
        lines = "".join(input.readlines()).split("\n")
        lines = (lines[0], [int(x) if x != 'x' else x for x in lines[1].split(",")])
    return lines


def check_valid(timestamp, busses, r):
    for x in range(r):
        if busses[x] == 'x':
            continue
        if (timestamp+x) % busses[x] != 0:
            return False
    return True

#149726654000000
#100299423000000

def day_13_1(inp):
    otime=int(inp[0])
    time=int(inp[0])
    busses=[int(x) for x in inp[1]]
    low=1
    lbuss=13
    wait=0
    while low != 0:
        for z in busses:
            if time%z<low:
                low=time%z
                lbuss=z
            if low==0:
                break
        if low == 0:
            break
        time+=1
        wait+=1
    print(f"time:{otime}, wait:{time-otime}, buss:{lbuss}")
    print(f"{wait*lbuss}")
#100027372867366
#149726651890963
def day_13_2(inp):
    busses=inp[1]
    r = len(busses)
    i = 249999997288451
    while not check_valid(i-r, busses, r) and i > 100027372867366:
        if i%1000000==0:
            print(i)
        i-=647
    print(i-r)



def sync(buses):
    indices = [i for i, bus in enumerate(buses) if bus]
    diff = indices[-1] - indices[0]
    prod = reduce(lambda a, b: a * b, filter(None, buses))
    return sum((diff - i) * pow(prod // n, n - 2, n) * prod // n
               for i, n in enumerate(buses) if n) % prod - diff


if __name__ == '__main__':
    raw_input = get_input_tuple(13)
    #day_13_2(raw_input)
    busses=[int(x) if x != 'x' else 0 for x in raw_input[1]]
    print(sync(busses))

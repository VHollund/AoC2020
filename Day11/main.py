from Helpers.GetInput import get_input


def fof(z):
    return z=="L" or z=="."


def flip_string(string,x,c):
    s=list(string)
    s[x]=c
    return "".join(s)


def is_edge_seat_free(k,y,x):
    if y==0 and x==0:
        if fof(k[y][x+1]) and fof(k[y+1][x]) and fof(k[y+1][x+1]):
            return True
        return False
    elif y==0 and x==len(k[0])-1:
        if fof(k[y][x-1]) and fof(k[y+1][x]) and fof(k[y+1][x-1]):
            return True
        return False
    elif y==0: #top
        if fof(k[y][x - 1]) and fof(k[y][x+1]) and fof(k[y + 1][x - 1]) and fof(k[y + 1][x]) and fof(k[y + 1][x + 1]):
            return True
        return False
    elif y==len(k)-1 and x==0:
        if fof(k[y][x+1]) and fof(k[y-1][x]) and fof(k[y-1][x+1]):
            return True
        return False
    elif y==len(k)-1 and x==len(k[0])-1:
        if fof(k[y][x-1]) and fof(k[y - 1][x-1]) and fof(k[y - 1][x]):
            return True
        return False
    elif y==len(k)-1: #bot
        if fof(k[y][x - 1]) and fof(k[y-1][x]) and fof(k[y][x+1]) and fof(k[y - 1][x-1]) and fof(k[y - 1][x + 1]):
            return True
        return False
    elif x==len(k[0])-1: #right
        if fof(k[y][x - 1]) and fof(k[y-1][x]) and fof(k[y + 1][x]) and fof(k[y + 1][x-1]) and fof(k[y - 1][x - 1]):
            return True
        return False
    elif x==0: #Left
        if fof(k[y][x + 1]) and fof(k[y-1][x]) and fof(k[y + 1][x]) and fof(k[y + 1][x+1]) and fof(k[y - 1][x + 1]):
            return True
        return False
    return False


def check_surrounding(k, y, x):
    return fof(k[y-1][x]) and fof(k[y-1][x-1]) and fof(k[y-1][x+1]) and fof(k[y][x-1]) and fof(k[y][x+1]) and fof(k[y+1][x]) and fof(k[y+1][x-1]) and fof(k[y+1][x+1])


def rule_1(k):
    new_k=k.copy()
    for y in range(len(k)):
        for x in range(len(k[y])):
            if k[y][x]!=".":
                if y == 0 or y == len(k) - 1 or x == 0 or x == len(k[0]) - 1:
                    if is_edge_seat_free(k, y, x):
                        new_k[y]=flip_string(new_k[y], x,"#")
                elif check_surrounding(k, y, x):
                    new_k[y]=flip_string(new_k[y], x,"#")
    return new_k


def check_edge(k, y, x):
    l=""
    if x==0:
        l=f"{k[y-1][x]}{k[y-1][x+1]}{k[y][x+1]}{k[y+1][x]}{k[y+1][x+1]}"
        return l.count("#")
    elif x==len(k[0])-1:
        l+=k[y-1][x]+k[y-1][x-1]+k[y][x-1]+k[y+1][x]+k[y+1][x-1]
        return l.count("#")
    elif y==0:
        l += k[y][x-1] + k[y][x+1] + k[y+1][x] + k[y + 1][x-1] + k[y + 1][x + 1]
        return l.count("#")
    elif y==len(k)-1:
        l += k[y][x-1] + k[y][x+1] + k[y-1][x] + k[y-1][x-1] + k[y-1][x+1]
        return l.count("#")


def count_surrounding(k, y, x):
    l = ""
    l += k[y][x-1]+k[y][x+1] + k[y-1][x]+k[y-1][x-1]+k[y-1][x+1] + k[y+1][x-1]+k[y+1][x]+k[y+1][x+1]
    return l.count("#")


def rule_2(k):
    new_k=k.copy()
    for y in range(len(k)):
        for x in range(len(k[y])):
            if k[y][x] == "#":
                if (y==0 or y==len(k)-1) and (x==0 or x==len(k[0])-1):
                    continue
                elif y==0 or y==len(k)-1 or x==0 or x==len(k[0])-1:
                    z = check_edge(k, y, x)
                    if z>=4:
                        new_k[y]=flip_string(new_k[y], x, "L")
                elif count_surrounding(k, y, x) >= 4:
                    new_k[y]=flip_string(new_k[y], x, "L")
    return new_k


def day_11_1(k):
    old_k=[]
    new_k=k
    while new_k!=old_k:
        old_k = new_k.copy()
        new_k=rule_1(new_k.copy())
        new_k=rule_2(new_k.copy()).copy()
    print("".join(new_k).count("#"))
    for x in new_k:
        print(x)


def check_t(k,y,x): #returns true if lane is open
    if y == 0:
        return True
    for l in range(y-1, -1, -1):
        if k[l][x] == "#":
            return False
        if k[l][x] == "L":
            return True
    return True


def check_b(k,y,x): #returns true if lane is open
    if y == len(k)-1:
        return True
    for y1 in range(y+1,len(k)):
        if k[y1][x] == "#":
            return False
        if k[y1][x] == "L":
            return True
    return True


def check_l(l, y, x): #returns true if lane is open
    if x == 0:
        return True
    for z in range(x-1, -1, -1):
        if l[z] == "#":
            return False
        if l[z] == "L":
            return True
    return True


def check_r(l, y, x):
    if x==len(l)+1:
        return True
    for z in range(x+1, len(l)):
        if l[z] == "#":
            return False
        if l[z] == "L":
            return True
    return True


def check_tr(k, y, x):
    c = 1
    if y == 0 or x == len(k[0])-1:
        return True
    while y-c >= 0 and x+c < len(k[0]):
        if k[y - c][x + c] == '#':
            return False
        if k[y - c][x + c] == 'L':
            return True
        c += 1
    return True


def check_tl(k, y, x):
    c = 1
    if x == 0 or y == 0:
        return True
    while y-c >= 0 and x-c >= 0:
        if k[y - c][x - c] == '#':
            return False
        if k[y - c][x - c] == 'L':
            return True
        c+=1
    return True


def check_bl(k, y, x):
    c = 1
    if y==len(k[0])-1 or x==0:
        return True
    while c + y < len(k) and x-c >= 0:
        if k[y + c][x - c] == '#':
            return False
        if k[y + c][x - c] == 'L':
            return True
        c += 1
    return True


def check_br(k, y, x):
    c=1
    if x==len(k[0])-1 or y==len(k)-1:
        return True
    while c+y<len(k) and c+x<len(k[0]):
        if k[y+c][x+c] == '#':
            return False
        if k[y + c][x + c] == 'L':
            return True
        c += 1
    return True


def all_dir(k,y,x): #returns true if all dir are clear
    count=0
    if not check_t(k,y,x):
        count+=1
    if not check_b(k,y,x):
        count+=1
    if not check_l(k[y],y,x):
        count+=1
    if not check_r(k[y],y,x):
        count+=1
    if not check_br(k,y,x):
        count+=1
    if not check_bl(k,y,x):
        count+=1
    if not check_tr(k,y,x):
        count+=1
    if not check_tl(k,y,x):
        count+=1
    return count==0

def count_dir(k,y,x):
    count=0
    if not check_t(k,y,x):
        count+=1
    if not check_b(k,y,x):
        count+=1
    if not check_l(k[y],y,x):
        count+=1
    if not check_r(k[y],y,x):
        count+=1
    if not check_br(k,y,x):
        count+=1
    if not check_bl(k,y,x):
        count+=1
    if not check_tr(k,y,x):
        count+=1
    if not check_tl(k,y,x):
        count+=1
    return count


def rule_1_2(k):
    new_k=k.copy()
    for y in range(len(k)):
        for x in range(len(k[y])):
            if k[y][x] != ".":
                if all_dir(k, y, x):
                    new_k[y] = flip_string(new_k[y], x, "#")
    return new_k


def rule_2_2(k):
    new_k = k.copy()
    for y in range(len(k)):
        for x in range(len(k[y])):
            if k[y][x] == "#":
                if count_dir(k, y, x) >= 5:
                    new_k[y] = flip_string(new_k[y], x, "L")
    return new_k


def day_11_2(k):
    old_k=[]
    new_k=k
    while new_k!=old_k:
        old_k = new_k.copy()
        new_k=rule_1_2(new_k)
        new_k=rule_2_2(new_k)
    for x in new_k:
        print(x)
    print("".join(new_k).count("#"))


if __name__ == '__main__':
    raw_input = get_input(11)
    day_11_2(raw_input)

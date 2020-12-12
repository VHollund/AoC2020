import re
import typing

pattern=r"([\w]+\s[\w]+)\sbags\scontain\s(no\sother\sbags\.)?(([0-9]+)\s([\w]+\s[\w]+)\sbags?[,|.])?\s?(([0-9]+)\s([\w]+\s[\w]+)\sbags?[,|.])?\s?(([0-9]+)\s([\w]+\s[\w]+)\sbags?[,|.])?\s?(([0-9]+)\s([\w]+\s[\w]+)\sbags?[,|.])?"
bag_count={}
bag_size={}

def contains_bags(bagString, bagDict: typing.Dict):
    total=0
    content=bagDict[bagString]
    for x in content:
        total+=x[0]
        if x[1] not in bag_size:
            bag_size[x[1]]=contains_bags(x[1], bagDict)
        total+=x[0]*bag_size[x[1]]
    print(total)
    return total
#7016601 too high

def day_7_1():
    count=0
    contains={}
    with open('Day7\input.txt', 'r') as input:
        lines="".join(input.readlines()).split("\n")
        for x in lines:
            k=re.match(pattern,x)
            if "no other bags." in x:
                contains[k[1]]=[]
                continue
            contains[k[1]]=[]
            for z in range(4,16,3):
                if k.group(1) is not None and k.group(z) is not None:
                    contains[k.group(1)].append((int(k.group(z)), k.group(z+1)))

    print(contains_bags("shiny gold",contains))





if __name__ == '__main__':
    day_7_1()
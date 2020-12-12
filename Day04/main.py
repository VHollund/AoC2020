import re
import collections


def day_4_1():
    items = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    items.sort()
    valid=0
    with open('Day4\input.txt', 'r') as input:
        input=''.join(input.readlines()).split('\n\n')
        for e in input:
            e.replace('\n', " ")
            list=[x for x in re.findall(r"[a-z]{3}", e)]
            if all((x in list) for x in items):
                valid+=1
    print(valid)


def check_hight(x):
    k = re.match("([0-9]+)(cm|in)", x)
    if k is not None:
        return (k[2] == "in" and 59 <= int(k[1]) <= 76) or (k[2] == "cm" and 150 <= int(k[1]) <= 193)
    else:
        return False


def day_4_2():
    items = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    Ecolor=["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    items.sort()
    valid=0
    with open('Day4\input.txt', 'r') as input:
        input=''.join(input.readlines()).split('\n\n')
        print(len(input))
        for e in input:
            e=e.replace('\n', " ")
            list = [x for x in re.findall(r"[a-z]{3}", e)]
            if not all((x in list) for x in items):
                continue
            dict={x[0]: x[1] for x in re.findall(r"([a-z]{3}):([#]?[\w]+)", e)}
            if "cid" in dict.keys():
                dict.pop("cid")
            fact=[1920<=int(dict['byr'])<=2002,
            2010<=int(dict['iyr'])<=2020,
            2020<=int(dict['eyr'])<=2030,
            check_hight(dict["hgt"]),
            re.search("#[0-9a-f]{6}", dict["hcl"]) is not None,
            dict["ecl"] in Ecolor,
            (len(dict["pid"]) == 9 and dict["pid"].isdigit())
            ]
            if all(fact):
                if "cid" in dict.keys():
                    dict.pop("cid")
                print(",", sorted(dict.items()))
                valid += 1
#not 225 too high
#not 150 too low
    print(valid)


if __name__ == '__main__':
    day_4_2()


def day_6_1():
    count=0
    with open('Day6\input.txt', 'r') as input:
        ans="".join(input.readlines())
        ans=ans.split("\n\n")
        groups=[]
        for x in range(0,len(ans)):
            groups.append(set(ans[x].replace("\n","")))
        for x in groups:
            count+=len(x)
    print(count)



def day_6_2():
    count=0
    with open('Day6\input.txt', 'r') as input:
        ans="".join(input.readlines())
        ans=ans.split("\n\n")
        answeres=[]
        for x in range(0,len(ans)):
            yes=0
            groups_answers=set(ans[x].replace("\n",""))
            group_size=ans[x].count("\n")+1
            individual=ans[x].split("\n")
            for z in groups_answers:
                if ans[x].count(z)==group_size:
                    yes+=1
            count+=yes
    print(count)





if __name__ == '__main__':
    day_6_2()
def day_3_1(r,d):
    x=0
    y=0
    trees=0
    with open('Day3\input.txt', 'r') as input:
        grid=[z[0:len(z)-1] for z in input.readlines()]
        while y<len(grid):
            x+=r
            y+=d
            if x > len(grid[0])-1:
                x-=len(grid[0])
            if grid[y][x]=='#':
                trees+=1
            if y==len(grid)-1:
                break
    return trees





if __name__ == '__main__':
    r = [1, 3, 5, 7, 1]
    d = [1, 1, 1, 1, 2]
    product = 1
    for x, z in zip(r, d):
        product = product*(day_3_1(x, z))
    print(product)

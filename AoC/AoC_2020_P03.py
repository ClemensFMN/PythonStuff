# insppired by https://github.com/0xVector/AdventOfCode2020/blob/master/day03.py

with open("AoC_2020_P03_input.txt") as file:
    grid = [line[0:-1] for line in file] # read in every line but the last char (and that's CR)
    # grid = [line for line in file]

# we can use grid as follows: grid[y][x]
# grid[0][0] is the left-upper point

width = len(grid[0])
height = len(grid)


def check_part1(right, down):
    x, y = 0,0
    cnt = 0

    while(y < height-1):
        x = x + right
        y = y + down

        if(x >= width):
            x = x - width

        print(x,y)
            
        if(grid[y][x] == "#"):
           cnt = cnt + 1

    return cnt

res_part1 = check_part1(3, 1)
print(res_part1)

res_part2 = check_part1(1, 1) * check_part1(3, 1) * check_part1(5, 1) * check_part1(7, 1) * check_part1(1, 2)
print(res_part2)

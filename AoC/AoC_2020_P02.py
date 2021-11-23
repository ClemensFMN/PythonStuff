from pyparsing import Word, alphas, nums, OneOrMore


def checkLine_part1(strt, stp, char, passwd):
    # check whether line corresponds to a valid passwordin part 1
    cnt = passwd.count(char) # count how many times char appears in the password
    return((strt <= cnt) & (cnt <= stp)) # check whether the count is in the defined range


def checkLine_part2(strt, stp, char, passwd):
    # check whether line corresponds to a valid passwordin part 1
    val1 = passwd[strt-1] # password char @ position 1
    val2 = passwd[stp-1]  # ==     //      ==        2
    # a valid password is one where one password char matches the given char and the other one not (and vice versa => therefore two conditions combined via OR)
    res = ((val1 == char) and (val2 != char)) or ((val1 != char) and (val2 == char))
    return(res)


# we want to parse the format used in AoC 2020, day 2

# this matches one line
grmr_line = Word(nums) + "-" + Word(nums) + Word(alphas) + ":" + Word(alphas)

cnt_part1 = 0
cnt_part2 = 0


f = open('AoC_2020_P02_input.txt')
#f = open('AoC_2020_P02_test.txt')

for line in f:
    res = grmr_line.parseString(line)
    # print(res)
    chk_part1 = checkLine_part1(int(res[0]), int(res[2]), res[3], res[5])
    chk_part2 = checkLine_part2(int(res[0]), int(res[2]), res[3], res[5])
    print(chk_part2)
    if(chk_part1 == True):
        cnt_part1 = cnt_part1 + 1
    if(chk_part2 == True):
        cnt_part2 = cnt_part2 + 1

f.close()

print(cnt_part1)
print(cnt_part2)


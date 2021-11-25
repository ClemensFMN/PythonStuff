from pyparsing import Word, alphas, nums, alphanums, Optional, printables

# Idea #1: Use pyparsing to parse one passport
# We use & to combine the various key/value pairs in ANY order. Using + (AND) also considers the order and in this problem is order is NOT relevant!

# all 8 fields with CID optional
passprt_full = "byr:" + Word(printables) & "iyr:" + Word(printables) & "eyr:" + Word(printables) & "hgt:" + Word(printables) & "hcl:" + Word(printables) & "ecl:" + Word(printables) & "pid:" + Word(printables) & Optional("cid:" + Word(printables))


# here we are cheating a little as we have put every passprt in one line (see below)
test_str="""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in
"""

# passprt_full.runTests(test_str)

# actual start of problem

# parsing the file is a bit messy (as always :-))

data = []
# we get every (stripped) line into a list

#with open("AoC_2020_P04_test.txt") as file:
with open("AoC_2020_P04_input.txt") as file:
    data = [line.strip() for line in file]

# and add "" at the end
data.append("")

lines = []
s = ""    

# here we run through the list and accumulate entries into the string s. When we observe an empty string (a line break), we append s into to the result list (lines) and empty the string. Appending "" to data (done above) ensures that also the last block is written to lines.
for item in data:
    if item == "":
        lines.append(s)
        s = ""
    else:
        s += item.strip() + " "
        # print(s)

# print(lines)

# our counter for valid entries
cnt = 0

# run through all entries (one item = one entry) and trying to parse. If parsing passes, we increase the counter, if parsing fails, we do nothing...
for pprt in lines:
    try:
        res = passprt_full.parseString(pprt)
        cnt += 1
    except:
        pass

print(cnt)



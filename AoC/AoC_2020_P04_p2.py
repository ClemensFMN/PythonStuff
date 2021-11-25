from pyparsing import Word, alphas, nums, alphanums, Optional, printables, srange, Literal

# part 2 - an exercise in pyparsing :-)


def validation_byr(s, loc, tokens):
    # print("s:", s, "loc: ", loc, "tokens: ", tokens)
    year = int(tokens[0])
    if(1920 <= year <= 2002):
        return(True)
    else:
        return(False)


byr = "byr:" + Word(nums).addCondition(validation_byr)


byr_test = """byr: 1980
              byr: 1919
              byr: 2003
              byr: 12345
"""

# byr.runTests(byr_test)


def validation_iyr(s, loc, tokens):
    # print("s:", s, "loc: ", loc, "tokens: ", tokens)
    year = int(tokens[0])
    if(2010 <= year <= 2020):
        return(True)
    else:
        return(False)


iyr = "iyr:" + Word(nums).addCondition(validation_iyr)


def validation_eyr(s, loc, tokens):
    # print("s:", s, "loc: ", loc, "tokens: ", tokens)
    year = int(tokens[0])
    if(2020 <= year <= 2030):
        return(True)
    else:
        return(False)


eyr = "eyr:" + Word(nums).addCondition(validation_eyr)



def validation_hgt_cm(s, loc, tokens):
    if 150 <= int(tokens[0]) <= 193:
        return(True)
    return(False)

def validation_hgt_in(s, loc, tokens):
    if 59 <= int(tokens[0]) <= 76:
        return(True)
    return(False)


hgt_cm = Word(nums) + "cm"
hgt_cm.addCondition(validation_hgt_cm)
hgt_inch = Word(nums) + "in"
hgt_inch.addCondition(validation_hgt_in)

hgt = "hgt:" + (hgt_cm ^ hgt_inch) # brackets are required!

hgt_test = """hgt: 160cm
              hgt: 50cm
              hgt: 60in
              hgt: 40in
"""

# hgt.runTests(hgt_test) # careful, in this case the error messages are NOT right?!


hcl = "hcl:" + Word("#") + Word(srange("[a-f0-9]"), exact=6)

hcl_test = "#3a57bf"
# hcl.runTests(hcl_test)
#res = hcl.parseString(hcl_test)
#print(res)


ecl = "ecl:" + (Literal("amb") ^ Literal("blu") ^ Literal("brn") ^ Literal("gry") ^ Literal("grn") ^ Literal("hzl") ^ Literal("oth"))
ecl_test = "ecl:amb"
#res = ecl.parseString(ecl_test)
#print(res)

pid = "pid:" + Word(nums, exact=9)
pid_test = "002344567"
#res = pid.parseString(pid_test)
#print(res)


passport_full = byr & iyr & eyr & hgt & hcl & ecl & pid & Optional("cid:" + Word(printables))


# this is copied from part 1
# should be factored out :-)

with open("AoC_2020_P04_test2.txt") as file:
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
        res = passport_full.parseString(pprt)
        cnt += 1
    except:
        pass

print(cnt)

# debug
# this should parse

pass1_pid = "pid:087499704"
res = pid.parseString(pass1_pid)
print(res)

pass1_hgt = "hgt:74in"
res = hgt.parseString(pass1_hgt)
print(res)

pass1_ecl = "ecl:grn"
res = ecl.parseString(pass1_ecl)
print(res)

pass1_iyr = "iyr:2012"
res = iyr.parseString(pass1_iyr)
print(res)

pass1_eyr = "eyr:2030"
res = eyr.parseString(pass1_eyr)
print(res)

pass1_byr = "byr:1980"
res = byr.parseString(pass1_byr)
print(res)

pass1_hcl = "hcl:#623a2f"
res = hcl.parseString(pass1_hcl)
print(res)


pass1  = "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f"
res = passport_full.parseString(pass1)
print(res)


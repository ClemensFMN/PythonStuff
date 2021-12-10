with open("AoC_2020_P06_input.txt") as file:
    data = [line.strip() for line in file]

data.append("")

# Parse the data into list of groups
groups, group = [], []

for line in data:
    if line == "":
        groups.append(group)
        group = []
    else:
        group.append(line)

# part 1
# we join the answers from all persons in a group together - since we create a set, duplicates are removed :-)
answers = [set("".join(g)) for g in groups]
# count the length of each group
num_answers = [len(x) for x in answers]
# and sum it up...
print(sum(num_answers))

# part 2
# here we need to convert each "person" string into a set & intersect with the sets from all persons if the same group.
answers = [[set(x) for x in g] for g in groups]

lngth = 0

for grp in answers:
    print(grp)
    common_answers = set.intersection(*grp)
    lngth += len(common_answers)

print(lngth)

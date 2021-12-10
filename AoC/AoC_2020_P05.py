# a bit lazy today, so reusing https://github.com/0xVector/AdventOfCode2020/blob/master/day05.py

def get_seat_id(passport):
    # Row determination
    lower = 0  # F
    upper = 127  # B

    for i in range(7):
        mid = (lower + upper) / 2
        if passport[i] == "F":
            upper = int(mid)
        if passport[i] == "B":
            if not mid.is_integer():  # Dividing odd numbers produces float, add 1 to truncate correctly
                mid += 1
                lower = int(mid)
        row = lower

    # Col determination
    lower = 0  # L
    upper = 7  # R

    for i in range(7, 10):
        mid = (lower + upper) / 2
        if passport[i] == "L":
            upper = int(mid)
        if passport[i] == "R":
            if not mid.is_integer():
                mid += 1
                lower = int(mid)
        col = lower

    seat_id = row * 8 + col
    return(seat_id)



seat_ids = []

with open("AoC_2020_P05_input.txt") as file:
    data = [line.strip() for line in file]

# passport = "FBFBBFFRLR"

# iterate over all passports, calc the seat_id, and store it
for passport in data:
    sid = get_seat_id(passport)
    seat_ids.append(sid)

# part 1
# get max seat ID from all observed passports
print(max(seat_ids))

# part 2
# a bix more tricky... we sort the array and start with the first element (this way we ignore the first missing rows)
# funny example. we start with seat_id 4 & store the the first / smallest seat_id. iterate across the list and increase
# the stored seat_id. when the currently observed seat_id does not match the stored one, we have found the missing id.
# seat_ids = [4, 5, 6, 7, 8, 10, 11]

seat_ids.sort()

cur_id = seat_ids[0]
for sid in seat_ids:
    if(cur_id != sid): # we have found the gap -> we are done: cur_id contains out seat id
        break
    cur_id += 1

print(cur_id)

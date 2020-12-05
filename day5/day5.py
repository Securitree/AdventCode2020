#BFFFBBFRRR: row 70, column 7, seat ID 567.
#FFFBBBFRRR: row 14, column 7, seat ID 119.
#BBFFBBFRLL: row 102, column 4, seat ID 820.
'''
For example, consider just the last 3 characters of FBFBBFF RLR:

Start by considering the whole range, columns 0 through 7.

R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
'''


with open("input.txt","r") as f:
    data = f.readlines()
    
def part_one(data):
    boarding_id = 0
    boarding_list = []
    for line in data:
        row = find_row(line[:7])
        column = find_column(line[7:]) 
        tmp = (row * 8) + column
        boarding_list.append(tmp)
        if tmp > boarding_id:
            boarding_id = tmp
    return boarding_id, boarding_list
        
def find_row(line):
    rows = [0,127]
    for i in range (0,7):
        diff = rows[1]-rows[0]
        if line[i] == "F":
            rows[1] = rows[0] + (diff // 2)
        if line[i] == "B":
            rows[0] = rows[0] + (diff // 2) +1
    if line[i] == "F":
        return rows[0]
    else:
        return rows[1]

def find_column(line):
    columns = [0,7]
    for i in range (0,3):
        diff = columns[1]-columns[0]
        if line[i] == "L":
            columns[1] = columns[0] + (diff // 2)
        if line[i] == "R":
            columns[0] = columns[0] + (diff // 2) +1 
    if line[i] == "L":
        return columns[0]
    else:
        return columns[1]
        
def find_seat(boarding_id, boarding_list):
    boarding_set = set(boarding_list)
    for item in boarding_list:
        if (item != boarding_id) or (item+1 != boarding_id) or (item+2 != boarding_id):
            if item + 2 in boarding_set:
                if item +1 not in boarding_set:
                    return item+1
            if item -2 in boarding_set:
                if item -1 not in boarding_set:
                    return item-1

boarding_id, boarding_list = part_one(data)
#solution part 1
print (boarding_id)

#solution part 2
my_id = find_seat(boarding_id, boarding_list)
print (my_id)
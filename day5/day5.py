with open("input.txt","r") as f:
    data = f.readlines()
    
def find_id(data):
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
        if item + 2 in boarding_set:
            if item +1 not in boarding_set:
                return item+1
        if item -2 in boarding_set:
            if item -1 not in boarding_set:
                return item-1

boarding_id, boarding_list = find_id(data)
#solution part 1
print (boarding_id)

#solution part 2
my_id = find_seat(boarding_id, boarding_list)
print (my_id)

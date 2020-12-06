with open ("input.txt","r") as f:
     data = f.read().split("\n\n")

def create_set(item):
    item_set = set()
    for char in item:
        item_set.add(char)
    return item_set

def create_list(item):
    item_list = []
    for elem in item:
        item_list.append(elem)
    return item_list
    
def find_answers(item_list):
    sets = [set(x) for x in item_list] 
    common_answers = sets[0].intersection(*sets[1:])
    return (len(common_answers))
    
def anyone_yes(data):
    count = 0
    for item in data:
        item_set = create_set(item.replace("\n",""))
        count += len(item_set)
    return count

def everyone_yes(data):
    count = 0
    for item in data:
        item_list = create_list(item.split())
        common_answers = find_answers(item_list)
        count += common_answers
    return count



solution_one = anyone_yes(data)
print (solution_one)

solution_two = everyone_yes(data)
print (solution_two)
input_file = "input.txt"

values_one = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
values_two = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

with open (input_file,"r") as f:
	data = f.readlines()

def create_set(list):
	passport_set = set()
	for key_value in list:
	    (key,value) = key_value.split(':')
	    passport_set.add(key)
	return passport_set

def compare_sets(values_one, values_two,set_two):
	if (set(values_one) == set(set_two)) or (set(values_two) == set(set_two)):
		return True

def part_one(data):
	tmp = []
	valid = 0
	for line in data:
		if line != "\n":
			tmp = tmp + line.split()
		else:
			passport_set = create_set(tmp)
			if compare_sets(values_one, values_two,passport_set) == True:
				valid+=1
			tmp = []
	#check if last line is valid -- necessary if file doesn't terminate with \n
	passport_set = create_set(tmp)
	if compare_sets(values_one, values_two,passport_set) == True:
		valid+=1
	return valid


solution_one = part_one(data)
print (solution_one)

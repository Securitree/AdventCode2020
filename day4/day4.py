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


def check_fields(key,value):
	import re
	hgt_pattern = "\\d+(cm|in)"
	hcl_pattern = "#[a-f0-9]{6}"
	ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	pid_pattern = "\\d{9}"
	try:
		if key == "byr":
			if 1920 <= value <= 2002:
				return True
		if key == "iyr":
			if 2010 <= value <= 2020:
				return True
		if key == "eyr":
			if 20200 <= value <= 2030:
				return True
		if key == "hgt":
			if re.search(hgt_pattern, value):
				numbers,letters = re.split('(\\d+)',value)
				if ((letters == "cm") and ( 150 <= numbers <= 193)) or ((letters == "in") and ( 59 <= numbers <= 76)):
					return True
		if key == "hcl":
			if re.search(hcl_pattern, value):
				return True
		if key == "ecl":
			if value in ecl_list:
				return True
		if key == "pid":
			if re.search(pid_pattern, value):
				return True
	except:
		return False


solution_one = part_one(data)
print (solution_one)
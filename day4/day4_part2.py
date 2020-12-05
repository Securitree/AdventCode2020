input_file = "input.txt"

values_one = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
values_two = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

with open (input_file,"r") as f:
	data = f.readlines()

def create_set(tmp):
	passport_set = set()
	passport_dict = {}
	for key_value in tmp:
	    (key,value) = key_value.split(':')
	    passport_set.add(key)
	    passport_dict[key] = value
	return passport_set,passport_dict

def compare_sets(values_one, values_two,set_two):
	if (set(values_one) == set(set_two)) or (set(values_two) == set(set_two)):
		return True

def part_two(data):
	tmp = []
	valid = 0
	for line in data:
		if line != "\n":
			tmp = tmp + line.split()
		else:
			passport_set, passport_dict = create_set(tmp)
			if compare_sets(values_one, values_two,passport_set) == True:
				if check_fields(passport_dict) == True:
					#print (passport_dict)
					valid+=1
			tmp = []
	#check if last line is valid -- necessary if file doesn't terminate with \n
	passport_set,passport_dict = create_set(tmp)
	if compare_sets(values_one, values_two,passport_set) == True:
		if check_fields(passport_dict) == True:
			#print (passport_dict)
			valid+=1
	return valid


def check_fields(passport_dict):
	import re
	hgt_pattern = "\\d+(cm|in)"
	hcl_pattern = "#[a-f0-9]{6}"
	ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	pid_pattern = "\\d{9}"
	try:
		i = 0
		if 1920 <= int(passport_dict["byr"]) <= 2002:
			i+=1
		if 2010 <= int(passport_dict["iyr"]) <= 2020:
			i+=1           
		if 2020 <= int(passport_dict["eyr"]) <= 2030:
			i+=1
		if re.search(hgt_pattern, passport_dict["hgt"]):
			t,numbers,letters = re.split('(\\d+)',passport_dict["hgt"])
			if ((letters == "cm") and (150 <= int(numbers) <= 193)) or ((letters == "in") and (59 <= int(numbers) <= 76)):
				i+=1
		if re.search(hcl_pattern, passport_dict["hcl"]):
			i+=1
		if passport_dict["ecl"] in ecl_list:
			i+=1
		if len(passport_dict["pid"]) == 9 and passport_dict["pid"].isdigit():
			i+=1
		if i == 7:
			return True
	except Exception as e:
		print (e)
		return False

solution_one = part_two(data)
print (solution_one)
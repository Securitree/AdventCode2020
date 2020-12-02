import re

input_file = "input.txt"
pattern = "(\\d+)(?:-)(\\d+)(?: )([a-z])"

def part_one():
	valid_pwd = 0
	with open (input_file,"r") as f:
		for line in f:
			line = line.replace("\n","")
			x = re.search(pattern,line)
			min = int(x.group(1))
			max = int(x.group(2))
			letter = x.group(3)
			tmp = line.split(": ")
			occurrency = int(tmp[1].count(letter))
			if min <= occurrency <= max:
				valid_pwd+=1
	return(valid_pwd)


def part_two():
	valid_pwd = 0
	with open (input_file,"r") as f:
		for line in f:
			line = line.replace("\n","")
			x = re.search(pattern,line)
			min = int(x.group(1))
			max = int(x.group(2))
			letter = x.group(3)
			tmp = line.split(": ")
			word = tmp[1]
			if ((word[min-1] == letter) and (word[max-1] != letter)) or ((word[min-1] != letter) and (word[max-1] == letter)):
					valid_pwd+=1
	return(valid_pwd)


solution_one = part_one()
print (solution_one)

solution_two = part_two()
print (solution_two)
		

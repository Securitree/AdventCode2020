input_file = "input.txt"
total = 2020
number_list = []

with open (input_file,"r") as f:
	for line in f:
		number_list.append(int(line)) 
	number_set = set(number_list)

def part_one(number_list, number_set):
	for number in number_list:
		tmp = total - number
		if tmp in number_set:
			return(tmp * number)


def part_two(number_list, number_set):
	for i in range (0,len(number_list)):
		tmp_one = total - number_list[i]
		for j in range (i+1,len(number_list)):
			tmp = tmp_one - number_list[j]
			if tmp in number_set:
				return(tmp * number_list[i] * number_list[j])


solution_one = part_one(number_list, number_set)
print (solution_one)
solution_two = part_two(number_list, number_set)
print (solution_two)

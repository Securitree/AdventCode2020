input_file = "input.txt"
total = 2020
numbers = []

with open (input_file,"r") as f:
	for line in f:
		numbers.append(int(line)) 

def part_one(numbers):
	for number in numbers:
		tmp = total - number
		if tmp in numbers:
			return = tmp * number


def part_two(numbers):
	for i in range (0,len(numbers)):
		tmp_one = total - numbers[i]
		for j in range (i+1,len(numbers)):
			tmp = tmp_one - numbers[j]
			if tmp in numbers:
				return(tmp * numbers[i] * numbers[j])


solution_one = part_one(numbers)
print (solution_one)
solution_two = part_two(numbers)
print (solution_two)
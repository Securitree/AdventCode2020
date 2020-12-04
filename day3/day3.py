input_file = "input.txt"
right = 3

with open (input_file, "r") as f:
	data = f.readlines()

def part_one(data,right):
	i = 0
	trees = 0
	for line in data:
		i+=1
		if i == 1:
			continue
		for j in range(1,i):
			first = line[0:right]
			last = line [right:]
			line = (last+first).replace("\n","")
		if line[0] == "#":
			trees+=1
	return trees
    
def part_two(data,right):
	i = 1
	trees = 0
	for line in data:
		i+=1
		for j in range(1,i):
			first = line[0:right]
			last = line [right:]
			line = (last+first).replace("\n","")
		#print (i, line)
		if line[0] == "#":
			trees+=1
	return trees

#solution 1
solution_one = part_one(data,right)
print (solution_one)

#solution 2
r_items = [1,3,5,7]
solution_two = 1
for right in r_items:
	partial_solution = part_one(data,right)
	print (partial_solution)
	solution_two = solution_two * partial_solution

#keep from 3rd line to every 2 lines
data = data[2::2]
right = 1
partial_solution = part_two(data,right)
print (partial_solution)
solution_two = solution_two * partial_solution
print (solution_two)
		

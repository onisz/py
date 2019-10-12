import math 
numbers = [2, 4, 9, 16, 25]
j = []
for i in numbers:
	i = math.sqrt(i)
	j.append(i)
print(j)
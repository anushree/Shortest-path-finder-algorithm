#!/usr/bin/python
import sys

#Maze inputted
maze = ['S', '1', '1', '1', '1', '1', '0', '0', '0','0', '0', '1', '1', '0', '1', '0', '0', '0','0', '0', '1', '1', '1', '1', '0', '0', '0','0', '0', '0', '1', '1', '1', '0', '0', '0','0', '0', '0', '0', '1', '1', '0', '0', '1','0', '0', '0', '0', '0', '1', '1', '0', '0','0', '0', '0', '0', '0', '0', '1', '1', '0','0', '1', '0', '0', '0', '0', '1', '1', '0','0', '0', '0', '1', '0', '0', '0', '1', 'X']

#Parents of all nodes initialised to 0 originally
parent = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0, 0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0, 0,  0,  0, 0,  0,  0, 0]

#Queue initialised to 0
queue = [0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0, 0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0]

#Original maze displayed
print("Original Maze:\n")
for i in range(9):	
	for j in range(9):
		sys.stdout.write(maze[i * 9 + j])
		sys.stdout.write("\t")
	sys.stdout.write("\n")

lenq = 1
flag = 0
x = 0

#Performing BFS on the maze
while (lenq > 0 and flag == 0):
	x = queue[0]
	if (maze[x + 1] == '1'):
		queue[lenq] = x + 1 
		lenq = lenq + 1
		maze[x + 1] = 'W'
		parent[x + 1] = x
		print(x + 1)
	if (x + 9 < 80):
		if (maze[x + 9] == '1'):
			queue[lenq] = x + 9
			lenq = lenq + 1
			maze[x + 9] = 'W'
			parent[x + 9] = x
			print(x + 9)
	if (maze[x + 1] == 'X'):
		queue[lenq] = x + 1
		lenq = lenq + 1
		flag = 1
		parent[x + 1] = x
		print(x + 1)
	if (x + 9 < 80):
		if (maze[x + 9] == 'X' and x + 9 < 80):
			queue[lenq] = x + 9
			lenq = lenq + 1
			flag = 1
			parent[x + 9] = x
			print(x + 9)
	del queue[0]
	lenq = lenq - 1

#If a path is found it is displayed
if (flag == 1):
	x = parent[queue[lenq - 1]]
	while (x > 0):
		maze[x] = 'P'
		x = parent[x]
	print ("Solved maze\n")
	for i in range(9):
		for j in range(9):
			sys.stdout.write(maze[i * 9 + j])
			sys.stdout.write("\t")
		sys.stdout.write("\n")

#Output if path is not found
else:
	print "No path found"


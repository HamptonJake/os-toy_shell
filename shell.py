#! /usr/bin/env python3


import os
import sys
import re

#Get PID
pid = os.getpid()




#Print the prompt to the user for every entry until exit
while True:
	if 'PS1' not in os.environ:
		#print('PS1 not set.\nDefault prompt will be: $.')
		path = os.getcwd() + '$'
		#Print to standard out
		os.write(1, path.encode())
	else:
	
		os.environ['PS1']
		
		
	input_stream = os.read(0, 100).decode().split()
	print('input_stream: ' + str(input_stream))
	
	
	if 'exit' in input_stream:
		print('Closing Shell')
		sys.exit(0)
	elif input_stream[0] == 'cd':
		print('Attempt to change directory\n')
		try:
			os.chdir(input_stream[1])
			print('Path updated successfully')
		except:
			#print('Path does not exist or arguments missing')
			os.write(2, ('Path does not exist or arguments missing').encode())
		
	elif '|' in input_stream:
		print('Attempt to pipe\n')
		#Used to move data between commands
		#Command1 -> Command2
		#Separate both sides of the pipe
		split_pipe_sides = path.index("|")
		pip_write = [0:split_pipe_sides] #left side
		pip_read = [split_pipe_sides + 1:] #right side
		
		
		
print('Program Terminated')

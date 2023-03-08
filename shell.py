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
		pip_write = path[0:split_pipe_sides] #for writing
		pip_read = path[split_pipe_sides + 1:] #for reading
		# file descriptors r, w for reading and writing
		pip_r, pip_w = os.pipe() 
		
		#create the child process
		the_fork = os.fork()
		#This method returns an integer value representing child’s process id in the parent process while 0 in the child process.
		
		if the_fork = 0:
			#Child write
			
			
		if the_fork > 0:
			#Child read
			
			
		
		
		
print('Program Terminated')

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
		pip_write_path = path[0:split_pipe_sides] #for writing
		pip_read_path = path[split_pipe_sides + 1:] #for reading
		# file descriptors r, w for reading and writing
		pip_r, pip_w = os.pipe() 
		
		#create the child process
		the_fork = os.fork()
		#This method returns an integer value representing child’s process id in the parent process while 0 in the child process. (geeksforgeeks)
		
		
		if the_fork = 0:
			dup_fd_write = pip_w
			#Close previous write
			os.close(1)
			os.dup(dup_fd_write)
			os.set_inheritable(1, True)
			
			#exec
			for f_descript in (pip_w, pip_r)
				#executing
				for dir in re.split(':', os.environ['PATH']):
					executable = "%s/%s" % (dir, path[0])
					try:
						os.execve(executable, pip_write_path, os.environ)
					except:
						sys.exit(1)
			
		elif the_fork > 0:
			pipe_helper(pipe_read, pipe_write, r, 0)
			dup_fd_read = pip_r
			#Close previous read
			os.close(0)
			os.dup(dup_fd_read)
			os.set_inheritable(0, True)
			

			#exec
			for f_descript in (pip_w, pip_r)
				#executing
				for dir in re.split(':', os.environ['PATH']):
					executable = "%s/%s" % (dir, path[0])
					try:
						os.execve(executable, pip_read_path, os.environ)
					except:
						sys.exit(1)

		else:
			#Fork error
			sys.exit(1)
			
	else:
		#Redirect Section
		print('Redirection begins')

		redir_fork = os.fork()

		if redir_fork < 0:
			#Error
			sys.exit(1)

		elif redir_fork == 0:
			#Check directions of redirection
			if '>' in input_stream:
				# Redirect to fd1 output
				print('Redirect: >')
				os.close(1)
				#If file doesn't exist, create it
				os.open(input_stream[2], os.O_CREAT | os.O_WRONLY)
				# Inherit with flag code #1
				os.set_inheritable(1, True)
				input_stream = input_stream[:1]
			elif '<' in input_stream:
				# Redirect to fd1 output
				print('Redirect: <')
				os.close(0)
				os.open(input_stream[2], os.O_CREAT | os.O_WRONLY)
				# Inherit with flag code #0
				os.set_inheritable(0, True)
				input_stream = input_stream[:1]
			    # Search each directory in PATH
			
			for dir in re.split(":", os.environ['PATH']):
				redir_exectuable = "%s/%s" % (dir, path[0])
				try:
					os.execve()
			
		
		
		
print('Program Terminated')

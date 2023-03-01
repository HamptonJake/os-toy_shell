#! /usr/bin/env python3


import os
import sys
import re

#Get PID
pid = os.getpid()



#Print the prompt to the user for every entry until exit
while True:
	if 'PS1' not in os.environ:
		print('PS1 not set.\nDefault prompt will be: $.')
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
		
		
		
print('Program Terminated')

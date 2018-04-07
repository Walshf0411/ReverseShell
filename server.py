from socket import *
import sys
# create the socket 
def create_socket():
	try:
		global host
		global port
		global s

		host="127.0.0.1"
		port=9999
		s=socket()
	except:
		print("Socket creation error has occured"+s.error)
# bind the port and the IP to the socket
def bind_socket():
	try:
		global host
		global port
		global s
		print("Binding port and IP to socket")
		s.bind((host, port))
		s.listen(5)
	except:
		print("Socket Binding error...Retrying")
		bind_socket()

#Listen for connections
def socket_listen():
	global host
	global port
	global s

	conn, addr = s.accept()
	print("Connection established with host with IP "+addr[0]+" and port "+str(addr[1]))
	send_commands(conn)
	conn.close()

def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'exit':
			conn.close()
			s.close()
			sys.exit()
		if len(cmd.encode())>0:
			conn.send(cmd.encode())
			client_response=str(conn.recv(1024), 'utf-8')
			print(client_response, end="")


def main():
	create_socket()
	bind_socket()
	socket_listen()

main()


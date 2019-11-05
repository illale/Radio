import socket
import time
import zipfile

VERSION_NUMBER = "0.0.1"

def init_socket(HOST, PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s

def receive_data(conn):
    data = conn.recv(4096)
    VER = data.decode()
    if (VER == VERSION_NUMBER):
        cn = conn.recv(1024)
        print(cn.decode())
    else:
        conn.sendall(str.encode("OLD"))
            for i in range(0, 1):
                data = conn.recv(1024)
                name = data.decode()
                with open(name, "w") as target:
                    while True:
                        data = conn.recv(1024)
                        data_txt = data.decode()
                        print(data_txt)
                        if (data_txt == "DONE"):
                            print("Done")
                            break
                            target.write(data_txt)

def parse_file():
    with open("load.txt", "a"):
        return

if __name__ == '__main__':
    conn = init_socket("127.0.0.1", 2225)
    receive_data(conn)

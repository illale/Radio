import socket
import threading
from _thread import start_new_thread
import time
import zipfile

VERSION_NUMBER = "0.0.2"

def init_server(HOST, PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    return s

def send_new_files(soc, file_name, conn):
    return

def handle_client(conn):

    conn.sendall(str.encode(VERSION_NUMBER))
    b_resp = conn.recv(1024)
    resp = b_resp.decode()

    if (resp == "OLD"):
        with zipfile.ZipFile("AAA.zip") as zip:
            for name in zip.namelist():
                if len(name) == 0:
                    continue
                else:
                    conn.sendall(str.encode(name))
                    with open(name, "rb") as source:
                        while True:
                            data = source.read(1024)
                            if (len(data) == 0):
                                print("Sleeping...")
                                time.sleep(10)
                                print("Waking up")
                                print("Done")
                                conn.sendall(str.encode(""))
                                conn.sendall(str.encode("DONE"))
                                break
                            conn.sendall(data)

    elif (resp == "UPD"):
        conn.sendall(str.encode("CNT"))
    return

def main():
    ss = init_server("127.0.0.1", 2225)
    ss.listen(5)
    print("Server || Waiting for connection...")
    while True:
        connection, addr = ss.accept()
        print("Server || {} connected", addr)
        start_new_thread(handle_client, (connection,))

if __name__ == '__main__':
    main()

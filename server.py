import os
import socket
from Crypto.PublicKey import RSA
import RSA as rsa
decryptedStr = ""
Key = None

def server_program():

    rsa.RsaGenerateKey()
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(3048)
        if not data:
            break

        if (os.path.isfile("key.pem")):
            f = open('key.pem', 'r')
            Key = RSA.import_key(f.read())
            decryptedStr = rsa.RsaDecrypt(data, Key)

        print("from connected user: " + str(decryptedStr.decode("utf-8")))

        data = input(' -> ')
        encryptedMsg = rsa.RsaEncrypt(data.encode(), Key.public_key())
        conn.send(encryptedMsg)

    conn.close()



if __name__ == '__main__':
    server_program()

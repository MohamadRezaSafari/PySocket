import os
import socket
import RSA as rsa
from Crypto.PublicKey import RSA
encryptKey = ""
decryptedStr = ""

def client_program():

    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != 'bye':

        if (os.path.isfile("key.pem")):
            f = open('key.pem', 'r')
            encryptKey = RSA.import_key(f.read())

        encryptedMsg = rsa.RsaEncrypt(message.encode(), encryptKey.public_key())
        client_socket.send(encryptedMsg)


        data = client_socket.recv(3048)
        if (os.path.isfile("key.pem")):
            f = open('key.pem', 'r')
            Key = RSA.import_key(f.read())
            decryptedStr = rsa.RsaDecrypt(data, Key)
        print('Received from server: ' + str(decryptedStr.decode("utf-8")))

        message = input(" -> ")

    client_socket.close()


if __name__ == '__main__':
    client_program()

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def RsaGenerateKey():

    keyPair = RSA.generate(1024)

    f = open('key.pem', 'wb')
    f.write(keyPair.export_key('PEM'))
    f.close()

    return keyPair

def RsaEncrypt(txt, key):
    pubKey = key.publickey()
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(txt)
    return encrypted


def RsaDecrypt(encryptedTxt, key):
    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(encryptedTxt)
    return decrypted
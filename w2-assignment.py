
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter


def decryptCBC(k,enc):
    iv = enc[:16]
    enc= enc[16:]
    cipher = AES.new(k, AES.MODE_CBC, iv )
    return cipher.decrypt(enc)

def decryptCTR(k,enc):
	block_size = AES.block_size
	iv = enc[:block_size]
	ctr = Counter.new(128, initial_value = long(iv.encode("hex"), block_size))
	enc = enc[block_size:]
	cipher = AES.new(k, AES.MODE_CTR, counter = ctr)
	plaintext = cipher.decrypt(enc)
	return plaintext

ciphertext = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
ciphertext = ciphertext.decode('hex')
key = '140b41b22a29beb4061bda66b6747e14'
key = key.decode('hex')
plaintext = decryptCBC(key,ciphertext)
print "MESSAGE 1 :%s" % plaintext

ciphertext = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'
ciphertext = ciphertext.decode('hex')
plaintext = decryptCBC(key,ciphertext)
print "MESSAGE 2 :%s" % plaintext


ciphertext = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
ciphertext = ciphertext.decode('hex')
key = '36f18357be4dbd77f050515c73fcf9f2'
key = key.decode('hex')
plaintext = decryptCTR(key, ciphertext)
print "MESSAGE 3 :%s" % plaintext


ciphertext = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'
ciphertext = ciphertext.decode('hex')
plaintext = decryptCTR(key, ciphertext)
print "MESSAGE 4 :%s" % plaintext
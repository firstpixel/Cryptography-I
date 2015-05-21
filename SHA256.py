import sys
from Crypto.Hash import SHA256


piece_size = 1024 # 1 KiB
block = 0
dataArray = []
with open("./6 - 1 - Introduction (11 min).mp4", "rb") as input:
    while True:
        data = input.read(piece_size)
        if data == "":
        	block = block-1
        	break
    	dataArray.append(data)  
    	block += 1


blockTotal = block


blockSha256 = ""
while block >= 0: 
	if blockTotal == block: 
		blockSha256 = SHA256.new(dataArray[block])
	else:
		newBlock = dataArray[block]+blockSha256.digest()
		blockSha256 = SHA256.new(newBlock)
	
	block -= 1	


print(blockSha256.hexdigest())

            

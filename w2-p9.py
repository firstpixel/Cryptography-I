k = ['0011','0101','1100','1100','0101'] #random key, the result is not the solution
#x = '1101'
def F(k,x):
	t = k[0]
	for i in range(4):
		#print "i:",i
		#print "x:",x[i]
		if x[i]=='1':
			t = bin(int(t,2) ^ int(k[i+1],2))[2:].zfill(4)
	return t

x = '0110'
print ':', x
print ' ', F(k,x)
y = '0101'
print ':',y
print ' ', F(k,y)
z = '1110'
print ':',z
print ' ', F(k,z)
j = '1101'
print ':',j
print ' ', F(k,j)
import sys

f1= open(sys.argv[1],"r")
f2 = open(sys.argv[2],"r")
f3 = open(sys.argv[3],"w")
z = f1.read()
y = f2.read()


z1 = '<GetResult xmlns:b="http://schemas.datacontract.org/SomeFormat" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">'
z2 = '</GetResult>'


x = f3.write(z[:z.find(z2)] + y[y.find(z1)+len(z1):y.find(z2)] + z[z.find(z2):])


# front
# print z[z.find(z2)]

# content
# print z[z.find(z1)+len(z1):z.find(z2)]

f3.close()
f2.close()
f1.close()

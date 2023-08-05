


f = open("portfolio.dat")

listofdata=[]

for line in f:
    listofdata.append(line.split(' '))
print (listofdata)

stockprice=0
for data in listofdata:
    stockprice+=float(data[1])*float(data[2])
print (stockprice)
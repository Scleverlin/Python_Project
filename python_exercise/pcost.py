


f = open("portfolio.dat")

listofdata=[]
i=0
for line in f:
    listofdata.append(line.split(' '))
print (listofdata)

for data in listofdata:
  data[2].replace('\n','')
  print(data[2])

stockprice=0
for data in listofdata:
    stockprice+=float(data[1])*float(data[2])
print (stockprice)
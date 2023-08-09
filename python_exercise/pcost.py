


# f = open("portfolio.dat")

# listofdata=[]

# for line in f:
#     listofdata.append(line.split(' '))
# print (listofdata)

# stockprice=0
# for data in listofdata:
#     stockprice+=float(data[1])*float(data[2])
# print (stockprice)

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        for line in f:
            fields = line.split()
            try:
                nshares    = int(fields[1])
                price      = float(fields[2])
                total_cost = total_cost + nshares*price

            # This catches errors in int() and float() conversions above
            except ValueError as e:
                print("Couldn't parse:", repr(line))
                print("Reason:", e)

    return total_cost

print(portfolio_cost('./portfolio3.dat'))
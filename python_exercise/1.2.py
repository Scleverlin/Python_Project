a=7/4
print (a)
print (a.as_integer_ratio())
print (a.is_integer())
a=7//4
print (a)
print (a.as_integer_ratio())
a=2.2
print (a.is_integer()) # only for float, not for int


symbols = 'AAPL IBM MSFT YHOO SCO' 
symbols += ' GOOG' # concatenation of strings
symbols = 'HPQ ' + symbols  # concatenation of strings
print (symbols)
# for i in range(len(symbols)):
#     print (symbols[i])
#     print (symbols[i:i+1])
a='IBM' in symbols # check if a string is in another string
print (a)
a='AA' in symbols
print (a)

lower_symbols = symbols.lower() # convert to lower case
print (lower_symbols)

print (symbols.find('MSFT')) # find the index of a substring
print (symbols[13:17]) # slicing a string

symbols = symbols.replace(' ','n') # replaced string is in front, latter string is for replacement 
print (symbols)

symbols = symbols.replace('n',' ') # replaced string is in front, latter string is for replacement 
print (symbols)

symlist = symbols.split() # split a string into a list based on the space/seperator
print (symlist)

for sym in symlist: # iterate over a list, itearation is not able to be run on a number, must be a list
    print (sym)

symlist[2] = 'AIG' # replace a list element

a='AIG' in symlist
print (a)

a='IBM' in symlist
print (a)

a='AA' in symlist
print (a)

a='AAPL' in symlist
print (a)

symlist.append('RHT')

print (symlist)
symlist.remove('MSFT')
print (symlist)
symlist.sort()
print (symlist) # sort a list in alphabetical order
symlist.sort(reverse=True)
print (symlist) # sort a list in reverse alphabetical order

nums = [101,102,103]
items = [symlist, nums]

print (items)

print (items[0][2]) # print the 3rd element of the 1st list in the list of lists
print (items[0][2][1]) # print the 2nd letter of the 3rd element of the 1st list in the list of lists

for i in range(len(items)):
    # print (items[i])
    if i==0:
        for oneitem in items[i]:
            for i in range(len(oneitem)):
                print (oneitem[i])
    elif i==1:
        for oneitem in items[i]:
            print (oneitem)

#Dictionary

prices = { 'IBM': 91.1, 'GOOG': 490.1, 'AAPL':312.23 }

print (prices['IBM']) # print the value of the key 'IBM'

prices['IBM'] = 123.45 # change the value of the key 'IBM'
prices['HPQ'] = 26.15       # add a new key-value pair

print (prices)

print (list(prices)) # print the keys of the dictionary, default is keys
print (list(prices.keys())) # print the keys of the dictionary
print (list(prices.values())) # print the values of the dictionary
         
        
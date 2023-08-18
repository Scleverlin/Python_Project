import numpy as np

def AND_gate (x1,x2):
    w1,w2,theta=0.5,0.5,0.9
    y=w1*x1+w2*x2
    if y<=theta:
        return 0
    else :
        return 1

for i , j in [(0,0),(0,1),(1,0),(1,1)]:
    y=AND_gate(i,j)
    print(str(i)+" AND "+str(j)+" = "+str(y))    

x=np.array([[0,1],[2,3]])
w=np.array([0.5,0.6])
b=-0.7
print (x@w)
print (np.dot(x, w))
print(w*x) #Hadamard Product (element-wise product)
print(np.sum(w*x))# numpy.sum() is a function that sums the every element of an array.
print(np.sum(w*x)+b)

def AND_gate_with_offset (x1,x2): # AND gate with offset
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    y=np.sum(w*x)+b
    if y<=0:
        return 0
    else :
        return 1
    
for i , j in [(0,0),(0,1),(1,0),(1,1)]:
    y=AND_gate(i,j)
    print(str(i)+" AND "+str(j)+" = "+str(y))   
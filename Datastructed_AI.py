import numpy as np
app = np.linspace(2.0, 3.0, num=10)
print(app)
#-----------------------------------------------

c= np.array([[
    [1,2], 
    [3,4],
    [5,6], 
    [7,8]]])

a = np.array([1,2,3])
b = 10
print(a+b)

#Broadcast

a1=np.tile(np.arange(0,40,10),(3,2))
print(a1)
print(a1.shape)


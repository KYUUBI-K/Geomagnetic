import numpy as np
import matplotlib.pyplot as plt

X = [1,5,9]
Pi = [0.5,0.25,0.25]
plt.plot(X,Pi)
plt.grid()
plt.show()
first = np.arange(X[0]-4,X[0]+1)
second=np.arange(X[0],X[1]+1)
third=np.arange(X[1],X[2]+1)
fourth = np.arange(X[2],X[2]+5)
print(first)
print(second)
print(third)
print(fourth)


M1=[]
for i in range(first.size):
    M1.append(Pi[0])
plt.plot(first,M1)
M2=[]
for i in range(second.size):
    M2.append(Pi[1])
plt.plot(second,M2)
M3=[]
for i in range(third.size):
    M3.append(Pi[2])
plt.plot(third,M3)
M4=[]
for i in range(fourth.size):
    M4.append(1)
plt.plot(fourth,M4)
plt.grid()
plt.show()


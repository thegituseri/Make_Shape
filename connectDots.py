import matplotlib.pyplot as plt
import numpy as np
import random


X = []
Y = []

corners = random.randint(4, 50)
for i in range(corners):
    X.append(random.randint(1, 100))
    Y.append(random.randint(1,100))

X = np.array(X)
Y = np.array(Y)


for i in range(len(X)):
    for j in range(len(X)):
        if X[i] < X[j]:
            temp = X[i]
            X[i] = X[j]
            X[j] = temp
            temp = Y[i]
            Y[i] = Y[j]
            Y[j] = temp


max_index = np.argmax(Y)
min_index = np.argmin(Y)
A = Y[max_index] - Y[min_index]
B = X[min_index] - X[max_index]
C = X[max_index] * Y[min_index] - X[min_index] * Y[max_index]

RX = []
RY = []
LX = []
LY = []
for i in range(len(X)):
    sum = A * X[i] + B * Y[i] + C
    if sum >= 0:
        RX.append(X[i])
        RY.append(Y[i])
    elif sum < 0:
        LX.append(X[i])
        LY.append(Y[i])

RX = np.array(RX)
RY = np.array(RY)
LX = np.array(LX)
LY = np.array(LY)

for i in range(len(LY)):
    for j in range(len(LY)):
        if LY[i] > LY[j]:
            temp = LX[i]
            LX[i] = LX[j]
            LX[j] = temp
            temp = LY[i]
            LY[i] = LY[j]
            LY[j] = temp

for i in range(len(RY)):
    for j in range(len(RY)):
        if RY[i] < RY[j]:
            temp = RX[i]
            RX[i] = RX[j]
            RX[j] = temp
            temp = RY[i]
            RY[i] = RY[j]
            RY[j] = temp


X = np.concatenate((LX, RX))
Y = np.concatenate((LY, RY))
X = np.append(X, X[0])
Y = np.append(Y, Y[0])
plt.scatter(X,Y)
plt.plot(X,Y)
plt.show()

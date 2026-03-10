import matplotlib.pyplot as plt
import random as rnd

n = int(input("Ingresa el número de elementos aleatorios a los que quieres aplicar regresión lineal: "))
X = []
Y = []

for i in range(n):
    X.append(rnd.random())
    Y.append(rnd.random())


# Sum x * y | Sum x | Sum y
sum_XpY = 0
sum_X2 = 0
sum_X = 0
sum_Y = 0
for i in range(n):
    sum_XpY = sum_XpY + (X[i] * Y[i])
    sum_X2 = sum_X2 + X[i]**2
    sum_X = sum_X + X[i]
    sum_Y = sum_Y + Y[i]
    
## || PENDIENTE (m) ||##
m = ((n * sum_XpY) - (sum_X * sum_Y)) / ((n * sum_X2) - (sum_X**2))
    
## || CORTE EN Y (b) ||##

b = ((sum_Y * sum_X2) - (sum_X * sum_XpY)) / ((n * sum_X2) - (sum_X**2))

Y2 = []
for i in X:
    Y2.append(i*m + b)

plt.plot(X, Y, "g*", X, Y2, "r-")
plt.show()
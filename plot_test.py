import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-5,5,0.1)

p = 0.5
y1 = p*((1-x)**2)
y2 = p*((1-x)**2 + (1-x))
y3 = (1-x)

def base(x):
    res =[]
    for item in x:
        if item>=0:
            res.append(0)
        else:
            res.append(1)
    return res
y4 = base(x)
plt.figure()

ax = plt.gca()

# plt.plot(x,y1,label ="y=x^2")
plt.plot(x,y2,label="y = x^2+x")
plt.plot(x,y3,label="hinge loss")
plt.plot(x,y4,label="0-1 loss")

plt.legend()

plt.show()




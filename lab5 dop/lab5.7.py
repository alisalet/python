import matplotlib.pyplot as plt
import numpy as np

data=np.genfromtxt('data.csv',delimiter=',')
x=data[:,0]
y=data[:,1]

plt.scatter(x,y,color='#40a6e6',s=75,label='Данные')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График зависимости x от y')
plt.grid(True,alpha=0.5)
plt.legend()
plt.show()
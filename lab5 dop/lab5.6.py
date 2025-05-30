import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig,ax=plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_xlim(0,10)
ax.set_ylim(-1.2,1.2)
ax.set_title('Анимация графика sin(x)')

x=np.linspace(0,10,100)
y=np.sin(x)

line,=ax.plot([],[],color='#40a6e6')
point,=ax.plot([],[],'o',color='#3c7ee8')

def init():
    line.set_data([],[])
    point.set_data([],[])
    return line,point

def animation(i):
    line.set_data(x[:i],y[:i])
    point.set_data([x[i-1]],[y[i-1]])
    return line,point

a=FuncAnimation(fig,animation,frames=len(x),init_func=init,interval=10,repeat=False)

plt.show()
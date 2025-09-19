import numpy as np
import matplotlib.pyplot as plt

x=y=np.linspace(-5, 5, 100)
X,Y=np.meshgrid(x, y)
Z=np.sin(np.sqrt(X**2 + Y**2))

fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.plot_surface(X,Y,Z,cmap='plasma')
ax.set_title('z=sin(sqrt(x^2 + y^2))')
plt.show()
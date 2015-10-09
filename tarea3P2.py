import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D

#P2
#Def funcion
def AtractorDeLorenz(t,xyz):
    x, y, z=xyz
    dx=10*(y-x)
    dy=x*(p-z)-y
    dz=x*y-b*z
    return [dx, dy, dz]
#Condiciones iniciales
o=10
b=8/3
p=28
x=[float(input('X inicial?'))]
y=[float(input('Y inicial?'))]
z=[float(input('Z inicial?'))]
xyz0=[x,y,z]

#Integracion utilizando ode, con dopri5
r=ode(AtractorDeLorenz)
r.set_integrator('dopri5', max_step=0.01)
r.set_initial_value(xyz0,0) 
#Fijar tiempo
t=np.linspace(0, 30, 10000)
#Iteraciones integrando, donde se agrega cada termino nuevo al x, y, z.
N=1#Variable auxiliar para contar las iteraciones
while N<10000:
    r.integrate(t[N-1])
    N+=1
    x.append(r.y[0])
    y.append(r.y[1])
    z.append(r.y[2])
#Variables usadas para los plot
xp=x[0]
yp=y[0]
zp=z[0]
#Plots
fig=plt.figure(1)
fig.clf()
ax=fig.add_subplot(111,projection='3d')
ax.set_aspect('equal')
ax.plot(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('$Atractor$ $de$ $Lorentz$ $con$ $(X_0, Y_0, Z_0)=$'+'$('+str(xp)+',$'+' $'+str(yp)+',$'+' $'+str(zp)+')$')
fig.savefig('Atractor('+str(xp)+', '+str(yp)+', '+str(zp)+').png')
plt.show()

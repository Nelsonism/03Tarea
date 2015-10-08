import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate 
from mpl_toolkits.mplot3d import Axes3D

#P2

def VanDerPool(y, dy):
    return dy, -y-u*((y**2)-1)*dy

def k1(Xn, Yn, f):
    F=f(Xn, Yn)
    return h*F[0], h*F[1]

def k2(Xn, Yn, f):
    K1=k1(Xn, Yn, f)
    F=f(Xn+(h/2), Yn+(1/2)*K1[1])
    return h*F[0], h*F[1]

def k3(Xn, Yn, f):
    K1=k1(Xn, Yn, f)
    K2=k2(Xn, Yn, f)
    F=f(Xn+h, Yn-K1[1]-2*K2[1])
    return h*F[0], h*F[1]

def RK3(Xn, Yn, f):
    K1=k1(Xn, Yn, f)
    K2=k2(Xn, Yn, f)
    K3=k3(Xn, Yn, f)
    Xn1=Xn+(1/6)*(K1[0]+4*K2[0]+K3[0])
    Yn1=Yn+(1/6)*(K1[1]+4*K2[1]+K3[1])
    return Xn1, Yn1


u=1.312
Pasos=30000
h=20*np.pi/Pasos
T=np.linspace(0, 20*np.pi, Pasos)

#1)
y=[0.1]
dy=[0]
N=1
while N<Pasos:
    Yn1, dYn1 = RK3(y[N-1], dy[N-1], VanDerPool)
    N+=1
    y.append(Yn1)
    dy.append(dYn1)
y=np.asarray(y)
dy=np.asarray(dy)

plt.plot(T,y)
plt.xlabel('$s$')
plt.ylabel('$y(s)$')
plt.title('$y(s)$ para $\mu^* = 1.312$, $y(0)=0.1$, $dy/ds(0)=0$')
plt.show()
plt.savefig('ys1.eps')

plt.plot(y,dy)
plt.xlabel('$y(s)$')
plt.ylabel('$dy/ds(s)$')
plt.title('$y(s)$ para $\mu^* = 1.312$, $y(0)=0.1$, $dy/ds(0)=0$')
plt.show()
plt.savefig('ydy1.eps')

#2)
y=[4]
dy=[0]
N=1
while N<Pasos:
    Yn1, dYn1 = RK3(y[N-1], dy[N-1], VanDerPool)
    N+=1
    y.append(Yn1)
    dy.append(dYn1)
y=np.asarray(y)
dy=np.asarray(dy)

plt.plot(T,y)
plt.xlabel('$s$')
plt.ylabel('$y(s)$')
plt.title('y(s) para $\mu^* = 1.312$, $y(0)=4$, $dy/ds(0)=0$')
plt.show()
plt.savefig('ys2.eps')

plt.plot(y,dy)
plt.xlabel('$y(s)$')
plt.ylabel('$dy/ds(s)$')
plt.title('y vs dy/ds para $\mu^* = 1.312$, $y(0)=4$, $dy/ds(0)=0$')
plt.show()
plt.savefig('ydy2.eps')

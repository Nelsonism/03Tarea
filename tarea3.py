import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate 
from mpl_toolkits.mplot3d import Axes3D

u=1.312

def VanDerPool(y, dy):
    return dy, -y-u*((y**2)-1)*z

def k1(Xn, Yn, h, f):
    F=f(Xn, Yn)
    return h*F[0], h*F[1]

def k2(Xn, Yn, h, f):
    K1=k1(Xn, Yn, h, f)
    F=f(Xn+(h/2), Yn+(1/2)*K1[1])
    return h*F[0], h*F[1]

def k3(Xn, Yn, h, f):
    K1=k1(Xn, Yn, h, f)
    K2=k2(Xn, Yn, h, f)
    F=f(Xn+h, Yn-K1[1]-2*K2[1])
    return h*F[0], h*F[1]

def RK3(Xn, Yn, h, f):
    K1=k1(Xn, Yn, h, f)
    K2=k2(Xn, Yn, h, f)
    K3=k3(Xn, Yn, h, f)
    Xn1=Xn+(1/6)*(K1[0]+4*K2[0]+K3[0])
    Yn1=Yn+(1/6)*(K1[1]+4*K2[1]+K3[1])
    return Xn1, Yn1

Pasos=30000
h=20*np.pi/Pasos

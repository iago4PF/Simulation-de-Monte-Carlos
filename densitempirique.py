import numpy as np
from numpy.random import rand
from math import *
import matplotlib.pyplot as plt
#import matplotlib.colors as colors

Nmc=13
Y=[0,0,0,0,1,1,1,2,2,2,3,3,3]
a=0
b=20
Nx=100
deltax=(b-a)/Nx

def Densite_empirique(Y,a,Nx):
    x=[]
    proba=[]
    for i in range (0,Nx):
        x.append(a+deltax*i)
        counter=0
        for n in range(0,Nmc):
            if((Y[n]>x[i]) and (Y[n]<=x[i]+deltax)):
                counter=counter+1
                
        proba.append(counter/Nmc)
    return (proba)
        
    
probabilite=Densite_empirique(Y,a,Nx)

fig=plt.figure
plt.plot(probabilite)

        
    
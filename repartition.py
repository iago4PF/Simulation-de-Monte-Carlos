import numpy as np
from numpy.random import rand
from math import *
import matplotlib.pyplot as plt
#import matplotlib.colors as colors

Nmc=13
Y=[0,0,0,0,1,1,1,2,2,2,3,3,3]
taille=13
a=0
b=3
Nx=100
deltax=(b-a)/Nx

def Repartiton(Y,a,Nx):
    X=[]
    proba=[]
    for i in range(0,Nx):
        
        X.append(a+deltax*i)
        counter=0
        
        for n in range(0,taille):
            if (Y[n]<=X[i]):
                counter=counter+1
                
        proba.append(counter/taille)
        
    return(proba)

probabilite=Repartiton(Y,a,Nx)

fig=plt.figure
plt.plot(probabilite)

        
    
import numpy as np
from numpy.random import rand
from math import *
import matplotlib.pyplot as plt
#import matplotlib.colors as colors


lambd=5.0
Nmc=60
a=0.0



def V_A_Poisson(lambd):
    n=0
    proba=exp(-lambd)
    F=proba
    U=rand()
    while U>F:
        proba=proba*lambd/(n+1)
        F=F+proba
        n=n+1
    return n

def Chaine_Valeurs_Poisson(lambd,Nmc):
    esp=0
    var=0
    X=[]
    for n in range(0,Nmc):
        X.append(V_A_Poisson(lambd))
        esp=esp+X[n]
        var=var+(X[n]*X[n])
    return (X,esp,var)
esperance=0
variance=0
(Y,esperance,variance)=Chaine_Valeurs_Poisson(lambd, Nmc)

esperance=esperance/Nmc
variance=variance/Nmc-esperance*esperance

print(Y)
print("Esperance empirique")
print(np.mean(Y))

print("Esperance theorique")
print(lambd)
print()
print("Variance empirique")
print(variance)
print(np.std(Y)*np.std(Y))

print("Variance theorique")
print(lambd)


fig=plt.figure()

   
plt.plot(Y)
plt.plot(np.mean(Y),"r")
import numpy as np
from numpy import zeros, linspace
from numpy.random import rand
from math import *
import matplotlib.pyplot as plt
import matplotlib.colors as colors


lambd=10.0
Nmc=1000
a=0.0
delta=0.2
print ("delta :",delta)

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
    X=zeros(Nmc)
    for n in range(0,Nmc):
        X[n]=V_A_Poisson(lambd)
    return X

Y=Chaine_Valeurs_Poisson(lambd,Nmc)

"""print(Y)"""

def Densite_MC(Y,a,delta,Nmc):
    N_x=100
    x=zeros(N_x)
    p=zeros(N_x)
    for i in range(0,N_x):
        x[i]=a+delta*i
        counter=0.0
        for n in range(0,Nmc):
            if (Y[n]>=x[i]) and (Y[n]<x[i]+delta):
                counter=counter+1
            p[i]=counter/Nmc
        
    plt.figure()
    plt.plot(x,p)
    
Densite_MC(Y,a,delta,Nmc)

def Repartition_MC(Y,a,delta,Nmc):
    N_x=100
    x=zeros(N_x)
    p=zeros(N_x)
    for i in range(0,N_x):
        x[i]=a+delta*i
        counter=0.0
        for n in range(1,Nmc):
            if Y[n]< x[i]:
                counter=counter+1
            
        p[i]=counter/Nmc
        
    fig=plt.figure()
    plt.plot(x,p,"r")
    
Repartition_MC(Y,a,delta,Nmc)

print("Esperance empirique :",np.mean(Y))
print("Variance empirique :", np.std(Y)*np.std(Y))
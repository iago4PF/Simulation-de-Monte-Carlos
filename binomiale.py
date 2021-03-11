import numpy as np
from numpy import zeros, linspace
from numpy.random import rand
from math import *
import matplotlib.pyplot as plt
import matplotlib.colors as colors

N=20
p=0.5
Nmc=1000
delta=0.5
a=0

def V_A_Binomiale(p,N):
    k=0
    proba=pow((1-p),N)
    F=proba
    U=rand()
    while(U>F):
        proba=proba*(p*(N-k))/((1-p)*(k+1))
        F=F+proba
        k=k+1
    return k

def Chaine_Valeurs_Binomiale(p,N,Nmc):
    X=zeros(Nmc)
    for n in range(0,Nmc):
        X[n]=V_A_Binomiale(p,N)
    return X

Y=Chaine_Valeurs_Binomiale(p,N,Nmc)

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
print("Esperance theorique :",N*p)
print()
print("Variance empirique :",np.std(Y)*np.std(Y))
print("Variance theorique :",N*p*(1-p))
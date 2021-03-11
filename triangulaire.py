import numpy as np
from numpy import zeros, linspace
from numpy.random import rand
from math import *
import matplotlib.pyplot as plt
import matplotlib.colors as colors

Nmc=1000000;
a=0
delta=0.03;

def V_A_Triangulaire():

    U=rand()
    F=0
    if U<=1.0/2:
        F=sqrt(2*U)
    else:
        F=2-sqrt(2*(1-U))
    return F
        
def Chaine_Valeurs_Triangulaire(Nmc):
    
    X=zeros(Nmc)
    for n in range(0,Nmc):
        X[n]=V_A_Triangulaire()
    return X

Y=Chaine_Valeurs_Triangulaire(Nmc)
#print(Y)

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
            p[i]=counter/(Nmc*delta)
        
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


print("esperance empirique :",np.mean(Y))
print("esperance theorique : 1" )
print()
print("variance empirique :",np.std(Y)*np.std(Y))
print("variance theorique : 0.166666", )
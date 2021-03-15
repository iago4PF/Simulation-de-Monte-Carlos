import numpy as np
from numpy import zeros, linspace
from numpy.random import rand
from math import *
import matplotlib.pyplot as plt
import matplotlib.colors as colors

alph=2.0
bet=3.0
Nmc=10000
a=-0.05
delta=0.05
#print(delta)

def V_A_Gamma(alph,bet):
    i=0
    U=rand()
    F= -(log(1-U))/(bet)
    while i<alph:
        u=rand()
        F+=-(log(1-u))/(bet)
        i=i+1
    return F

def Chaine_Valeurs_Gamma(alph,bet,Nmc):
    X=zeros(Nmc)
    for n in range(0,Nmc):
        X[n]=V_A_Gamma(alph,bet)
    return X

Y=Chaine_Valeurs_Gamma(alph,bet,Nmc)
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
print("esperance theorique :" ,alph/bet)
print()
print("variance empirique :",np.std(Y)*np.std(Y))
print("variance theorique :", alph/(bet*bet))

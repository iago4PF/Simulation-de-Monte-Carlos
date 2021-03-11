import numpy
from numpy import zeros, linspace
from numpy.random import rand
from math import *
import matplotlib.pyplot as plt
import matplotlib.colors as colors

lambd=5.0
Nmc=1000
a=0.0
delta=0.2



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

def Repartition_MC(Y,a,delta,Nmc):
    Nx=50
    x=zeros(Nx)
    p=zeros(Nx)
    for i in range(0,Nx):
        x[i]=a+delta*i
        counter=0.0
        for n in range(0,Nmc):
            if(Y[n]>=x[i] and Y[n]<x[i]+delta):
                counter=counter+1
            p[i]=counter/Nmc
        
    return(x,p)
    
Repartition_MC(Y,a,delta,Nmc)


def Densite_MC(Y,a,delta,Nmc):
    Nx=50
    x=zeros(Nx)
    p=zeros(Nx)
    for i in range(0,Nx):
        x[i]=(a+delta*i)
        counter=0.0
        for n in range(0,Nmc):
            if( Y[n]<x[i]):
                counter=counter+1
        p[i]=(counter/Nmc)       
    return(x,p)


(x1,p1)=Repartition_MC(Y,a,delta,Nmc)

(x2,p2)=Densite_MC(Y,a,delta,Nmc)

fig=plt.figure
plt.plot(x1,p1,"r")
plt.plot(x2,p2)


        
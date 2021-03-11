import numpy as np
from numpy.random import rand
from math import *
import matplotlib.pyplot as plt
#import matplotlib.colors as colors

p=[0.25,0.3,0.1,0.18,0.05,0.08,0.02,0.02]
a=[1,2,3,4,5,6,7,8]

Nmc=50
print("sum des p[i] =",sum(p))
print()


def V_A_Discrete(p,a):
    n=0
    F=p[0]
    U=rand()
    while U>F:
        F=F+p[n+1]
        n=n+1
    return a[n]

def Chaine_Valeurs_V_A(p,a,Nmc):
    esp=0
    var=0
    X=[]
    for n in range (0,Nmc):
        X.append(V_A_Discrete(p,a))
        esp=esp+X[n]
        var=var+(X[n]*X[n])
    return (X,esp,var)
    

esperance=0.0
variance=0.0
(Y,esperance,variance)=Chaine_Valeurs_V_A(p,a,Nmc)
print("Chaine aléaroire =",Y)
print()
print("esperance empirique =", esperance/Nmc)
print()
#print(esperance/Nmc)
#print(np.mean(Y))
print("variance empirique =",variance/Nmc-(esperance/Nmc)*(esperance/Nmc))
#print(variance/Nmc-(esperance/Nmc)*(esperance/Nmc))

#test

def Occurrence(a):
    n=0
    for i in range(0,Nmc):
        if (Y[i]==a):
            n=n+1
    return n
"""
b=8
print("occurrence de ",b,"=",Occurrence(b))
    
c=7
print("occurrence de ",c,"=",Occurrence(c))
    

print(p[1])

"""

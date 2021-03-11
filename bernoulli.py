from numpy.random import rand
import matplotlib.pyplot as plt

#fonction qui calcule la fréquence d'apparition
def Frequence(Nmc):
    counter1=0.0
    counter2=0.0
    x=[]
    
    for n in range(0,Nmc):
        u=rand()
        
        if u<1/3.0:
            x.append(1)
            counter1=counter1+1
        else:
            x.append(0)
            counter2=counter2+1
    prob1=counter1/Nmc
    prob2=counter2/Nmc
    return (prob1,prob2)

Nmc_lim=1000
#test
a=[]
for i in range(0,500):
    a.append(i)
#fin test

proba1=[]
proba2=[]

for Nmc in range (1, Nmc_lim+1):
    y=Frequence(Nmc)
    proba2.append(y[1])
    proba1.append(y[0])
    
fig = plt.figure()

plt.plot(proba1)
plt.plot(proba2,"r")
#plt.plot(a,"g")
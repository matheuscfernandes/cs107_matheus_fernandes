def numbers(type,N):
    #ASSERITING TO MAKE SURE THAT N IS ALWAY GRATER THAN 0 BEFORE RUNNING FUNCTION
    assert N>0, 'N has to be greater than 0'
    #COMPUTING PI BASED ON INFINITE SUM
    if type == 'pi':
        pi=0
        #COMPUTING THE SUM OF RHS TERM
        for n in range(1,N+1):
            pi+=1/(n**2)
        #MOVING THINGS FROM LHS TERM TO GET PI BY ITSELF
        pi=pi*6
        pi=pi**(1/2)
        return pi
    
    #COMPUTING THE GOLDEN RATIO SECTION
    elif type == 'goldenratio':
        #INITIALIZING THE SEQUENCE FOR FIRST TWO CASES
        F=[1,1]
        #FOR CASE OF N=1
        if N==1:
            fib=F[0]
        #FOR CASE OF N=2
        elif N==2:
            fib=F[1]
        #FOR ANY CASE PF n>2
        else:
            #LOOP TO CREATE THE SEQUENCE
            for n in range(2,N):
                F.append(F[-1]+F[-2])
            #COMPUTING THE RATIO BASED ON THE LAST TWO ENTRIES OF THE SEQUENCE
            fib=F[-1]/F[-2]
        return fib
    #DEALING WITH CASE OF PASSING A STRING THAT IS UNACCOUNTED FOR    
    else:
        print("Type not programmed in! Please check the series in question.")

#INITIALIZING THE DIFFERENT LISTS
plist=[*range(15,1001)]
glist=[*range(3,11)]

#COMPUTING THE CORRESPONDING PIES FOR THE LIST
pies=[]
for i in plist:
    pies.append(numbers('pi',i))
goldens=[]

#COMPUTING THE CORRESPONDING GOLDENS FOR THE LIST
for j in glist:
    goldens.append(numbers('goldenratio',j))

import matplotlib.pyplot as plt
import numpy as np


# PLOTTING FIGURE FOR PI SEQUENCE
plt.figure()

plt.axhline(np.pi,c='k',ls='--',label=r'True $\pi$')
plt.plot(plist,pies,'o',label=r'Series Approximation')

plt.title(r'Pi Series approximation compared to True Value')
plt.xlabel(r'Approximate $\pi$')
plt.ylabel(r'Number of terms')

plt.legend()
plt.savefig('PiEstimation.png',dpi=300)

#COMPUTING TRUE GOLDEN RATIO
truefib=(1./2.)*(1+np.sqrt(5))


# PLOTTING FIGURE FOR GOLDEN MEAN SEQUENCE
plt.figure()

plt.axhline(truefib,c='k',ls='--',label=r'True $\varphi$')
plt.plot(glist,goldens,'o',label=r'Series Approximation')

plt.title(r'Golden Ratio Series approximation compared to True Value')
plt.xlabel(r'Approximate $\varphi$')
plt.ylabel(r'Number of terms')

plt.legend()
plt.savefig('GoldenEstimation.png',dpi=300)
#I made some change

#THIS PROGRAM CALCULATES THE VALUE OF DIFFERENT DISK RADII FOR A RANGE OF VALUES OF MASS 
#OF HALO AND DIFFERENT SPIN PARAMETERS

import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import save_figure
import os


#print os.getcwd()

def Disk_Scale_Radius(M_vir,Zcol,s_para):
    "This funcion is for calculating the disk scale radius of the galactic disk"

    H0 = 2.27e-18;G = 6.7e-11;pi = 4.0*math.atan(1.0)
    
    r_vir = (1.26*10e9)*(((2*G*M_vir)/(18*(pi**2)*(H0**2)))**(1.0/3.0))*((1+Zcol)**(-1))
    
    R_d = ((1.0/math.sqrt(2.0))*s_para*(r_vir)) 

    return R_d



#DEFINE THE SPIN PARAMETER FOR SPIN=0.05

SPIN=0.05

count = 0
colors = plt.get_cmap("gist_rainbow")(np.linspace(0,1,15))

for Z in range(0,3,1):
    R1=[]
    M1=[]
    for M in np.linspace(8,16,15):
         
         R_kpc = math.log(Disk_Scale_Radius(10**(M),Z,SPIN)/(3.086e+19),10)
         R1.append(R_kpc)
         M1.append(M)
         
    plt.plot(M1,R1,'--', linewidth='3', color = colors[count],label='z = %1.2f'%(Z))
    count +=1
    plt.grid(True)
    ll = plt.legend(loc='upper left')
    plt.xlabel("log$M_{vir}(M_0)$")
    plt.ylabel("log($R_d$ (kpc))")
 

save_figure.save("M_{vir}vs_R_d_for_Z", ext="png", close=False, verbose=True)



#CODE FOR DIFFERENT SPIN PARAMETER BUT REDSHIFT = 0

Z = 0.0

SPIN_PARA= np.linspace(0.01,0.09,8)

del M1[:]
del R1[:]

count = 0
colors = plt.get_cmap("gist_rainbow")(np.linspace(0,1,len(SPIN_PARA)))
plt.figure(2)
for SPIN in SPIN_PARA:
	R1 = []
	M1 = []
	for M in np.linspace(8,16,15):
        	R_kpc = math.log(Disk_Scale_Radius(10**(M),Z,SPIN)/(3.086e+19),10)
        	R1.append(R_kpc)
                M1.append(M)
	plt.plot(M1,R1,'--', linewidth='3', color = colors[count],label='%1.3f'%(SPIN))
	count +=1
	plt.grid(True)
        ll = plt.legend(loc='upper left')
        plt.xlabel("log$M_{vir}(M_0)$")
        plt.ylabel("$log(R_d$ (kpc))")
        #plt.set_yscale('log')
        plt.title("log($M_{vir})$ vs Disk Radius ($R_d$) for different spin parameter")

save_figure.save("M_vir_vs_R_d_for_lambda", ext="png", close=False, verbose=True)






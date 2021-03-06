import numpy as np
import math as m
from numpy.polynomial.legendre import leggauss
from scipy.special import legendre
import matplotlib.pyplot as plt
from scipy.special import spherical_jn
from scipy.interpolate import interp1d

class OBEpot:
   print("Include >>OBEpot<< by Dr. Nogger in functions.py. We can't provide it because of copyright conflicts")

    
class TwoBody:
    print("Include >>TwoBody<< by Dr. Nogger in functions.py. We can't provide it because of copyright conflicts")

# set up set of equations and calculate eigenvalues 

    def eigv(self,E,neigv):
       print("Include >>eigv<< by Dr. Nogger in functions.py. We can't provide it because of copyright conflicts")

    
    def esearch(self,neigv=1,e1=-0.01,e2=-0.0105,elow=0.0,tol=1e-8):
        print("Include >>esearch<< by Dr. Nogger in functions.py. We can't provide it because of copyright conflicts")
           
    def fourier(self,wfp):
        print("Include >>fourier<< by Dr. Nogger in functions.py. We can't provide it because of copyright conflicts")
    
    
    def rms(self,wfr):
        print("Include >>rms<< by Dr. Nogger in functions.py. We can't provide it because of copyright conflicts")

def beauty_plot():
    plt.figure(figsize=(10,5))
    plt.minorticks_on()
    plt.rcParams["mathtext.fontset"]="cm"
    plt.rcParams['errorbar.capsize'] = 3
    plt.rcParams['mathtext.rm'] = 'serif'
    font={'family' : 'serif','size'   : 22}
    plt.rc("font",**font)
    plt.xticks(fontsize=22,fontname='DejaVu Serif')
    plt.yticks(fontsize=22,fontname='DejaVu Serif')
    plt.grid(color='black',linestyle=':')    

def trafo(np1,np2,pa,pb,pc):
    print("Include >>trafo<< by Dr. Nogger in functions.py. We can't provide it because of copyright conflicts")

# Simple script to calculate halo/subhalo mass functions from hdf5                                                                                            
#                                                                                                                                                             
# Below run gives mass functions of the Micro-Uchuu simulation at z=0                                                                                         
# python uchuu_h5_mfunc.py MicroUchuu_halolist_z0p00.h5 mfunc.pdf                                                                                             

import numpy as np
import matplotlib.pyplot as plt
import h5py
import sys

args = sys.argv
inputfile = args[1]
outputfile = args[2]

hf = h5py.File( inputfile, 'r')
mvir = np.array( hf['Mvir'])
pid = np.array(hf['pid'])
hf.close()

mvir_halo =  mvir[pid==-1]
mvir_subhalo =  mvir[pid!=-1]

bins0 = np.logspace( 8, 16, 33)
n_halo, bins = np.histogram( mvir_halo, bins=(bins0))
n_subhalo, bins = np.histogram( mvir_subhalo, bins=(bins0))

mbins = np.zeros_like(n_halo)
for i in range( len(bins)-1):
    mbins[i] =  np.sqrt( bins[i] * bins[i+1])

plt.xscale("log")
plt.yscale("log")
plt.plot( mbins, n_halo, "o-", label="halo")
plt.plot( mbins, n_subhalo, "s-", label="subhalo")
plt.legend()
plt.savefig( outputfile)

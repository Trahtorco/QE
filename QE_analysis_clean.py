#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import scipy

from matplotlib.colors import LogNorm
from scipy import stats 
from astropy.io import fits

plt.style.use('dark_background')


# In[2]:


wavelengths = np.array([310, 325, 340, 365, 385, 400, 465, 525, 590, 628])

for i in wavelengths:
    for j in range(0, 10):
        locals()["qhy" + str(i) + '_' + str(j+1) + 's'] = fits.open('./qe_data/qhy' + str(i) + '_' + str(j+1) + 's.fts')
        locals()["qhydata" + str(i) + '_' + str(j+1) + 's'] = locals()["qhy" + str(i) + '_' + str(j+1) + 's'][0].data
        locals()["qhy" + str(i) + '_' + str(j+1) + 's'].close()
        locals()["qhymed" + str(i) + '_' + str(j+1) + 's'] = np.median(locals()["qhydata" + str(i) + '_' + str(j+1) + 's'])
    locals()["qhyx" + str(i)] = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    locals()["qhyy" + str(i)] = np.array([locals()["qhymed" + str(i) + '_1s'], locals()["qhymed" + str(i) + '_2s'], locals()["qhymed" + str(i) + '_3s'], locals()["qhymed" + str(i) + '_4s'], locals()["qhymed" + str(i) + '_5s'], locals()["qhymed" + str(i) + '_6s'], locals()["qhymed" + str(i) + '_7s'], locals()["qhymed" + str(i) + '_8s'], locals()["qhymed" + str(i) + '_9s'], locals()["qhymed" + str(i) + '_10s']])
    locals()["qhycoef" + str(i)] = np.polyfit(locals()["qhyx" + str(i)], locals()["qhyy" + str(i)], 1)
    locals()["qhypoly1d" + str(i)] = np.poly1d(locals()["qhycoef" + str(i)])
    locals()["qhyslope" + str(i)], locals()["qhyintercept" + str(i)], locals()["qhyrvalue" + str(i)], locals()["qhypvalue" + str(i)], locals()["qhystderr" + str(i)] = scipy.stats.linregress(locals()["qhyx" + str(i)], locals()["qhyy" + str(i)])


# In[ ]:


for i in wavelengths:
    for j in range(0, 10):
        locals()["pixis" + str(i) + '_' + str(j+1) + 's'] = fits.open('./qe_data/pixis' + str(i) + '_' + str(j+1) + 's.fts')
        locals()["pixisdata" + str(i) + '_' + str(j+1) + 's'] = locals()["pixis" + str(i) + '_' + str(j+1) + 's'][0].data
        locals()["pixis" + str(i) + '_' + str(j+1) + 's'].close()
        locals()["pixismed" + str(i) + '_' + str(j+1) + 's'] = np.median(locals()["pixisdata" + str(i) + '_' + str(j+1) + 's'])
    locals()["pixisx" + str(i)] = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    locals()["pixisy" + str(i)] = np.array([locals()["pixismed" + str(i) + '_1s'], locals()["pixismed" + str(i) + '_2s'], locals()["pixismed" + str(i) + '_3s'], locals()["pixismed" + str(i) + '_4s'], locals()["pixismed" + str(i) + '_5s'], locals()["pixismed" + str(i) + '_6s'], locals()["pixismed" + str(i) + '_7s'], locals()["pixismed" + str(i) + '_8s'], locals()["pixismed" + str(i) + '_9s'], locals()["pixismed" + str(i) + '_10s']])
    locals()["pixiscoef" + str(i)] = np.polyfit(locals()["pixisx" + str(i)], locals()["pixisy" + str(i)], 1)
    locals()["pixispoly1d" + str(i)] = np.poly1d(locals()["pixiscoef" + str(i)])
    locals()["pixisslope" + str(i)], locals()["pixisintercept" + str(i)], locals()["pixisrvalue" + str(i)], locals()["pixispvalue" + str(i)], locals()["pixisstderr" + str(i)] = scipy.stats.linregress(locals()["pixisx" + str(i)], locals()["pixisy" + str(i)])


# In[ ]:


qhypixel = 3.76**2 #pixel size is 3.76x3.76 micrometers
pixispixel = 20**2 #pixel size is 20x20 micrometers

qhygain = #number of electrons per ADU
pixisgain = 

for i in wavelengths:
    locals()["qhyelectron" + str(i)] = locals()["qhyslope" + str(i)]*qhygain/qhypixel #number of electrons per second per square micrometer for QHY
    locals()["pixiselectron" + str(i)] = locals()["pixisslope" + str(i)]*pixisgain/pixispixel #number of electrons per second per square micrometer for Pixis
    locals()["ratio" + str(i)] = locals()["qhyelectron" + str(i)]/locals()["pixiselectron" + str(i)] #electron ratio

ratios = np.array([ratio310, ratio325, ratio340, ratio365, ratio385, ratio400, ratio465, ratio525, ratio590, ratio628])


# In[ ]:


pixis_qe = np.array([34, 34, 34, 41, 65, 82, 92, 89, 90, 92])
qhy_qe = ratios*pixis_qe


# In[ ]:


plt.plot(wavelengths*10, qhy_qe, 'w.')
plt.xlabel(r'Wavelength $(\mathrm{\AA})$')
plt.ylabel(r'QHY600 Absolute QE $(\%)$')
plt.show()


# In[ ]:





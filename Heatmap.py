#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:44:55 2021

@author: Mathew
"""




import matplotlib.pyplot as plt
import numpy as np
from PIL import Image




# Change this to direct to the image of the brain (tif file in folder containing the script)
path_to_brain_image=r"/Users/Mathew/Documents/Edinburgh Code/PSD_heatmap/RegionsA.txt"

# Change to where you want images to be saved. 
path_to_save="/Users/Mathew/Documents/Edinburgh Code/PSD_heatmap/"



# Set values for image
olfactory_val=1
hippocampus_val=0.8
cerebellum_val=0.3
subcortex_val=0.5
isocortex_val=0.8

regionc_val=0

# set range
mini=0.2
maxi=1


# Set regions


olfactory=97
hippocampus=47
cerebellum=158
subcortex=242
isocortex=147

regionc=153
background=255
# Load the brain image
# brain=(path_to_brain_image)

brain=np.loadtxt(path_to_brain_image)

brain_orig=np.copy(brain)




# Set valueg
brain=np.copy(brain_orig)
brain_overlay=np.copy(brain)




brain_overlay[brain_overlay==0]=np.nan
brain_overlay[brain_overlay==background]=0
brain_overlay[brain_overlay==olfactory]=np.nan
brain_overlay[brain_overlay==hippocampus]=np.nan
brain_overlay[brain_overlay==cerebellum]=np.nan
brain_overlay[brain_overlay==subcortex]=np.nan
brain_overlay[brain_overlay==regionc]=0.5
brain_overlay[brain_overlay==isocortex]=np.nan





brain[brain==background]=np.nan
brain[brain==0]=0
brain[brain==olfactory]=olfactory_val
brain[brain==hippocampus]=hippocampus_val
brain[brain==cerebellum]=cerebellum_val
brain[brain==subcortex]=subcortex_val
brain[brain==regionc]=regionc_val
brain[brain==isocortex]=isocortex_val



# plt.figsize=(40,40)
plt.imshow(brain,cmap='Blues',vmin=mini,vmax=maxi)
plt.tick_params(left = False, right = False , labelleft = False,labelbottom = False, bottom = False)
plt.axis('Off')
plt.colorbar()
plt.imshow(brain_overlay,cmap='Greys',vmin=0,vmax=1)
# plt.imshow(brain_outline,cmap='Greys',vmin=0,vmax=1)
plt.savefig(path_to_save+"Figure.pdf",dpi=1000)

im = Image.fromarray(brain)
im.save(path_to_save+'test.tif')

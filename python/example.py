# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 08:21:50 2018

@author: hugo
"""

import numpy as np
import os
import SimpleITK as sitk

inputDir = '/input'
outputDir = '/output'

# Load the image
t1Image = sitk.ReadImage(os.path.join(inputDir, 'pre', 'reg_T1.nii.gz'))
t1Array = sitk.GetArrayFromImage(t1Image)

# Apply some simple thresholds
t1Array[t1Array < 10] = 0                       # Background
t1Array[(t1Array >=  10) & (t1Array <  80)] = 5 # CSF
t1Array[(t1Array >=  80) & (t1Array < 130)] = 1 # cGM
t1Array[(t1Array >= 130) & (t1Array < 150)] = 2 # BG
t1Array[(t1Array >= 150)] = 3                   # WM

resultImage = sitk.GetImageFromArray(t1Array)
resultImage.CopyInformation(t1Image)

sitk.WriteImage(resultImage, os.path.join(outputDir, 'result.nii.gz'))
######################################################################
# Strahinja Trecakov
# CIBC Developer Tasks - Required Task 3
#
# In python generate a script that will load in two 2D color images and
# evaluate the differences between them. The script must somehow 
# quantify the differences between images.
# You can use common python packages in you implementations (numpy,
# scipy, etc). Write some pytest code to test your implementations 
# with the included test data.
#
#######################################################################
import sys

import pytest
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average
from skimage.measure import compare_ssim as ssim

def main():
    # Read args
    arg0, arg1 = sys.argv[1:1+2]
    # Read images and converting them to 2D arrays 
    image1 = to_2D(imread(arg0).astype('float64'))
    image2 = to_2D(imread(arg1).astype('float64'))
    # Comparing images
    li, de, m, z, mse_, ssim_ = compare_images(image1, image2)
    print("-----Linalg Form-----:", li, "| per pixel:", li/image1.size)
    print("-----Euclidean Distance-----:", de, "| per pixel:", de/image1.size)
    print("-----Manhattan Norm-----:", m, "| per pixel:", m/image1.size)
    print("-----Zero Norm-----:", z, "| per pixel:", z*1.0/image1.size)
    print("-----Mean Squared Error-----: ", mse_)
    print("-----Structural Similarity Index-----: ", ssim_)

# Mean Squared Error
def mse(img1, img2):
    error = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
    error /= float(img1.shape[0] * img2.shape[1])
    return error

# Comparing images
def compare_images(img1, img2):
    difference = img1 - img2  # Calculating difference
    de_r = math.sqrt(sum((difference)**2)) # Euclidean distance
    linalg_r = np.linalg.norm(difference) # Linalg norm
    m_r = sum(abs(difference))  # Manhattan norm
    z_r = norm(difference.ravel(), 0)  # Zero norm 
    mse_r = mse(img1, img2)  # Mean Squared Error
    ssi_r = ssim(img1, img2) # Structural Similarity Index
    # Returning all norms
    return (linalg_r, de_r, m_r, z_r, mse_r, ssi_r)

# Converting to 2D array
def to_2D(array):
    # If 3D, convert to 2D
    if len(array.shape) == 3:
        return average(array, -1)  # average over the last axis (color channels)
    else:
        return array

# Tests
def test_all():
    # Loading images
    image1 = to_2D(imread("../test_data/2D_registration/w0.png").astype('float64'))
    image2 = to_2D(imread("../test_data/2D_registration/w1.png").astype('float64'))
    
    # Comparing images for pytest
    li, de, m, z, mse_, ssim_ = compare_images(image1, image2)
    li_e, de_e, m_e, z_e, mse_e, ssim_e = compare_images(image1, image1)
    
    # Euclidean distance of two different images, should not be equal to 0.0
    assert de != 0.0
    # Euclidean distance of identical images, should be equal to 0.0
    assert de_e == 0.0

    # Linalg norm of two different images, should not be equal to 0.0
    assert li != 0.0
    # Linalg norm of identical images, should be equal to 0.0
    assert li_e == 0.0   
   
    # Manhattan norm of two different images, should not be equal to 0.0
    assert m != 0.0
    # Manhattan norm of identical images, should be equal to 0.0
    assert m_e == 0.0
    
    # Zero norm of two different images, should not be equal to 0.0
    assert z != 0.0
    # Zero norm of identical images, should be equal to 0.0
    assert z_e == 0.0
    
    # mse of two different images, should not be equal to 0.0
    assert mse_ != 0.0
    # mse of identical images, should be equal to 0.0
    assert mse_e == 0.0
    
    # ssi of two different images, should be between -1.0 and 1.0
    assert ssim_ != 1.0
    # ssi of identical images, should be equal to 1.0
    assert ssim_e == 1.0

if __name__ == "__main__":
    main()

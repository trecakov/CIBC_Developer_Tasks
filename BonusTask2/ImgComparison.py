######################################################################
# Strahinja Trecakov
# CIBC Developer Tasks - Bonus Task 2
#
# Continuing from Required Task 3 above, create a Python function that will
# find the affine transformation between two sets of 2D or 3D correspondence 
# points.
# The affine transformation is a linear transformation and translation that
# can be expressed in a single matrix, 3x3 in the 2D case and 4x4 in the 3D
# case. See the Wikipedia page for more information. With a set of 
# corresponding points, the affine transformation can be found by solving 
# for the coefficients of the affine transformation in the least squared 
# sense.
# Create a Python function that will use the affine transformation calculated
# for 2D points to combine two images into one. Create some test code using 
# pytest.
#######################################################################
import sys

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
    transf(image1, image2)
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

# Affine transformation
def transf(img1, img2):
	
        rows, cols = img2.shape
        # Removing the end of the 1st image and begining of the 2nd image.
        M1 = np.float32([[1,0,-145],[0,1,5]])
        M2 = np.float32([[1,0,100],[0,1,5]])
        dst1 = cv2.warpAffine(rotation(img2),M1,(cols,rows))
        dst2 = cv2.warpAffine(img1,M2,(cols,rows))
        dst3 = cv2.warpAffine(img2,M1,(cols,rows))
        # Using numpy to combine arrays with axis 1 that they will be joined
        combined_wr = np.concatenate((dst2,dst1),axis=1)
        combined = np.concatenate((dst2,dst3),axis=1)
	# Image write
        cv2.imwrite('combined_with_rotation.png',combined_wr)
        cv2.imwrite('combined.png',combined)

# Image Rotation
def rotation(img):
        rows, cols = img.shape

        # Rotation
        M = cv2.getRotationMatrix2D((cols/2,rows/2),-4,1)
        dst = cv2.warpAffine(img,M,(cols,rows))
        return dst

if __name__ == "__main__":
    main()

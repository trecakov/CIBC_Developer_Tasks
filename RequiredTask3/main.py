#!/usr/bin/python
import os


print ("\nTesting ../test_data/2D_registration/w0.png and w1.png\n DIFFERENT IMAGES")
os.system ("python ImgComparison.py ../test_data/2D_registration/w0.png ../test_data/2D_registration/w1.png")

print ("\nTesting ../test_data/2D_registration/w0.png and w0.png\n SAME IMAGES")
os.system ("python ImgComparison.py ../test_data/2D_registration/w0.png ../test_data/2D_registration/w0.png")

print ("\nTesting ../test_data/diff_test/test_image_1.png and test_image_2.png\n DIFFERENT IMAGES")
os.system ("python ImgComparison.py ../test_data/diff_test/test_image_1.png ../test_data/diff_test/test_image_2.png")

print ("\nTesting ../test_data/diff_test/test_image_1.png and test_image_1.png\n SAME IMAGES")
os.system ("python ImgComparison.py ../test_data/diff_test/test_image_1.png ../test_data/diff_test/test_image_1.png")

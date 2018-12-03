This script loads 2 images and converts them to 2D array for easier comparison. 6 different ways of comparing the images are implemented..
1. Euclidean distance - (https://en.wikipedia.org/wiki/Euclidean_distance)
2. Linalg norm - (https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linalg.norm.html)
- This norm is the same as Euclidean distance, however, it is already builtin. 
3. Manhattan norm - (https://en.wikipedia.org/wiki/Norm_(mathematics)#Taxicab_norm_or_Manhattan_norm)
4. Zero norm -  (https://en.wikipedia.org/wiki/Norm_(mathematics)#Taxicab_norm_or_Manhattan_norm)
5. Mean Squared Error - (https://en.wikipedia.org/wiki/Mean_squared_error)
-  when MSE value is 0, it indicates perfect similarity.
6. Structural Similarity Measure - (https://en.wikipedia.org/wiki/Structural_similarity) 
- SSIM value are between -1 and 1, where 1 indicates perfect similarity.

To run the script type:
python ImgComparison.py <Img1> <Img2>

or to run test script:
python main.py

The example output:
Testing test_data/2D_registration/w0.png and w1.png
 DIFFERENT IMAGES
-----Linalg Form-----: 27518.32175115336 | per pixel: 0.11058996331321276
-----Euclidean Distance-----: 27518.32175115336 | per pixel: 0.11058996331321276
-----Manhattan Norm-----: 11170992.0 | per pixel: 44.89371141975309
-----Zero Norm-----: 247309.0 | per pixel: 0.9938794045781894
-----Mean Squared Error-----:  3043.2501929012346
-----Structural Similarity Index-----:  -0.004652714558784956

Testing test_data/2D_registration/w0.png and w0.png
 SAME IMAGES
-----Linalg Form-----: 0.0 | per pixel: 0.0
-----Euclidean Distance-----: 0.0 | per pixel: 0.0
-----Manhattan Norm-----: 0.0 | per pixel: 0.0
-----Zero Norm-----: 0.0 | per pixel: 0.0
-----Mean Squared Error-----:  0.0
-----Structural Similarity Index-----:  1.0



To run pytest that has assert tests for 2 cases(same and different image) and tests all 6 ways of comparing images, please type:
pytest ImgComparison.py

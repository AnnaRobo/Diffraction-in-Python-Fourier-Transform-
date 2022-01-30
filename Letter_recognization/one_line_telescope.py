import cv2
import numpy as np
#import scipy as sp
import matplotlib.pyplot as plt
plt.style.use(['seaborn-notebook'])
#import sympy as smp
#from skimage import color
#from skimage import io
#from scipy.fft import fftfreq
#from scipy.fft import fft, ifft, fft2, ifft2

img = cv2.imread('D:/PaAC Project/print_one_slit_2.png', cv2.IMREAD_GRAYSCALE)

#img = color.rgb2gray(io.imread('D:/PaAC Project/Final_Report/Red_E.jpg'))
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

#magnitude_spectrum = 20 * np.log(np.abs(fshift))
magnitude_spectrum = 20*(np.log(np.abs(fshift)))
magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
img_and_magnitude = np.concatenate((img, magnitude_spectrum), axis=1)

cv2.imwrite('single_slit_diffraction ' + 'image.png', img_and_magnitude)
cv2.imshow('Red_E', img_and_magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()

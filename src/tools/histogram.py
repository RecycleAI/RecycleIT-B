import sys
from email.mime import image
from fileinput import filename
from pickle import TRUE
import cv2
import numpy as np

def histogram_normalization(file_name , img , show_image=False):
    
    img = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
    #creating a Histograms Equalization
    #of a image using cv2.equalizeHist()
    img[:,:,0] = cv2.equalizeHist (img[:,:,0])
    equ = cv2.cvtColor(img, cv2.COLOR_YUV2BGR)
    cv2.imwrite (file_name , equ)
    

    if show_image == True:
        #stacking images side-by-side
        res = np.hstack ((img, equ))
    
        #show image input vs output
        cv2.imshow ("Image",res)

    
def load_images():
    file_name  = sys.argv [1]  

    #read a image using imread
    img = cv2.imread (file_name)
    return img 

def reduce_noise(input_img):
    output_img = cv2.GaussianBlur(input_img, (5,5), 0)
    return output_img


img = load_images()
histogram_normalization(sys.argv[1] , img )


#How to use : Enter the file address
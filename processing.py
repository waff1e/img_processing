import cv2
import numpy as np
import os


def resize(img, flag):

    src = cv2.imread(img)

    W, H = map(int, input('변경할 이미지의 크기를 입력(예:1920x1080)>>>').split('x'))
    
    dst = cv2.resize(src, dsize=(W,H), interpolation=cv2.INTER_LINEAR)
   
    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('resize', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    return dst, W, H


def gray_scale(img, flag):
   src = cv2.imread(img)
   dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

   if flag == 1:
       cv2.imshow('original', src)
       cv2.imshow('GrayScale', dst)
       cv2.waitKey(0)
       cv2.destroyAllWindows()
   
   return dst


def LR_reverse(img, flag):
    src = cv2.imread(img)
    dst = cv2.flip(src, 1)


    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('LR_reverse', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return src


def adaptive_Threshold(img, flag):
    src = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) 

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('adaptive_Threshold', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return dst

def onChange(x):
    pass

def canny_edge(img):
    src = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('canny')

    cv2.createTrackbar('low threshold', 'canny', 0, 255, onChange)
    cv2.createTrackbar('high threshold', 'canny', 0, 255, onChange)
    cv2.imshow('canny', src)

    while True:
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

        low = cv2.getTrackbarPos('low threshold', 'canny')
        high = cv2.getTrackbarPos('high threshold', 'canny')

        if low > high:
            print('low threshold 값은 high threshold 값 보다 작아야 합니다.')

        elif ((low == 0) & (high == 0)):
            cv2.imshow('canny', src)

        else:
            canny = cv2.Canny(src, low, high)
            cv2.imshow('canny', canny)

    cv2.destroyAllWindows()

def dilation_closing(img, flag):

    #src = cv2.imread(img)

    kernel = np.ones((5, 5), np.uint8)

    dilation = cv2.dilate(img, kernel, iterations=1)
#    closing1 = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)
    closing = cv2.erode(dilation, kernel, iterations=1)
    
    if flag == 1:
        #cv2.imshow('original', src)
        cv2.imshow('closing', closing)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return closing

def CLAHE(img, flag):

    src = gray_scale(img, 0)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_result = clahe.apply(src)

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('CLAHE', clahe_result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    return clahe_result

def gaussian_blurring(img, flag):
    src = cv2.imread(img)
    blur = cv2.GaussianBlur(src, (5,5), 0)

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('gaussian_blurring', blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return blur

def averaging_blurring(img, flag):
    src = cv2.imread(img)
    blur = cv2.blur(src, (5,5))

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('averaging_blurring', blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return blur

def median_blurring(img, flag):
    src = cv2.imread(img)
    blur = cv2.medianBlur(src, 5)

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('median_blurring', blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return blur

def sharpen(img, flag):
    src = cv2.imread(img)
    
    kernel1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1,]])
    kernel2 = np.array([[-1, -1, -1, -1, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, 2, 9, 2, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, -1, -1, -1, -1]]) / 9.0

    dst1 = cv2.filter2D(src, -1, kernel1)
    dst2 = cv2.filter2D(src, -1, kernel2)

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('sharpen', dst1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    return dst1

def bitwise_Xor(img, flag):
    src = gray_scale(img, 0)
    _, binary = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)

    xor = cv2.bitwise_xor(src, binary)
    
    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('XOR', xor)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return xor

def main():
    pass

if __name__ == "__main__":
    main()

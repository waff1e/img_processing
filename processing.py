import cv2
import numpy as np
import os




	# GrayScale 변환 유무 확인 후 변환
def check_Gray(src, isGrayScale):

    if not(isGrayScale):
        print(f'현재 isGrayScale:{isGrayScale}')
        src = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
        isGrayScale = 1

    return src, isGrayScale



    # RGB변환 유무 확인 후 변환
def check_Rgb(src, isRGB):

    if not(isRGB):
        src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        isRGB = 1

    return src, isRGB



def resize(src, W, H, flag, isRGB):
	
    dst = cv2.resize(src, dsize=(W,H), interpolation=cv2.INTER_LINEAR)
    dst, isRGB = check_Rgb(dst, isRGB)
   
    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('resize', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    return dst, isRGB



def gray_scale(src, flag):

    dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)		

    if flag == 1:
       #cv2.imshow('original', src)
       cv2.imshow('GrayScale', dst)
       cv2.waitKey(0)
       cv2.destroyAllWindows()
   
    return dst



def LR_reverse(src, flag, isRGB):

    dst = cv2.flip(src, 1)
    dst, isRGB = check_Rgb(dst, isRGB)

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('LR_reverse', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return dst, isRGB



def adaptive_Threshold(src, flag, isGrayScale):

    src, isGrayScale = check_Gray(src, isGrayScale)

    dst  = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) 

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('adaptive_Threshold', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return dst, isGrayScale



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




def canny_edge2(src, low_threshold, high_threshold, isGrayScale):

    low_threshold = low_threshold
    high_threshold = high_threshold

    src, isGrayScale = check_Gray(src, isGrayScale)
    canny = cv2.Canny(src, low_threshold, high_threshold)

    return canny, isGrayScale



def dilation_closing(src, flag, isRGB): # isRGB 변수 처리 하기

    kernel = np.ones((5, 5), np.uint8)

    dilation = cv2.dilate(src, kernel, iterations=1)
#    closing1 = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)
    closing = cv2.erode(dilation, kernel, iterations=1)
    closing, isRGB = check_Rgb(closing, isRGB)

    if flag == 1:
        #cv2.imshow('original', src)
        cv2.imshow('closing', closing)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return closing, isRGB



def CLAHE(src, flag, isGrayScale):

    src, isGrayScale = check_Gray(src, isGrayScale)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_result = clahe.apply(src)

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('CLAHE', clahe_result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    return clahe_result, isGrayScale



	# 가우시안 블러링
def gaussian_blurring(src, flag, isRGB):

    blur = cv2.GaussianBlur(src, (5,5), 0)
    blur, isRGB = check_Rgb(blur, isRGB)

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('gaussian_blurring', blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return blur, isRGB



	# 평균 블러링
def averaging_blurring(src, flag, isRGB):

    blur = cv2.blur(src, (5,5))
    blur, isRGB = check_Rgb(blur, isRGB)

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('averaging_blurring', blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return blur, isRGB



def median_blurring(src, flag, isRGB):

    blur = cv2.medianBlur(src, 5)
    blur, isRGB = check_Rgb(blur, isRGB)

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('median_blurring', blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return blur, isRGB



def sharpen(src, flag, isRGB):
    
    kernel1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1,]])
    kernel2 = np.array([[-1, -1, -1, -1, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, 2, 9, 2, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, -1, -1, -1, -1]]) / 9.0

    dst1 = cv2.filter2D(src, -1, kernel1)
    dst2 = cv2.filter2D(src, -1, kernel2)
	
    dst1, isRGB = check_Rgb(dst1, isRGB)

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('sharpen', dst1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    return dst1, isRGB



def bitwise_Xor(src, flag, isRGB):

    _, binary = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)

    xor = cv2.bitwise_xor(src, binary)
    xor, isRGB = check_Rgb(xor, isRGB)

    if flag == 1:
        cv2.imshow('original', src)
        cv2.imshow('XOR', xor)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return xor, isRGB








def main():
    pass

if __name__ == "__main__":
    main()

from processing import *
import sys
import os

def load_file(create_dirname, load_dirname):
    
    if not os.path.exists(create_dirname):
        os.mkdir(create_dirname)
    else:
        print('해당 디렉터리가 이미 존재합니다.')
        sys.exit()

    img_file = []
    
    for file_name in os.listdir(load_dirname):
        if file_name.endswith('.jpg'):
            img_file.append(file_name)
    img_file.sort()
    print(img_file)
    print(f'total:{len(img_file)}')

    return img_file


def first():
    
    img_file = load_file('1', 'img')
        
    W, H = map(int, input('변경할 이미지의 크기를 입력(예:1920x1080)>>>').split('x'))

    for i, file_name in enumerate(img_file):
        
        print(file_name)
        result = CLAHE(os.path.join('img', file_name), 0)

        result = cv2.resize(result, dsize=(W,H), interpolation=cv2.INTER_LINEAR)

        cv2.imwrite(f'1/{file_name}_resize+GrayScale+CLAHE.jpg', result)
        print('생성완료')


def second():

    img_file = load_file('2', 'img')

    for i, file_name in enumerate(img_file):
        
        print(file_name)
        gray = gray_scale(os.path.join('img', file_name),0)
        

        adt_result = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        result = dilation_closing(adt_result, 0)
        
        cv2.imwrite(f'2/{file_name}_Gray Scale+AdaptiveThreshold+dilation+closing.jpg', result)
        print('생성완료')

def third():

    img_file = load_file('3', 'img')

    for i, file_name in enumerate(img_file):
        
        print(file_name)
        sharpen_result = sharpen(os.path.join('img', file_name), 0)
        midanblur_result = median_blurring(os.path.join('img', file_name), 0)


        xor_result = cv2.bitwise_xor(sharpen_result, midanblur_result)
        and_result = cv2.bitwise_and(sharpen_result, midanblur_result)

        cv2.imwrite(f'3/{file_name}_SharpenAndMedianBlur_xor.jpg', xor_result)
        cv2.imwrite(f'3/{file_name}_SharpenAndMedianBlur_and.jpg', and_result)
        print('생성완료')

if __name__ == "__main__":
    first() 
    second()
    third()

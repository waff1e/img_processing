import cv2

src = cv2.imread('img/sample001.jpg')
print(f'src:{src.shape}')

(sb, sg, sr) = cv2.split(src)
print(f'sb{sb}, sg{sg}, sr{sr}')

#bgr = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
#print(f'bgr{bgr.shape}')

rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
print(f'rgb{rgb.shape}')

(rr, rg, rb) = cv2.split(rgb)
print(f'rr{rr}, rg{rg}, rb{rb}')

# cv2.imshow('src', src)
# cv2.imshow('rgb', rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
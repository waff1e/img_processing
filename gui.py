import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from processing import *
import qimage2ndarray

form_class = uic.loadUiType("img_processiong.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setFixedSize(850, 850)

		self.select_file = None
		self.input_text = None
		
		
		self.qPixmapVar1 = QPixmap()
		self.qPixmapVar1.load('img/empty.png')
		self.qPixmapVar1 = self.qPixmapVar1.scaledToWidth(400)
		self.display1.setPixmap(self.qPixmapVar1)


		self.qPixmapVar2 = QPixmap()
		self.qPixmapVar2.load('img/empty.png')
		self.qPixmapVar2 = self.qPixmapVar2.scaledToWidth(400)
		self.display2.setPixmap(self.qPixmapVar2)

		self.resize_button.clicked.connect(self.resizeFunc)
		self.gray_scale_button.clicked.connect(self.grayScaleFunc)
		self.LR_reverse_button.clicked.connect(self.lrReverseFunc)
		self.adaptive_Threshold_button.clicked.connect(self.adaptiveThresholdFunc)
		self.canny_button.clicked.connect(self.cannyFunc)
		self.dilation_closing_button.clicked.connect(self.dilationClosingFunc)
		self.CLAHE_button.clicked.connect(self.ClaheFunc)
		self.median_blurring_button.clicked.connect(self.medianBlurringFunc)
		self.gaussian_blurring_button.clicked.connect(self.gussianBlurringFunc)
		self.averaging_blurring_button.clicked.connect(self.averagingBlurringFunc)
		self.bitwise_xor_button.clicked.connect(self.bitwiseXorFunc)
		self.sharpen_button.clicked.connect(self.sharpenFunc)

		self.open_button.clicked.connect(self.imageLoad)
	

	def imageLoad(self):
		fileName, _ = QFileDialog.getOpenFileName(self, '불러올 이미지를 선택하세요','*.jpg')

		if fileName:
			self.select_file = fileName
			print(self.select_file)
			self.qPixmapVar1.load(self.select_file)
			self.qPixmapVar1 = self.qPixmapVar1.scaledToWidth(400)
			self.display1.setPixmap(self.qPixmapVar1)

		msg = os.path.basename(fileName) + ' 불러오기 완료'
		#self.select_file = frame[0]
		self.console.append(msg)

	def convertToPixmap(self, dst):
		
		dst = qimage2ndarray.array2qimage(dst, normalize=False)
		dst = QPixmap.fromImage(dst)

		self.qPixmapVar2 = dst
		self.qPixmapVar2 = self.qPixmapVar2.scaledToWidth(400)
		self.display2.setPixmap(self.qPixmapVar2)	
	
	def showDialog(self):
		text, ok = QInputDialog.getText(self, 'Input Dialog', '변경할 크기를 입력(1920x1080):')

		if ok:
			self.input_text = text

		return ok	

	def resizeFunc(self):
		status = self.showDialog()

		if status:
			W, H = self.input_text.split('x')
			W = int(W)
			H = int(H)
			resize(self.select_file, W, H, 0)
			self.console.append(f'사진의 크기가 {W}x{H}로 변경되었습니다.')

	def grayScaleFunc(self):
		dst = gray_scale(self.select_file, 0)

		dst = qimage2ndarray.array2qimage(dst, normalize=False)
		dst = QPixmap.fromImage(dst)

		self.qPixmapVar2 = dst
		self.qPixmapVar2 = self.qPixmapVar2.scaledToWidth(400)
		self.display2.setPixmap(self.qPixmapVar2)

	def	lrReverseFunc(self):
		dst = LR_reverse(self.select_file, 0)
		
		dst = qimage2ndarray.array2qimage(dst, normalize=False)
		dst = QPixmap.fromImage(dst)

		self.qPixmapVar2 = dst
		self.qPixmapVar2 = self.qPixmapVar2.scaledToWidth(400)
		self.display2.setPixmap(self.qPixmapVar2)
		
	def adaptiveThresholdFunc(self):
		dst = adaptive_Threshold(self.select_file, 0)
		
		dst = qimage2ndarray.array2qimage(dst, normalize=False)
		dst = QPixmap.fromImage(dst)

		self.qPixmapVar2 = dst
		self.qPixmapVar2 = self.qPixmapVar2.scaledToWidth(400)
		self.display2.setPixmap(self.qPixmapVar2)	
	
	def cannyFunc(self):
	#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@아직 구현 안됨 구현해야 함@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
		#dst = canny_edge()
		pass

	def dilationClosingFunc(self):
		dst = dilation_closing(self.select_file, 0)	
		self.convertToPixmap(dst)
	
	def ClaheFunc(self):
		dst = CLAHE(self.select_file, 0)
		self.convertToPixmap(dst)

	def medianBlurringFunc(self):
		dst = median_blurring(self.select_file, 0)
		self.convertToPixmap(dst)
	
	def gussianBlurringFunc(self):
		dst = gaussian_blurring(self.select_file, 0)
		self.convertToPixmap(dst)


	def averagingBlurringFunc(self):
		dst = averaging_blurring(self.select_file, 0)
		self.convertToPixmap(dst)

	def bitwiseXorFunc(self):
		dst = bitwise_Xor(self.select_file, 0)
		self.convertToPixmap(dst)

	def sharpenFunc(self):
		dst = sharpen(self.select_file, 0)
		self.convertToPixmap(dst)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()


"""
	반영할 사항들
	1.canny GUI로 구현
	2.각종 예외 처리들(지금 발견될 것은 세로로 긴 사진을 어떻게 짤리지 않게할지 처리하는 것)
	3.각 버튼들 위치 구성 다듬기
	4.저장 기능 추가
"""

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
		self.setFixedSize(850, 650)

		self.select_file = None
		self.input_text = None
		
		
		self.qPixmapVar1 = QPixmap()
		self.select_file = 'img/empty.png'
		self.qPixmapVar1.load(self.select_file)
		self.qPixmapVar1 = self.qPixmapVar1.scaledToHeight(300)
		self.display1.setPixmap(self.qPixmapVar1)


		self.qPixmapVar2 = QPixmap()
		self.qPixmapVar2.load('img/empty.png')
		self.qPixmapVar2 = self.qPixmapVar2.scaledToHeight(300)
		self.display2.setPixmap(self.qPixmapVar2)

		self.resize_button.clicked.connect(self.resizeFunc)
		self.gray_scale_button.clicked.connect(self.grayScaleFunc)
		self.LR_reverse_button.clicked.connect(self.lrReverseFunc)
		self.adaptive_Threshold_button.clicked.connect(self.adaptiveThresholdFunc)
		self.canny_button.clicked.connect(self.cannyFunc)
		self.dilation_closing_button.clicked.connect(self.dilationClosingFunc)
		self.CLAHE_button.clicked.connect(self.ClaheFunc)
		self.median_blurring_button.clicked.connect(self.medianBlurringFunc)
		self.gaussian_blurring_button.clicked.connect(self.gaussianBlurringFunc)
		self.averaging_blurring_button.clicked.connect(self.averagingBlurringFunc)
		self.bitwise_xor_button.clicked.connect(self.bitwiseXorFunc)
		self.sharpen_button.clicked.connect(self.sharpenFunc)

		self.open_button.clicked.connect(self.imageLoad)
		self.save_button.clicked.connect(self.saveImage)
	

	def imageLoad(self):
		fileName, _ = QFileDialog.getOpenFileName(self, '불러올 이미지를 선택하세요','*.jpg')
		if fileName and (fileName[-4:] ==  ".jpg"):
			self.qPixmapVar2.load('img/empty.png')
			self.qPixmapVar2 = self.qPixmapVar2.scaledToHeight(300)
			self.display2.setPixmap(self.qPixmapVar2)

			self.select_file = fileName
			print(self.select_file)
			self.qPixmapVar1.load(self.select_file)
			self.qPixmapVar1 = self.qPixmapVar1.scaledToHeight(300)
			self.display1.setPixmap(self.qPixmapVar1)

			msg = os.path.basename(fileName) + ' 불러오기 완료'
			self.console.append(msg)
		elif fileName and not(fileName[-4:] ==  ".jpg"):
			warringWindow = QMessageBox.information(self, 'warnning', 'jpg파일을 불러와야 합니다.',QMessageBox.Yes)
			
			if warringWindow == QMessageBox.Yes:
				pass
		elif fileName == None:
			pass

	def saveImage(self):
		if self.select_file != 'img/empty.png':
			self.original_dst = cv2.cvtColor(self.original_dst, cv2.COLOR_RGB2BGR)
			
			status = self.showDialog('지정할 파일명을 입력하세요.')	
			if status:
				name = self.input_text		

				if not(os.path.isdir('./result')):
					os.makedirs('./result')

				cv2.imwrite(f'./result/{name}.jpg', self.original_dst)
				self.console.append(f'이미지 프로세싱 된 {name}.jpg 저장되었습니다.')
		else:
			pass


	def convertToPixmap(self, dst):
		
		dst = qimage2ndarray.array2qimage(dst, normalize=False)
		dst = QPixmap.fromImage(dst)

		self.qPixmapVar2 = dst
		self.qPixmapVar2 = self.qPixmapVar2.scaledToHeight(300)
		self.display2.setPixmap(self.qPixmapVar2)	
	
	def showDialog(self, msg):
		text, ok = QInputDialog.getText(self, 'Input Dialog', msg)

		if ok:
			self.input_text = text

		return ok	

	def resizeFunc(self):
		if self.select_file != 'img/empty.png':
			status = self.showDialog('변경할 가로 크기를 입력하세요.')

			if status:
				W = self.input_text
				W = int(W)

		
				status = self.showDialog('변경할 세로 크기를 입력하세요.')

				if status:
					H = self.input_text
					H = int(H)

					self.original_dst, _, _ = resize(self.select_file, W, H, 0)
					self.original_dst = cv2.cvtColor(self.original_dst, cv2.COLOR_BGR2RGB)
					self.convertToPixmap(self.original_dst)
					
					self.console.append(f'사진의 크기가 {W}x{H}로 변경되었습니다.')
		else:
			pass

	def grayScaleFunc(self):
		if self.select_file != 'img/empty.png':
			self.original_dst = gray_scale(self.select_file, 0)
			self.convertToPixmap(self.original_dst)
			self.console.append('Grayscale 적용 완료')
		else:
			pass

	def	lrReverseFunc(self):
		if self.select_file != 'img/empty.png':
			self.original_dst = LR_reverse(self.select_file, 0)
			self.convertToPixmap(self.original_dst)	
			self.console.append('좌우반전 적용 완료')
		else:
			pass
		
	def adaptiveThresholdFunc(self):
		if self.select_file != 'img/empty.png':
			self.original_dst = adaptive_Threshold(self.select_file, 0)
			self.convertToPixmap(self.original_dst)	
			self.console.append('Adaptive threshold 적용 완료')
		else:
			pass
	
	def cannyFunc(self):
		if self.select_file != 'img/empty.png':
			status = self.showDialog('Low_Threshold 값을 입력해 주세요(0~255)')
			if status:
				low_threshold = self.input_text
				low_threshold = int(low_threshold)
				
				if 0 <= low_threshold <= 255:

					status = self.showDialog('High_Threshold 값을 입력해 주세요(0~255)')

					if status:
						high_threshold = self.input_text
						high_threshold = int(high_threshold)

						if 0 <= high_threshold <= 255:

							if low_threshold >= high_threshold:
								warringWindow = QMessageBox.information(
									self, 'warring', 'Low Threshold값이 High_Threshold값 보다 작아야 합니다.',
									QMessageBox.Yes)

								if warringWindow == QMessageBox.Yes:
									pass

							else:
								self.original_dst = canny_edge2(self.select_file, low_threshold, high_threshold)
								self.convertToPixmap(self.original_dst)
								self.console.append('Canny 적용 완료')
		else:
			pass

	def dilationClosingFunc(self):
		if self.select_file != 'img/empty.png':
			self.original_dst = dilation_closing(self.select_file, 0)	
			self.convertToPixmap(self.original_dst)
			self.console.append('Dilation Closing 적용 완료')
		else:
			pass
	
	def ClaheFunc(self):
		if self.select_file != 'img/empty.png':
			self.original_dst = CLAHE(self.select_file, 0)
			self.convertToPixmap(self.original_dst)
			self.console.append('CLAHE 적용 완료')
		else:
			pass

	def medianBlurringFunc(self):
		if self.select_file != 'img/empty.png':
			self.original_dst = median_blurring(self.select_file, 0)
			self.convertToPixmap(self.original_dst)
			self.console.append('Median blurring 적용 완료')
		else:
			pass
	
	def gaussianBlurringFunc(self):
		if self.select_file != 'img/empty.png':
			self.original_dst = gaussian_blurring(self.select_file, 0)
			self.convertToPixmap(self.original_dst)
			self.console.append('Gaussian blurring 적용 완료')
		else:
			pass

	def averagingBlurringFunc(self):
		if self.select_file != 'img/empty.png':
			self.original_dst = averaging_blurring(self.select_file, 0)
			self.convertToPixmap(self.original_dst)
			self.console.append('Averaging blurring 적용 완료')
		else:
			pass

	def bitwiseXorFunc(self):
		if self.select_file != 'img/empty.png':
			self.original_dst = bitwise_Xor(self.select_file, 0)
			self.convertToPixmap(self.original_dst)
			self.console.append('Bitwise XOR 적용 완료')
		else:
			pass

	def sharpenFunc(self):
		if self.select_file != 'img/empty.png':
			self.original_dst = sharpen(self.select_file, 0)
			self.convertToPixmap(self.original_dst)
			self.console.append('Sharpen 적용 완료')
		else:
			pass

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()


"""
	반영할 사항들
	3.중복처리
"""

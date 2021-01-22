import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from processing import *
import qimage2ndarray
import cv2
form_class = uic.loadUiType("img_processiong.ui")[0]



class WindowClass(QMainWindow, form_class):

	def __init__(self):
	
		super().__init__()
		self.setupUi(self)
		self.setFixedSize(850, 650)
		
		# 객체 변수 초기화
		self.select_file = None # 불러들인 파일의 절대경로 저장
		self.input_text = None # Input 다이얼로그에 입력한 문자열을 저장
		self.readImg = None # 읽어들인 ndarray를 저장
		self.isGrayScale = 0
		self.isRGB = 0

		self.setupDisplay1()
		self.setupDisplay2()

		self.connectClickBtn()











	# 첫번째 출력화면 관련
	def setupDisplay1(self):

		self.qPixmapVar1 = QPixmap()
		self.select_file = 'img/empty.png'
		self.qPixmapVar1.load(self.select_file)
		self.qPixmapVar1 = self.qPixmapVar1.scaledToHeight(300)
		self.display1.setPixmap(self.qPixmapVar1)



	# 두번째 출력화면 관련
	def setupDisplay2(self):

		self.qPixmapVar2 = QPixmap()
		self.qPixmapVar2.load('img/empty.png')
		self.qPixmapVar2 = self.qPixmapVar2.scaledToHeight(300)
		self.display2.setPixmap(self.qPixmapVar2)



	# 버튼기능 연결
	def connectClickBtn(self):

		# 이미지 프로세싱 기능
		self.resize_button.clicked.connect(self.resizeFunc_TEST)
		self.gray_scale_button.clicked.connect(self.grayScaleFunc_TEST)
		self.LR_reverse_button.clicked.connect(self.lrReverseFunc_TEST)
		self.adaptive_Threshold_button.clicked.connect(self.adaptiveThresholdFunc_TEST)
		self.canny_button.clicked.connect(self.cannyFunc_TEST)
		self.dilation_closing_button.clicked.connect(self.dilationClosingFunc_TEST)
		self.CLAHE_button.clicked.connect(self.ClaheFunc_TEST)
		self.median_blurring_button.clicked.connect(self.medianBlurringFunc_TEST)
		self.gaussian_blurring_button.clicked.connect(self.gaussianBlurringFunc_TEST)
		self.averaging_blurring_button.clicked.connect(self.averagingBlurringFunc_TEST)
		self.bitwise_xor_button.clicked.connect(self.bitwiseXorFunc_TEST)
		self.sharpen_button.clicked.connect(self.sharpenFunc_TEST)
		
		# 파일 관리
		self.open_button.clicked.connect(self.imageLoad)
		self.save_button.clicked.connect(self.saveImage)


	
	# 영상채널 수 확인
	def checkChannel(self, msg='None'):

		try:
			print(f'{msg}: {self.readImg.shape[2]}채널의 영상입니다.\n')
			flag = 1
		except IndexError:
			print(f'{msg}: 1채널의 영상입니다. \n')
			flag = 0
	
		return flag		



	# 파일 불러오기
	def imageLoad(self): 

		fileName, _ = QFileDialog.getOpenFileName(self, '불러올 이미지를 선택하세요','*.jpg')
		if fileName and (fileName[-4:] ==  ".jpg"):
			self.qPixmapVar2.load('img/empty.png')
			self.qPixmapVar2 = self.qPixmapVar2.scaledToHeight(300)
			self.display2.setPixmap(self.qPixmapVar2)

			
			self.select_file = fileName
			self.readImg = cv2.imread(self.select_file)
			
			# 채널 확인 함수 추가
			self.checkChannel()
			
			self.isRGB = 0
			self.isGrayScale = 0
			print(self.select_file)
			self.qPixmapVar1.load(self.select_file)
			self.qPixmapVar1 = self.qPixmapVar1.scaledToHeight(300)
			self.display1.setPixmap(self.qPixmapVar1)

			msg = os.path.basename(fileName) + ' 불러오기 완료'
			self.console.append(msg)
		elif fileName and not(fileName[-4:] == '.jpg'):
			warringWindow = QMessageBox.information(self, 'warnning', 'jpg파일을 불러와야 합니다.',QMessageBox.Yes)
			
			if warringWindow == QMessageBox.Yes:
				pass

		elif fileName == None:
			pass



	# 이미지 저장 
	def saveImage(self):
		if self.select_file != 'img/empty.png':
			self.readImg = cv2.cvtColor(self.readImg, cv2.COLOR_RGB2BGR)
			
			status = self.showDialog('지정할 파일명을 입력하세요.')	
			if status:
				name = self.input_text		

				if not(os.path.isdir('./result')):
					os.makedirs('./result')

				cv2.imwrite(f'./result/{name}.jpg', self.readImg)
				self.console.append(f'이미지 프로세싱 된 {name}.jpg 저장되었습니다.')
		else:
			pass



	# 넘파이 배열 -> 픽스맵 객체
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



	# 이미지 사이즈 변경(Test)
	def resizeFunc_TEST(self):

			if self.select_file != 'img/empty.png':
				status = self.showDialog('변경할 가로 크기를 입력하세요.')

				if status and self.input_text != '' and self.input_text.isnumeric():
					W = self.input_text
					W = int(W)

				elif status and self.input_text != '' and not(self.input_text.isnumeric()):		
					warringWindow = QMessageBox.information(self, 'warring', '숫자를 입력해야 합니다.', QMessageBox.Yes)

					if warringWindow == QMessageBox.Yes:
						return
				
				else:
					return


				status = self.showDialog('변경할 세로 크기를 입력하세요.')

				if status and self.input_text != '' and self.input_text.isnumeric():
					H = self.input_text
					H = int(H)

				elif status and self.input_text != '' and not(self.input_text.isnumeric()):		
					warringWindow = QMessageBox.information(self, 'warring', '숫자를 입력해야 합니다.', QMessageBox.Yes)

					if warringWindow == QMessageBox.Yes:
						return
				
				else:
					return

				self.checkChannel('전')
				self.readImg, self.isRGB = resize(self.readImg, W, H, 0, self.isRGB)
				self.checkChannel('후')
				#self.readImg = cv2.cvtColor(self.readImg, cv2.COLOR_BGR2RGB)
				self.convertToPixmap(self.readImg)
				
				self.console.append(f'사진의 크기가 {W}x{H}로 변경되었습니다.')

			else:
				pass



	# GarayScale 변환(Test)
	def grayScaleFunc_TEST(self): # 2번 적용 불가 

			if self.select_file != 'img/empty.png':
				if not(self.isGrayScale == 1):
					self.checkChannel('전')
					self.readImg = gray_scale(self.readImg, 0)
					self.checkChannel('후')

					self.isGrayScale = 1
					self.convertToPixmap(self.readImg)
					self.console.append('Grayscale 적용 완료')
			else:
				pass
	


	# 좌우반전(Test)
	def	lrReverseFunc_TEST(self): # 2번 적용 허용

			if self.select_file != 'img/empty.png':
				self.checkChannel('전')
				self.readImg, self.isRGB = LR_reverse(self.readImg, 0, self.isRGB)
				self.checkChannel('후')
				self.convertToPixmap(self.readImg)	
				self.console.append('좌우반전 적용 완료')
			else:
				pass	



	# Adaptive Threshold(Test)
	def adaptiveThresholdFunc_TEST(self):
		if self.select_file != 'img/empty.png':
			self.checkChannel('전')
			self.readImg, self.isGrayScale = adaptive_Threshold(self.readImg, 0, self.isGrayScale)
			self.checkChannel('후')
			
			self.convertToPixmap(self.readImg)	
			self.console.append('Adaptive threshold 적용 완료')
		else:
			pass
	


    # canny(Test)
	def cannyFunc_TEST(self):

		if self.select_file != 'img/empty.png':
			
			# 첫번째 입력
			status = self.showDialog('Low_Threshold 값을 입력해 주세요(0~255)')
			low_threshold = self.input_text

			# 정상적으로 입력한 경우
			if status and self.input_text != '' and self.input_text.isnumeric():
				low_threshold = int(low_threshold)
			
			# 숫자를 입력하지 않은 경우
			elif status and self.input_text != '' and not(self.input_text.isnumeric()):		
				warringWindow = QMessageBox.information(self, 'warring', '숫자를 입력해야 합니다.', QMessageBox.Yes)

				if warringWindow == QMessageBox.Yes:
					return

			# 공백의 경우	
			else:
				return


			if 0 <= low_threshold <= 255:

				# 두번째 입력
				status = self.showDialog('High_Threshold 값을 입력해 주세요(0~255)')

				if status and self.input_text != '' and self.input_text.isnumeric(): 
					high_threshold = self.input_text
					high_threshold = int(high_threshold)

				elif status and self.input_text != '' and not(self.input_text.isnumeric()):		
					warringWindow = QMessageBox.information(self, 'warring', '숫자를 입력해야 합니다.', QMessageBox.Yes)

					if warringWindow == QMessageBox.Yes:
						return

				else:
					return

				if 0 <= high_threshold <= 255:

					if low_threshold >= high_threshold:
						warringWindow = QMessageBox.information(self, 'warring', 'Low Threshold값이 High_Threshold값 보다 작아야 합니다.', QMessageBox.Yes)

						if warringWindow == QMessageBox.Yes:
							pass

					else:
						self.checkChannel('전')
						self.readImg, self.isGrayScale = canny_edge2(self.readImg, low_threshold, high_threshold, self.isGrayScale)
						self.checkChannel('후')
						self.convertToPixmap(self.readImg)
						self.console.append('Canny 적용 완료')
		else:
			pass



    # Dilation and Closing(Test)
	def dilationClosingFunc_TEST(self):

			if self.select_file != 'img/empty.png':
				self.checkChannel('전')
				self.readImg, self.isRGB= dilation_closing(self.readImg, 0, self.isRGB)	# self.isRGB를 전달해야 하는게 아니고 전달 받아 와야 함
				self.checkChannel('후')
				self.convertToPixmap(self.readImg)
				self.console.append('Dilation Closing 적용 완료')
			else:
				pass



    # CLAHE(Test)
	def ClaheFunc_TEST(self): # 혹시 readImg의 데이터를 그대로 pixmap객체로 변환해서 그런게 아닐까?
		# 이미 1채널인 경우에는 실행이 안되도록 하면 문제가 없겠다@@@@@    grayscale 변환 후에도 눌렀을 때 문제 없이 실행되야 함
		if self.select_file != 'img/empty.png':
			self.checkChannel('전')
			
			self.readImg, isGrayScale = CLAHE(self.readImg, 0, self.isGrayScale)
			self.checkChannel('후')
			self.convertToPixmap(self.readImg)
			self.console.append('CLAHE 적용 완료')
		else:
			pass



	# Median Blurring(Test)
	def medianBlurringFunc_TEST(self):

		if self.select_file != 'img/empty.png':
			self.checkChannel('전')
			self.readImg, self.isRGB = median_blurring(self.readImg, 0, self.isRGB)
			self.checkChannel('후')
			self.convertToPixmap(self.readImg)
			self.console.append('Median blurring 적용 완료')
		else:
			pass
	


    # Gaussian Blurring(Test)
	def gaussianBlurringFunc_TEST(self):

		if self.select_file != 'img/empty.png':
			self.checkChannel('전')
			self.readImg, self.isRGB = gaussian_blurring(self.readImg, 0, self.isRGB)
			self.checkChannel('후')
			self.convertToPixmap(self.readImg)
			self.console.append('Gaussian blurring 적용 완료')
		else:
			pass



    # Averaging Blurring(Test)
	def averagingBlurringFunc_TEST(self):

		if self.select_file != 'img/empty.png':
			self.checkChannel('전')
			self.readImg, self.isRGB= averaging_blurring(self.readImg, 0, self.isRGB)
			self.checkChannel('후')
			self.convertToPixmap(self.readImg)
			self.console.append('Averaging blurring 적용 완료')
		else:
			pass

	
	
	# bitwise XOR(Test)
	def bitwiseXorFunc_TEST(self):

		if self.select_file != 'img/empty.png':
			self.checkChannel('전')
			self.readImg, self.isRGB = bitwise_Xor(self.readImg, 0, self.isRGB)
			self.checkChannel('후')
			self.convertToPixmap(self.readImg)
			self.console.append('Bitwise XOR 적용 완료')
		else:
			pass



	# Sharpen
	def sharpenFunc_TEST(self):

		if self.select_file != 'img/empty.png':
			self.checkChannel('전')
			self.readImg, self.isRGB = sharpen(self.readImg, 0, self.isRGB)
			self.checkChannel('후')
			self.convertToPixmap(self.readImg)
			self.console.append('Sharpen 적용 완료')
		else:
			pass








if __name__ == "__main__":

	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	sys.exit(app.exec_())
	


"""
	반영할 사항들
	3.중복처리

	resize - O
	grayscale - O
	LR_reverse - O
	adative_Threshold - X
	canny - O
	bitwise XOR - X
	3 blur - O

	분석결과
	1.그레이스케일 적용하고 어댑티브 스래숄드  또는 비트와이즈 둘 중에 하나만 적용 할 경우에는 문제 없지만 두 가지 다 적용하려고 하니 오류가 발생
	2.좌우 반전 이나 다른 이미지 프로세싱 2번 적용시 색이 이상하게 변하는 증상 발생
	3.1번만 적용 되도록 그레이 스케일  처럼 만들기
"""

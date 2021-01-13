import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from processing import *

form_class = uic.loadUiType("img_processiong.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
#		self.setFixedSize(800, 800)
		
		self.initImage()
		
#		self.qPixmapVar = QPixmap()
#		self.qPixmapVar.load('img/empty.png')
#		self.display.setPixmap(self.qPixmapVar)

	#	self.resize_button.clicked.connect(self.resizeFunc)
		self.open_button.clicked.connect(self.imageLoad)
	
	def initImage(self):
		self.sid = QImage('img/empty.png').scaled(250, 260)

	def imageLoad(self):
		fileName, _ = QFileDialog.getOpenFileName(self, '불러올 이미지를 선택하세요','*.jpg')

		if fileName:
			print(fileName)
			self.sid = QImage(fileName).scaled(250,250)

		msg = os.path.basename(fileName) + ' 불러오기 완료'
		#self.select_file = frame[0]
		self.console.append(msg)


	def drawImages(self, painter):
		painter.drawImage(5, 15, self.sid)

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		self.drawImages(painter)
		painter.end()

	def resizeFunc(self):
		
		resize(self.select_file, 0)
		self.console.append(f'크기가 변경되었다.')

		
	
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()

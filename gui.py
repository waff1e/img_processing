import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from processing import *

form_class = uic.loadUiType("img_processiong.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.resize_button.clicked.connect(self.loadImageFromFile)
		

	def loadImageFromFile(self):
		self.qPixmapVar = QPixmap()
		self.qPixmapVar.load("img/sample001.jpg")
		
		self.display.setPixmap(self.qPixmapVar)
	
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()

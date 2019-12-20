import sys
from PyQt5.QtWidgets import QApplication, QWidget

def app():
	my_app = QApplication(sys.argv)
	w = QWidget()
	w.setWindowTitle("Testing this mug")
	w.show()
	sys.exit(my_app.exec_())

def main():
	app()

if __name__ == '__main__':
	main()
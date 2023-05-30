import sys
from PySide import Qtgui,QtCore

app=QtGui.QApplication(sys.argv)
mainwindow=QtGui.QWidget()
mainwindow.setWindowTitle("Pyside icon")
mainwindow.setWindowIcon(QtGui.QIcon('cat.png'))
mainwindow.show()
app.exec_()
from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        #laad de interface file
        uic.loadUi('test.ui', self)
        
        #twee knoppen
        self.child1 = self.findChild(QtWidgets.QPushButton, 'Tim')
        self.child1.clicked.connect(self.set_page_window) 
        self.page1 = self.findChild(QtWidgets.QPushButton, 'page1')
        self.page1.clicked.connect(self.set_pageview_window)
        
        #menubar
        self.menubar = self.findChild(QtWidgets.QMenuBar, 'menubar')
        self.actionKinderen.triggered.connect(self.set_children_window)
        self.actionBoeken.triggered.connect(self.set_page_window)
        
        #de stacked widget waarin de verschillende menus staan
        self.stackedwidget = self.findChild(QtWidgets.QStackedWidget, 'stackedWidget')
        
        self.show()

    def set_children_window(self):
        self.stackedWidget.setCurrentIndex(0)
        print('changed window to children')
    def set_page_window(self):
        self.stackedWidget.setCurrentIndex(1)
        print('changed window to pages')
    def set_pageview_window(self):
        self.stackedWidget.setCurrentIndex(2)
        print('changed window to page view')        

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

#sys.exit(app.exec_())
sys.exit()
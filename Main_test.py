from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        #global variables
        self.page_nr=1
        
        
        
        #laad de interface file
        uic.loadUi('test.ui', self)
        
        #beginview: kinderen
        self.child1 = self.findChild(QtWidgets.QPushButton, 'Tim')
        self.child1.clicked.connect(self.set_book_window) 
        self.child2 = self.findChild(QtWidgets.QPushButton, 'Lieke')
        self.child2.clicked.connect(self.set_book_window) 
        self.child3 = self.findChild(QtWidgets.QPushButton, 'kind3')
        self.child3.clicked.connect(self.set_book_window) 
        self.child4 = self.findChild(QtWidgets.QPushButton, 'kind4')
        self.child4.clicked.connect(self.set_book_window) 
        self.child5 = self.findChild(QtWidgets.QPushButton, 'kind5')
        self.child5.clicked.connect(self.set_book_window) 
        self.child6 = self.findChild(QtWidgets.QPushButton, 'kind6')
        self.child6.clicked.connect(self.set_book_window) 
        #view met de verschillende boeken
        self.book1 = self.findChild(QtWidgets.QPushButton, 'book1')
        self.book1.clicked.connect(self.set_page_window) 
        
        #view met alle paginas van een boek
        self.page1 = self.findChild(QtWidgets.QPushButton, 'page1')
        self.page1.clicked.connect(self.set_pageview_window)
        self.page2 = self.findChild(QtWidgets.QPushButton, 'page2')
        self.page2.clicked.connect(self.set_pageview_window)
        self.page3 = self.findChild(QtWidgets.QPushButton, 'page3')
        self.page3.clicked.connect(self.set_pageview_window)
        self.page4 = self.findChild(QtWidgets.QPushButton, 'page4')
        self.page4.clicked.connect(self.set_pageview_window)
        self.page5 = self.findChild(QtWidgets.QPushButton, 'page5')
        self.page5.clicked.connect(self.set_pageview_window)
        self.page6 = self.findChild(QtWidgets.QPushButton, 'page6')
        self.page6.clicked.connect(self.set_pageview_window)
        self.page7 = self.findChild(QtWidgets.QPushButton, 'page7')
        self.page7.clicked.connect(self.set_pageview_window)
        self.page8 = self.findChild(QtWidgets.QPushButton, 'page8')
        self.page8.clicked.connect(self.set_pageview_window)
        self.pagex = self.findChild(QtWidgets.QPushButton, 'pagex')
        self.pagex.clicked.connect(self.set_pageview_window)
        
        #view van één pagina
        self.screen = self.findChild(QtWidgets.QLabel, 'screen' )
        pixmap = QPixmap('video.PNG')
        self.screen.setPixmap(pixmap)
        self.pagenrlabel = self.findChild(QtWidgets.QLabel, 'pagenr' )
        
        self.nextpagebutton = self.findChild(QtWidgets.QPushButton, 'next_page')
        self.nextpagebutton.clicked.connect(self.turn_page_next)
        self.previouspagebutton = self.findChild(QtWidgets.QPushButton, 'previous_page')
        self.previouspagebutton.clicked.connect(self.turn_page_previous)
        #instellingen
        
        
        
        #menubar
        self.menubar = self.findChild(QtWidgets.QMenuBar, 'menubar')
        self.actionKinderen.triggered.connect(self.set_children_window)
        self.actionBoeken.triggered.connect(self.set_book_window)
        self.actionPaginas.triggered.connect(self.set_page_window)
        self.actionInstellingen.triggered.connect(self.set_instellingen_window)
        
        #de stacked widget waarin de verschillende windows staan
        self.stackedwidget = self.findChild(QtWidgets.QStackedWidget, 'stackedWidget')
        self.stackedWidget.setCurrentIndex(0)
        self.show()
        
        
        #voor plaatjes
        self.screen = self.findChild(QtWidgets.QLabel, 'screen' )
        pixmap = QPixmap('video.PNG')
        self.screen.setPixmap(pixmap)


    #verander de window
    def set_children_window(self):
        self.stackedWidget.setCurrentIndex(0)
        print('changed window to children')
    def set_instellingen_window(self):
        self.stackedwidget.setCurrentIndex(1)
    def set_page_window(self):
        self.stackedWidget.setCurrentIndex(2)
        print('changed window to pages')
    def set_pageview_window(self):
        self.stackedWidget.setCurrentIndex(3)
        print('changed window to page view')        
    def set_book_window(self):
        self.stackedWidget.setCurrentIndex(4)
        print('changed window to page view')  
    def turn_page_next(self):
        self.page_nr+=1
        self.pagenrlabel.setText(str(self.page_nr))
        print('page set to: ' + str(self.page_nr))
    def turn_page_previous(self):
        if(self.page_nr>1):
            self.page_nr-=1
        self.pagenrlabel.setText(str(self.page_nr))
        print('page set to: ' + str(self.page_nr))
    


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

#sys.exit(app.exec_())
sys.exit()
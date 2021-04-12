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
        self.child = self.findChild(QtWidgets.QPushButton, 'Tim_old')
        self.child.clicked.connect(self.set_book_window)

        #kinderen connecten aan volgende pagina
        self.child1 = self.findChild(QtWidgets.QPushButton, 'kind1')
        self.child1.clicked.connect(self.set_book_window)
        self.child2 = self.findChild(QtWidgets.QPushButton, 'kind2')
        self.child2.clicked.connect(self.set_book_window) 
        self.child3 = self.findChild(QtWidgets.QPushButton, 'kind3')
        self.child3.clicked.connect(self.set_book_window) 
        self.child4 = self.findChild(QtWidgets.QPushButton, 'kind4')
        self.child4.clicked.connect(self.set_book_window) 
        self.child5 = self.findChild(QtWidgets.QPushButton, 'kind5')
        self.child5.clicked.connect(self.set_book_window) 
        self.child6 = self.findChild(QtWidgets.QPushButton, 'kind6')
        self.child6.clicked.connect(self.set_book_window) 
        self.child7 = self.findChild(QtWidgets.QPushButton, 'kind7')
        self.child7.clicked.connect(self.set_book_window)

        #view met de verschillende boeken
        self.book1 = self.findChild(QtWidgets.QPushButton, 'book1')
        self.book1.clicked.connect(self.set_page_window) 
        
        #view met alle paginas van een boek
        self.page1 = self.findChild(QtWidgets.QPushButton, 'page1')
        #weer iets als if clicked:
        # video = video 1 (in set_pageview_window) die window is verder hetzelfde
        # caption = ... (bij het label caption)
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
        self.page9 = self.findChild(QtWidgets.QPushButton, 'page9')
        self.page9.clicked.connect(self.set_pageview_window)
        self.page10 = self.findChild(QtWidgets.QPushButton, 'page10')
        self.page10.clicked.connect(self.set_pageview_window)
        self.page11 = self.findChild(QtWidgets.QPushButton, 'page11')
        self.page11.clicked.connect(self.set_pageview_window)
        #self.pagex = self.findChild(QtWidgets.QPushButton, 'pagex')
        #self.pagex.clicked.connect(self.set_pageview_window)
        
        #view van één pagina
        self.boek = self.findChild(QtWidgets.QLabel, 'boek' )
        pixmap = QPixmap('boek.PNG')
        self.boek.setPixmap(pixmap)
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
        #self.screen = self.findChild(QtWidgets.QLabel, 'screen' )
        #pixmap = QPixmap('video.PNG')
        #self.screen.setPixmap(pixmap)

        #lijst met images
        #lijst met widths
        #lijst met hights 
        #lijst met channels, whatever dat is 
        #nieuwe lijst met pixmaps die nog op de goeie plek moeten komen en nu leeg is

        #if Qlabels name is iets met logo (dus logo of logo_2 of logo_3) : dan deze pixmap 
        self.logo = self.findChild(QtWidgets.QLabel, 'logo')
        pixmap2 = QPixmap('logo.PNG')
        self.logo.setPixmap(pixmap2)

        self.logo_2 = self.findChild(QtWidgets.QLabel, 'logo_2')
        self.logo_2.setPixmap(pixmap2)

        self.background = self.findChild(QtWidgets.QLabel, 'background')
        pixmap3 = QPixmap('background.PNG')
        self.background.setPixmap(pixmap3)

        #plaatjes kinderen
        self.child1_img = self.findChild(QtWidgets.QLabel, 'tim_img')
        pixmap4 = QPixmap('tim.PNG')
        self.child1_img.setPixmap(pixmap4)

        self.child2_img = self.findChild(QtWidgets.QLabel, 'lieke_img')
        pixmap5 = QPixmap('lieke.PNG')
        self.child2_img.setPixmap(pixmap5)

        #dit moet kind_pagina overzicht worden als label, dat ik de pixmap kan pakken van t goeie kind
        self.child2_img_2 = self.findChild(QtWidgets.QLabel, 'lieke_img_2')
        self.child2_img_2.setPixmap(pixmap5)

        self.child3_img = self.findChild(QtWidgets.QLabel, 'jorik_img')
        pixmap6 = QPixmap('jorik.PNG')
        self.child3_img.setPixmap(pixmap6)

        self.child4_img = self.findChild(QtWidgets.QLabel, 'noraja_img')
        pixmap7 = QPixmap('noraja.PNG')
        self.child4_img.setPixmap(pixmap7)

        self.child5_img = self.findChild(QtWidgets.QLabel, 'annsophie_img')
        pixmap8 = QPixmap('annsophie.PNG')
        self.child5_img.setPixmap(pixmap8)

        self.child6_img = self.findChild(QtWidgets.QLabel, 'annemiek_img')
        pixmap9 = QPixmap('annemiek.PNG')
        self.child6_img.setPixmap(pixmap9)

        self.child7_img = self.findChild(QtWidgets.QLabel, 'arjan_img')
        pixmap10 = QPixmap('arjan.PNG')
        self.child7_img.setPixmap(pixmap10)

        #plaatjes buttons
        self.add = self.findChild(QtWidgets.QLabel, 'add')
        pixmap11 = QPixmap('add.PNG')
        self.add.setPixmap(pixmap11)

        #plaatjes paginaoverzicht
        self.page1_img = self.findChild(QtWidgets.QLabel, 'page1_img')
        pixmap12 = QPixmap('Image_1.PNG')
        self.page1_img.setPixmap(pixmap12)

        self.page2_img = self.findChild(QtWidgets.QLabel, 'page2_img')
        pixmap13 = QPixmap('Image_7.PNG')
        self.page2_img.setPixmap(pixmap13)

        self.page3_img = self.findChild(QtWidgets.QLabel, 'page3_img')
        pixmap14 = QPixmap('Image_8.PNG')
        self.page3_img.setPixmap(pixmap14)

        self.page4_img = self.findChild(QtWidgets.QLabel, 'page4_img')
        pixmap15 = QPixmap('Image_9.PNG')
        self.page4_img.setPixmap(pixmap15)

        self.page5_img = self.findChild(QtWidgets.QLabel, 'page5_img')
        pixmap16 = QPixmap('Image_10.PNG')
        self.page5_img.setPixmap(pixmap16)

        self.page6_img = self.findChild(QtWidgets.QLabel, 'page6_img')
        pixmap17 = QPixmap('Image_11.PNG')
        self.page6_img.setPixmap(pixmap17)

        self.page7_img = self.findChild(QtWidgets.QLabel, 'page7_img')
        pixmap18 = QPixmap('Image_12.PNG')
        self.page7_img.setPixmap(pixmap18)

        self.page8_img = self.findChild(QtWidgets.QLabel, 'page8_img')
        pixmap19 = QPixmap('Image_13.PNG')
        self.page8_img.setPixmap(pixmap19)

        self.page9_img = self.findChild(QtWidgets.QLabel, 'page9_img')
        pixmap20 = QPixmap('Image_14.PNG')
        self.page9_img.setPixmap(pixmap20)

        self.page10_img = self.findChild(QtWidgets.QLabel, 'page10_img')
        pixmap21 = QPixmap('Image_15.PNG')
        self.page10_img.setPixmap(pixmap21)

        self.page11_img = self.findChild(QtWidgets.QLabel, 'page11_img')
        pixmap22 = QPixmap('Image_16.PNG')
        self.page11_img.setPixmap(pixmap22)

    class Child: 
        def __init__(self, name, img, button_size, fond_size, low_stim, pages_read):
            self.name = name
            self.img = img
            self.button_size = button_size
            self.fond_size = fond_size
            self.low_stim = low_stim 
            self.pages_read = pages_read
        
        def show_kid(self):
            pixmap = QPixmap(self.img)
            return pixmap
    







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
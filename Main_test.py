from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import cv2
import threading
from playsound import playsound

from PyQt5.QtWidgets import (
    QWidget, QApplication, QProgressBar, QMainWindow,
    QHBoxLayout, QPushButton
)

from PyQt5.QtCore import (
    Qt, QObject, pyqtSignal, pyqtSlot, QRunnable, QThreadPool
)
import time
import sys
sys.path.insert(1, 'Detection')
from inference import *
[m,mf,c] = load_model()
#[m,mf,c] = ['dum', 'dummy','dumst']
#%%
def set_caption(self, pagenr):
    captions = ['Hallo ..., we lezen nu kijk eens wat een kleintje',
        'Milo en Lana lopen langs de wei. Kijk eens even, wie komen daar voorbij? \n Het kleine kalfje en moeder koe. Lopen samen naar de boerderij toe.',
        'Milo: Wat een schattig kalfje. Hoe vind jij het om naar de boerderij te gaan?',
        'Milo en Lana lopen langs de wei. Kijk eens even, wie komt daar voorbij? \n Daar loopt de haan, wat hoor ik nu? De haan roept heel hard: kukeleku!',
        'Milo: Wat vind jij het leukste dierengeluid?',
        'Milo en Lana lopen langs de wei. Kijk eens even, wie komen daar voorbij? \n De hond, die blaft hard voor zijn hok En ...miauw! De poes: die schrok!',
        'Milo: Oh! Ik schrok ook! Naar welk dier zou jij nu heen willen gaan?',
        'Milo en Lana lopen langs de wei. Kijk eens even, wie komen daar voorbij? \n Daar vliegt de vogel, in de lucht heel snel. En de boer op de grond, die zet hem wel!',
        'Milo: *Opmerking over vogels*  Welk dier vind jij het liefst? Laten we daar naartoe gaan!',
        'Milo en Lana lopen langs de wei. Kijk eens even, wie komen daar voorbij? \n Moeder varken en de kleine biggen. Gaan achter het hek in de modder liggen.',
        'Een lekker modderbadje daar heb ik ook wel zin in. Wat zou jij doen op de boerderij?',
        'Milo en Lana lopen langs de wei. Kijk eens even, wie komen daar voorbij? \n Een kuiken dat piept, hij zwemt in het water. En mama eend? Die komt wat later.',
        'Milo: Spitter spetter spater, ik hou van water. Hoe vind jij het om te zwemmen?',
        'Milo en Lana lopen langs de wei. Kijk eens even, wie komen daar voorbij? \n De geit, die heeft allemaal gras in zijn bek. En konijn in haar hol? Die vindt het maar gek!',
        'Milo: Konijntjes zijn super zacht! Heb jij al wel eens een dier geaaid? Hoe vond je dat?',
        'Milo en Lana lopen langs de wei. Kijk eens even, wie komen daar voorbij? \n De kip die zoekt in de tuin wat te eten. Maar het ei in haar nest is ze niet vergeten!',
        'Milo: Wat een goeie mama is die kip. Naar welk dier zullen we nu gaan?',
        'Milo en Lana lopen langs de wei. Kijk eens even, wie komen daar voorbij? \n Daar is het lammetje, met zijn kopje zo zacht. En daar mama schaap, die lief op hem wacht.',
        'Milo: Welke dieren vind jij zacht?',
        'Zie Milo en Lana eens vrolijk zwaaien! Ze mogen van de boer alle dieren aaien. \n Wat een fijne lente-dag was dat, Met al die grote en kleine dieren op pad!',
        'Milo: Wat een leuk verhaal was dat! Welk dier vond jij het leukst? '
        ]
    self.page_caption.setText(captions[pagenr-1])
    
    
def load_page(self, pagenr):
<<<<<<< HEAD
<<<<<<< HEAD
    print('begin loading page:' + str(pagenr))
    self.stackedWidget.setCurrentIndex(3)
    self.animationpath='Animations/pagina'+str(int(pagenr/2)+1)+'.mp4'
=======
    self.stackedWidget.setCurrentIndex(3)
    self.animationpath='Animations/pagina'+str(pagenr)+'.mp4'
>>>>>>> parent of 3457f29 (dingen)
=======
    self.stackedWidget.setCurrentIndex(3)
    self.animationpath='Animations/pagina'+str(pagenr)+'.mp4'
>>>>>>> parent of 3457f29 (dingen)
    self.thread.animationpath =self.animationpath
    set_caption(self, pagenr)
    self.thread.kill()
    time.sleep(0.1)
<<<<<<< HEAD
    if pagenr % 2 == 0 or self.page_nr == 1:
        self.thread.start()
    if np.isin(self.page_nr, [7,9,17]):
        self.capturebutton.show()
    else:
        self.capturebutton.hide()
=======
    self.thread.start()
<<<<<<< HEAD
>>>>>>> parent of 3457f29 (dingen)
=======
>>>>>>> parent of 3457f29 (dingen)

#%%
#Dit is het paralelle proces waarin de video wordt afgespeeld
class Thread(QThread):
    #signaalding om te sturen dat het scherm geupdate moet worden
    changePixmap = pyqtSignal(QImage)
    #blijft draaien zolang dit waar is
    running=True
    animationpath='\Animations\pagina1.mp4'
    def run(self):
        self.running =True       
        cap = cv2.VideoCapture(self.animationpath) 
        
        #loop oneindig 
        while self.running:
            #pak de volgende frame
            ret, frame = cap.read()
            
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(1200, 900, Qt.KeepAspectRatio) 
                #stuur update signaal
                self.changePixmap.emit(p)
                
                
            if self.running==False:
                break
            #zorg dat je niet te snel afspeelt
            time.sleep(0.02)
            if ret == False:
                print('video done')
                break
    #stop het proces zodat je pc niet vastloopt en je spyder honderduizend keer moet opstarten wat een teringzooi
    def kill(self):
        self.running = False
        print('received stop signal from window.(1)')

class Thread2(QThread):

    #signaalding om te sturen dat het scherm geupdate moet worden
    changecamPixmap = pyqtSignal(QImage)
    #signaalding om te sturen welke pagina er moet worden geladen
    changepage = pyqtSignal(int)
    #blijft draaien zolang dit waar is
    running=True
    sounddict = {"varken" : "Sounds\\varken.mp3",
                 "kuiken" : "Sounds\kuiken.mp3",
                 "koe" : "Sounds\koe.mp3",
                 "schaap" :"Sounds\schaap.mp3",
                 "hond":"Sounds\hond.mp3"}
    pagedict = {"varken" : 10,
                "kuiken" : 12,
                "koe" : 2,
                "schaap" : 18,
                "hond" : 6}
    def load_model_please(self,package):
        self.model = package[1]
        self.model_fn = package[2]
        self.category_index = package[3]
        
        
    def run(self):
        #0 voor webcam, anders link naar de file
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        start = time.time()
        detections=[]
        #loop oneindig 
        while self.running:
            #pak de volgende frame
            ret, frame = cap.read()
            if ret:
                nn_detection,box = milo_predict(frame, self.model, self.model_fn, self.category_index)
                y=int(frame.shape[0]*box[0])
                x=int(frame.shape[1]*box[1])
                w=int((box[2]-box[0])*frame.shape[0])
                h=int((box[3]-box[1])*frame.shape[1])
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),5)
                cv2.putText(frame,nn_detection,(x+w+10,y+h),0,1.5,(255,255,255), 3)
                
                detections.append(nn_detection)
                now= time.time()
                current_time=now-start
                if current_time > 10:
                    occurence_count = Counter(detections)
                    final_detection=occurence_count.most_common(1)[0][0]
                    print(final_detection)
                    playsound(self.sounddict[final_detection])
                    self.changepage.emit(self.pagedict[final_detection])
                    break
                
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(350, 350, Qt.KeepAspectRatio) 
                #stuur update signaal
                self.changecamPixmap.emit(p)                
            if self.running==False:
                break
            #zorg dat je niet te snel afspeelt
            #time.sleep(0.02)
            
    #stop het proces zodat je pc niet vastloopt en je spyder honderduizend keer moet opstarten wat een teringzooi
    def kill(self):
        self.running = False
        print('received stop signal from window.(2)')
        
class Thread3(QThread):    
    #blijft draaien zolang dit waar is
    running=True
    soundpath='Sounds\eend.mp3'
    def run(self):
        playsound(self.soundpath)
        print('quack')
        return
    #stop het proces zodat je pc niet vastloopt en je spyder honderdduizend keer moet opstarten wat een teringzooi
    def kill(self):
        self.running = False
        print('received stop signal from window.(3)')

class Ui(QtWidgets.QMainWindow):
    #update videoplayer frame
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.videoplayer.setPixmap(QPixmap.fromImage(image))
    @pyqtSlot(QImage)
    def setcamplayer(self, image):
        self.camplayer.setPixmap(QPixmap.fromImage(image))
    @pyqtSlot(int)
    def set_page_choice(self, pagechoice):
        load_page(self, pagechoice)


        
    #er is op kruisje gedrukt dus sluit alles correct af    
    def closeEvent(self, event):
        
        self.thread.kill()
        self.thread2.kill()
        self.thread3.kill()
        print("Closing")
        #self.destory()
        
    def __init__(self, app):
        super(Ui, self).__init__()
        #global variables
        self.page_nr=1
        self.page_order = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
        
        #laad de interface file
        uic.loadUi('test.ui', self)
        self.show()
        #laat eerst programma zien en laad dan pas het model
        
        #[m,c]=[0,1]
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
        
        #view met alle paginas van een boek + connect aan pageview
        self.page1 = self.findChild(QtWidgets.QPushButton, 'page1')
        #weer iets als if clicked:
        # video = video 1 (in set_pageview_window) die window is verder hetzelfde
        # caption = ... (bij het label caption)
        self.page1.clicked.connect(self.set_pageview_window1)
        self.page2 = self.findChild(QtWidgets.QPushButton, 'page2')
        self.page2.clicked.connect(self.set_pageview_window2)
        self.page3 = self.findChild(QtWidgets.QPushButton, 'page3')
        self.page3.clicked.connect(self.set_pageview_window3)
        self.page4 = self.findChild(QtWidgets.QPushButton, 'page4')
        self.page4.clicked.connect(self.set_pageview_window4)
        self.page5 = self.findChild(QtWidgets.QPushButton, 'page5')
        self.page5.clicked.connect(self.set_pageview_window5)
        self.page6 = self.findChild(QtWidgets.QPushButton, 'page6')
        self.page6.clicked.connect(self.set_pageview_window6)
        self.page7 = self.findChild(QtWidgets.QPushButton, 'page7')
        self.page7.clicked.connect(self.set_pageview_window7)
        self.page8 = self.findChild(QtWidgets.QPushButton, 'page8')
        self.page8.clicked.connect(self.set_pageview_window8)
        self.page9 = self.findChild(QtWidgets.QPushButton, 'page9')
        self.page9.clicked.connect(self.set_pageview_window9)
        self.page10 = self.findChild(QtWidgets.QPushButton, 'page10')
        self.page10.clicked.connect(self.set_pageview_window10)
        self.page11 = self.findChild(QtWidgets.QPushButton, 'page11')
        self.page11.clicked.connect(self.set_pageview_window11)
        #self.pagex = self.findChild(QtWidgets.QPushButton, 'pagex')
        #self.pagex.clicked.connect(self.set_pageview_window)
        
        #view van één pagina
        self.boek = self.findChild(QtWidgets.QLabel, 'boek')
        self.boek.setPixmap(QPixmap('images/boek.PNG'))
        self.pagenrlabel = self.findChild(QtWidgets.QLabel, 'pagenr' )
        self.page_caption = self.findChild(QtWidgets.QLabel, 'caption')
        
        self.nextpagebutton = self.findChild(QtWidgets.QPushButton, 'next_page')
        self.nextpagebutton_img = self.findChild(QtWidgets.QLabel, 'next_page_img')
        self.nextpagebutton_img.setPixmap(QPixmap('images/next.PNG'))
        self.nextpagebutton.clicked.connect(self.turn_page_next)

        self.previouspagebutton = self.findChild(QtWidgets.QPushButton, 'previous_page')
        self.previouspagebutton_img = self.findChild(QtWidgets.QLabel, 'previous_page_img')
        self.previouspagebutton_img.setPixmap(QPixmap('images/back.PNG'))
        self.previouspagebutton.clicked.connect(self.turn_page_previous)
        
        self.capturebutton = self.findChild(QtWidgets.QPushButton, 'capture')
        self.capturebutton.clicked.connect(self.capture_choice)
        
        #@guus kan jij zorgen dat deze code pas 'happened' als de animatie is afgelopen?
        self.replay = self.findChild(QtWidgets.QPushButton, 'opnieuw')
        self.replay_img = self.findChild(QtWidgets.QLabel, 'opnieuw_img')
        self.replay_img.setPixmap(QPixmap('images/repeat.PNG'))
        self.replay.clicked.connect(self.replay_animation)
        
        #Dit stukje gaat over de videoplayer, met self.thread.start() begint hij met het afspelen van de animatie
        self.videoplayer = self.findChild(QtWidgets.QLabel, 'videoplayer' )
        self.camplayer = self.findChild(QtWidgets.QLabel, 'camplayer' )
        self.thread = Thread(self)
        self.thread.changePixmap.connect(self.setImage)
        self.thread2 = Thread2(self)
        self.thread2.load_model_please([self, m,mf,c])
        self.thread2.changecamPixmap.connect(self.setcamplayer)
        self.thread2.changepage.connect(self.set_page_choice)
        self.thread3 = Thread3(self)
        
        #self.thread.start()

        
        
        
        #menubar
        self.menubar = self.findChild(QtWidgets.QMenuBar, 'menubar')
        self.actionKinderen.triggered.connect(self.set_children_window)
        self.actionBoeken.triggered.connect(self.set_book_window)
        self.actionPaginas.triggered.connect(self.set_page_window)
        self.actionInstellingen.triggered.connect(self.set_instellingen_window)
        
        #de stacked widget waarin de verschillende windows staan
        self.stackedwidget = self.findChild(QtWidgets.QStackedWidget, 'stackedWidget')
        self.stackedWidget.setCurrentIndex(0)
        
        
        
        
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
        pixmap2 = QPixmap('images/logo.PNG')
        self.logo.setPixmap(pixmap2)

        self.logo_2 = self.findChild(QtWidgets.QLabel, 'logo_2')
        self.logo_2.setPixmap(pixmap2)

        #centralwidget spul
        self.background = self.findChild(QtWidgets.QLabel, 'background')
        self.background.setPixmap(QPixmap('images/background.JPEG'))

        self.hamburger_img = self.findChild(QtWidgets.QLabel, 'hamburger_img')
        self.hamburger_img.setPixmap(QPixmap('images/menuknop.PNG'))
        self.hamburger_uit_img = self.findChild(QtWidgets.QLabel, 'hamburger_uit_img')
        self.hamburger_uit_img.setPixmap(QPixmap('images/empty.JPEG'))
        self.hamburger = self.findChild(QtWidgets.QPushButton, 'hamburger')
        self.hamburger.clicked.connect(self.foldout_menu)
        self.exit = self.findChild(QtWidgets.QPushButton, 'exit')
        self.exit.setEnabled(False)
        self.exit.clicked.connect(self.foldin_menu)
<<<<<<< HEAD
        
        #if self.hamburger.clicked == True: 
   
=======

        self.instellingen = self.findChild(QtWidgets.QPushButton, 'instellingen')
        self.instellingen.setEnabled(False)
        self.instellingen.clicked.connect(self.instellingen_menu) 

        self.instellingen_open = self.findChild(QtWidgets.QLabel, 'instellingen_open')
        self.instellingen_open.setPixmap(QPixmap('images/empty.JPEG'))

        self.naar_klas = self.findChild(QtWidgets.QPushButton, 'knop_klas')
        self.naar_klas.setEnabled(False)
        self.naar_klas.setText(' ')
        self.naar_klas.clicked.connect(self.set_children_window)

        self.naar_boeken = self.findChild(QtWidgets.QPushButton, 'knop_boeken')
        self.naar_boeken.setEnabled(False)
        self.naar_boeken.setText(' ')
        self.naar_boeken.clicked.connect(self.set_book_window)

        self.naar_paginas = self.findChild(QtWidgets.QPushButton, 'knop_paginas')
        self.naar_paginas.setEnabled(False)
        self.naar_paginas.setText(' ')
        self.naar_paginas.clicked.connect(self.set_page_window)

        #if self.hamburger.clicked == True: 
         #   print("hoi")
<<<<<<< HEAD
>>>>>>> parent of 3457f29 (dingen)
=======
>>>>>>> parent of 3457f29 (dingen)
            
            #self.hamburger_uit_img.setPixmap(QPixmap('images/empty.JPEG'))
        #if clicked self.hamburger_uit_img.setPixmap(QPixmap('images/allessamen.PNG'))


        #plaatjes kinderen
        self.child1_img = self.findChild(QtWidgets.QLabel, 'tim_img')
        pixmap4 = QPixmap('images/tim.PNG')
        self.child1_img.setPixmap(pixmap4)

        self.child2_img = self.findChild(QtWidgets.QLabel, 'lieke_img')
        pixmap5 = QPixmap('images/lieke.PNG')
        self.child2_img.setPixmap(pixmap5)

        #dit moet kind_pagina overzicht worden als label, dat ik de pixmap kan pakken van t goeie kind
        self.child2_img_2 = self.findChild(QtWidgets.QLabel, 'lieke_img_2')
        self.child2_img_2.setPixmap(pixmap5)

        self.child3_img = self.findChild(QtWidgets.QLabel, 'jorik_img')
        pixmap6 = QPixmap('images/jorik.PNG')
        self.child3_img.setPixmap(pixmap6)

        self.child4_img = self.findChild(QtWidgets.QLabel, 'noraja_img')
        pixmap7 = QPixmap('images/noraja.PNG')
        self.child4_img.setPixmap(pixmap7)

        self.child5_img = self.findChild(QtWidgets.QLabel, 'annsophie_img')
        pixmap8 = QPixmap('images/annsophie.PNG')
        self.child5_img.setPixmap(pixmap8)

        self.child6_img = self.findChild(QtWidgets.QLabel, 'annemiek_img')
        pixmap9 = QPixmap('images/annemiek.PNG')
        self.child6_img.setPixmap(pixmap9)

        self.child7_img = self.findChild(QtWidgets.QLabel, 'arjan_img')
        pixmap10 = QPixmap('images/arjan.PNG')
        self.child7_img.setPixmap(pixmap10)

        #plaatjes buttons
        self.add = self.findChild(QtWidgets.QLabel, 'add')
        pixmap11 = QPixmap('images/add.PNG')
        self.add.setPixmap(pixmap11)

        #plaatjes paginaoverzicht
        self.page1_img = self.findChild(QtWidgets.QLabel, 'page1_img')
        pixmap12 = QPixmap('images/Image_1.PNG')
        self.page1_img.setPixmap(pixmap12)

        self.page2_img = self.findChild(QtWidgets.QLabel, 'page2_img')
        pixmap13 = QPixmap('images/Image_7.PNG')
        self.page2_img.setPixmap(pixmap13)

        self.page3_img = self.findChild(QtWidgets.QLabel, 'page3_img')
        pixmap14 = QPixmap('images/Image_8.PNG')
        self.page3_img.setPixmap(pixmap14)

        self.page4_img = self.findChild(QtWidgets.QLabel, 'page4_img')
        pixmap15 = QPixmap('images/Image_9.PNG')
        self.page4_img.setPixmap(pixmap15)

        self.page5_img = self.findChild(QtWidgets.QLabel, 'page5_img')
        pixmap16 = QPixmap('images/Image_10.PNG')
        self.page5_img.setPixmap(pixmap16)

        self.page6_img = self.findChild(QtWidgets.QLabel, 'page6_img')
        pixmap17 = QPixmap('images/Image_11.PNG')
        self.page6_img.setPixmap(pixmap17)

        self.page7_img = self.findChild(QtWidgets.QLabel, 'page7_img')
        pixmap18 = QPixmap('images/Image_12.PNG')
        self.page7_img.setPixmap(pixmap18)

        self.page8_img = self.findChild(QtWidgets.QLabel, 'page8_img')
        pixmap19 = QPixmap('images/Image_13.PNG')
        self.page8_img.setPixmap(pixmap19)

        self.page9_img = self.findChild(QtWidgets.QLabel, 'page9_img')
        pixmap20 = QPixmap('images/Image_14.PNG')
        self.page9_img.setPixmap(pixmap20)

        self.page10_img = self.findChild(QtWidgets.QLabel, 'page10_img')
        pixmap21 = QPixmap('images/Image_15.PNG')
        self.page10_img.setPixmap(pixmap21)

        self.page11_img = self.findChild(QtWidgets.QLabel, 'page11_img')
        pixmap22 = QPixmap('images/Image_16.PNG')
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
    def set_pageview_window(self):
        print('changed window to page view')  
        load_page(self, self.page_nr)
    def set_pageview_window1(self):
        print('changed window to page view')  
        self.page_nr = 1
        load_page(self, 1)
    def set_pageview_window2(self):
        print('changed window to page view')  
        self.page_nr = 2
        load_page(self, 2)
    def set_pageview_window3(self):
        print('changed window to page view')  
<<<<<<< HEAD
        self.page_nr = 4
        load_page(self, 4)
    def set_pageview_window4(self):
        print('changed window to page view')  
        self.page_nr = 6
        load_page(self, 6)
    def set_pageview_window5(self):
        print('changed window to page view')  
        self.page_nr = 8
        load_page(self, 8)
    def set_pageview_window6(self):
        print('changed window to page view')  
        self.page_nr = 10
        load_page(self, 10)
    def set_pageview_window7(self):
        print('changed window to page view')  
        self.page_nr = 12
        load_page(self, 12)
    def set_pageview_window8(self):
        print('changed window to page view')  
        self.page_nr = 14
        load_page(self, 14)
    def set_pageview_window9(self):
        print('changed window to page view')  
        self.page_nr = 16
        load_page(self, 16)
    def set_pageview_window10(self):
        print('changed window to page view')  
        self.page_nr = 18
        load_page(self, 18)
    def set_pageview_window11(self):
        print('changed window to page view')  
        self.page_nr = 20
        load_page(self, 20)
    
=======
        self.page_nr = 3
        load_page(self, 3)
    def set_pageview_window4(self):
        print('changed window to page view')  
        self.page_nr = 4
        load_page(self, 4)
    def set_pageview_window5(self):
        print('changed window to page view')  
        self.page_nr = 5
        load_page(self, 5)
    def set_pageview_window6(self):
        print('changed window to page view')  
        self.page_nr = 6
        load_page(self, 6)
    def set_pageview_window7(self):
        print('changed window to page view')  
        self.page_nr = 7
        load_page(self, 7)
    def set_pageview_window8(self):
        print('changed window to page view')  
        self.page_nr = 8
        load_page(self, 8)
    def set_pageview_window9(self):
        print('changed window to page view')  
        self.page_nr = 9
        load_page(self, 9)
    def set_pageview_window10(self):
        print('changed window to page view')  
        self.page_nr = 10
        load_page(self, 10)
    def set_pageview_window11(self):
        print('changed window to page view')  
        self.page_nr = 11
        load_page(self, 11)
<<<<<<< HEAD
>>>>>>> parent of 3457f29 (dingen)
=======
>>>>>>> parent of 3457f29 (dingen)

        

    def set_children_window(self):
        self.stackedWidget.setCurrentIndex(0)
        print('changed window to children')
    def set_instellingen_window(self):
        self.stackedwidget.setCurrentIndex(1)
    def set_page_window(self):
        self.stackedWidget.setCurrentIndex(2)
<<<<<<< HEAD
=======
        self.foldin_menu()
<<<<<<< HEAD
>>>>>>> parent of 3457f29 (dingen)
=======
>>>>>>> parent of 3457f29 (dingen)
        print('changed window to pages')        
    def set_book_window(self):
        self.stackedWidget.setCurrentIndex(4)
        print('changed window to bookview')  
    def replay_animation(self):
        if self.thread.running == True:
            self.thread.kill()
            time.sleep(0.1)
        self.thread.start()
        #self.thread2.start()
        print('thread started')
    def turn_page_next(self):
        if(self.page_nr<21):
            self.page_nr+=1
        self.pagenrlabel.setText(str(self.page_nr))
        
        load_page(self, self.page_order[self.page_nr-1])
        print('page set to: ' + str(self.page_nr))
    def turn_page_previous(self):
        if(self.page_nr>1):
            if self.page_nr % 2 == 0 :
                self.page_nr-=2
                if self.page_nr==0:
                    self.page_nr =1
            else:
                self.page_nr-=1
        self.pagenrlabel.setText(str(self.page_nr))
        load_page(self, self.page_order[self.page_nr-1])
        print('page set to: ' + str(self.page_nr))
    def foldout_menu(self):
        print("menu expanded")
        self.thread3.start()
        self.hamburger_uit_img.setPixmap(QPixmap('images/allessamen.PNG'))
        self.hamburger_img.setPixmap(QPixmap('images/empty.JPEG'))
        self.hamburger.setEnabled(False)
        self.exit.setEnabled(True)
    def foldin_menu(self):
        print("menu ingeklapt")
        self.hamburger_uit_img.setPixmap(QPixmap('images/empty.JPEG'))
        self.hamburger_img.setPixmap(QPixmap('images/menuknop.PNG'))
        self.hamburger.setEnabled(True)
        self.exit.setEnabled(False)
<<<<<<< HEAD
    def capture_choice(self):
        print('capturing choice')
        self.thread2.start()
=======
        self.instellingen.setEnabled(False)
        self.naar_klas.setEnabled(False)
        self.naar_boeken.setEnabled(False)
        self.naar_paginas.setEnabled(False)
        #laat teksten knoppen verdwijnen
        self.naar_klas.setText(' ')
        self.naar_boeken.setText(' ')
        self.naar_paginas.setText(' ')

    def instellingen_menu(self):
        print("dit zijn de instellingen")
        #self.instellingen_open.show()
        self.instellingen_open.setPixmap(QPixmap('images/instelling_backblack.PNG'))
        self.foldin_menu()
        
>>>>>>> parent of 3457f29 (dingen)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(app)
    window.show()
    #ys.exit()
    sys.exit(app.exec_()) 
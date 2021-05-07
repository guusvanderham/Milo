from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QFont
import cv2
import threading
from playsound import playsound
import pickle

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
#[m,mf,c] = load_model()
[m,mf,c] = ['dum', 'dummy','dumst']
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
        'Milo: Wat een leuk verhaal was dat! Welk dier vond jij het leukst? ',
        'Hallo'
        ]
    self.page_caption.setText(captions[pagenr-1])
    self.page_caption.setAlignment(Qt.AlignCenter)
    self.page_caption.setFont(QFont('Segoe UI', self.huidig_kind.font_size))
    #self.label_1.setFont(QFont('Arial', 10))
    
    
def load_page(self, pagenr):
    if pagenr == 0:
        return
    print('begin loading page:' + str(pagenr))
    self.stackedWidget.setCurrentIndex(3)
    self.animationpath='Animations/pagina'+str(int(pagenr/2)+1)+'.mp4'
    self.thread.animationpath =self.animationpath
    set_caption(self, pagenr)
    self.huidig_kind.pages_read.append(int(pagenr/2)+1)
    self.thread.kill()
    time.sleep(0.1)
    if pagenr % 2 == 0 or self.page_nr == 1:
        self.thread.start()
        time.sleep(0.2)
        self.replay_img.setPixmap(QPixmap('images/repeat_unactive.PNG'))
        if self.doorklikken==False:
            self.previouspagebutton.hide()
            self.previouspagebutton.setEnabled(False)
            self.previouspagebutton_img.hide()
            self.nextpagebutton.hide()
            self.nextpagebutton.setEnabled(False)
            self.nextpagebutton_img.hide()
    #keuze vastleg knop alleen op bepaalde paginas
    if np.isin(self.page_nr, [7,9,17]):
        self.capturebutton.show()
        self.capturebutton.setEnabled(True)
        self.capture_img.setPixmap(QPixmap('images/vastleggen.png'))
    else:
        self.capturebutton.hide()
        self.capturebutton.setEnabled(False)
        self.capture_img.setPixmap(QPixmap('images/empty.jpeg'))
    #geluidenknop aan of niet, en alleen op bepaalde paginas
    if np.isin(self.page_nr, [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) and self.geluidknop: 
        self.geluid.show()
        self.geluid.setEnabled(True)
        if self.page_nr == 2 or self.page_nr ==3:
            self.geluid_img.setPixmap(QPixmap('images/koe.png'))
        elif self.page_nr == 6 or self.page_nr ==7:
            self.geluid_img.setPixmap(QPixmap('images/hond.png'))
        elif self.page_nr == 10 or self.page_nr ==11:
            self.geluid_img.setPixmap(QPixmap('images/varken.png'))
        elif self.page_nr == 12 or self.page_nr ==13:
            self.geluid_img.setPixmap(QPixmap('images/kuiken.png'))
        elif self.page_nr == 18 or self.page_nr ==19:
            self.geluid_img.setPixmap(QPixmap('images/schaap.png'))
        else:
            self.geluid_img.setPixmap(QPixmap('images/sound.png'))
    else:
        self.geluid.hide()
        self.geluid.setEnabled(False)
        self.geluid_img.setPixmap(QPixmap('images/empty.jpeg'))
    #opnieuwknop aan of niet
    if self.opnieuwknop == True:
        self.replay.show()
        self.replay.setEnabled(True)
        self.replay_img.show()
    else:
        self.replay.hide()
        self.replay.setEnabled(False)
        self.replay_img.hide()
    

#%%
#Dit is het paralelle proces waarin de video wordt afgespeeld
class Thread(QThread):
    #signaalding om te sturen dat het scherm geupdate moet worden
    changePixmap = pyqtSignal(QImage)
    activateReplayButton = pyqtSignal()
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
                p = convertToQtFormat.scaled(1255, 960, Qt.KeepAspectRatio) 
                #stuur update signaal
                self.changePixmap.emit(p)
                
                
            if self.running==False:

                break
            #zorg dat je niet te snel afspeelt
            time.sleep(0.009)
            if ret == False:
                print('video done')
                self.activateReplayButton.emit()
                break
        self.running=False
    #stop het proces zodat je pc niet vastloopt en je spyder honderduizend keer moet opstarten wat een teringzooi
    def kill(self):
        self.running = False
        self.activateReplayButton.emit()
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
                 "hond":"Sounds\hond.mp3",
                 "geit": "Sounds\geit.mp3",
                 "vogel": "Sounds\vogel.mp3", 
                 "kip": "Sounds\kip.mp3",
                 "haan": "Sounds\haan.mp3"}
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

            
    #stop het proces zodat je pc niet vastloopt en je spyder honderduizend keer moet opstarten wat een gedoe
    def kill(self):
        self.running = False
        print('received stop signal from window.(2)')
        
class Thread3(QThread):    
    #blijft draaien zolang dit waar is
    running=True
    soundpath='Sounds\\eend.mp3'
    sounddict = {10 : "Sounds\\varken.mp3",
             12 : "Sounds\\kuiken.mp3",
             2 : "Sounds\\koe.mp3",
             18 :"Sounds\\schaap.mp3",
             6:"Sounds\\hond.mp3",
             0: "Sounds\\eend.mp3",
             11 : "Sounds\\varken.mp3",
             13 : "Sounds\\kuiken.mp3",
             3: "Sounds\\koe.mp3",
             19 :"Sounds\\schaap.mp3",
             7:"Sounds\\hond.mp3",
             0: "Sounds\\eend.mp3",
             14: "Sounds\\geit.mp3",
             15: "Sounds\\geit.mp3",
             8: "Sounds\\vogel.mp3", 
             9: "Sounds\\vogel.mp3", 
             16: "Sounds\\kip.mp3",
             17: "Sounds\\kip.mp3",
             4: "Sounds\\haan.mp3",
             5: "Sounds\\haan.mp3"}
    pagenr=0
    
    def run(self):
        
        self.soundpath=self.sounddict[self.pagenr]
        
        playsound(self.soundpath)
        return
    #stop het proces zodat je pc niet vastloopt en je spyder honderdduizend keer moet opstarten wat een teringzooi
    def kill(self):
        self.running = False
        print('received stop signal from window.(3)')
class Child: 
    def __init__(self, name, img, pages_read, font_size, geluid_zichtbaar, opnieuw_zichtbaar, prikkelarm, knopgr): 
        self.name = name
        self.img = img
        self.pages_read = pages_read
        self.font_size = font_size
        self.geluid_zichtbaar = geluid_zichtbaar
        self.opnieuw_zichtbaar = opnieuw_zichtbaar 
        self.prikkelarm = prikkelarm
        self.knopgr = knopgr
        
        #def show_kid(self):
            #pixmap = QPixmap(self.img)
            #return pixmap
        #[m,c]=[0,1]
        #beginview: kinderen

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
    @pyqtSlot()
    def activate_replay_button(self):
        if self.huidig_kind.knopgr ==0:
            self.replay_img.setPixmap(QPixmap('images/sizes/repeat_s.PNG'))
        elif self.huidig_kind.knopgr ==1:
            self.replay_img.setPixmap(QPixmap('images/sizes/repeat_m.PNG'))
        else:
            self.replay_img.setPixmap(QPixmap('images/sizes/repeat_l.PNG'))
        self.previouspagebutton.show()
        self.previouspagebutton.setEnabled(True)
        self.previouspagebutton_img.show()
        self.nextpagebutton.show()
        self.nextpagebutton.setEnabled(True)
        self.nextpagebutton_img.show()


        
    #er is op kruisje gedrukt dus sluit alles correct af    
    def closeEvent(self, event):
        
        self.thread.kill()
        self.thread2.kill()
        self.thread3.kill()
        #sla settings van kind op -> in vervolg -> open kinderen met settings
        print("Closing")
        print("Je mag dit scherm nu afsluiten.")

        with open('data_kinderen.pkl', 'wb') as output:
            pickle.dump(self.dummy, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.dummy2, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.dummy3, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.dummy4, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.dummy5, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.dummy6, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.dummy7, output, pickle.HIGHEST_PROTOCOL)

        #self.destory()
        
    def __init__(self, app):

        super(Ui, self).__init__()
        #global variables
        self.page_nr=0
        self.page_order = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
        self.geluidknop=True
        self.opnieuwknop=True
        self.doorklikken = True
        #laad de interface file
        uic.loadUi('test.ui', self)
        self.show()
        #laat eerst programma zien en laad dan pas het model
        #[m,mf,c] = load_model()
        #kinderen
        self.dummy = Child('Tim', 'images/sdier1.png', [], 13, 0, 0, 0, 0)
        self.dummy2 = Child('Lieke', 'images/sdier2.png', [], 13, 0, 0, 0, 0)
        self.dummy3 = Child('Jorik','images/sdier3.png', [], 13, 0, 0, 0, 0)
        self.dummy4 = Child('Noraja','images/sdier4.png', [], 13, 0, 0, 0, 0)
        self.dummy5 = Child('Sophie','images/sdier7.png', [], 13, 0, 0, 0, 0)
        self.dummy6 = Child('Arjan','images/sdier6.png', [], 13, 0, 0, 0, 0)
        self.dummy7 = Child('Anne','images/sdier5.png', [], 13, 0, 0, 0, 0)
        
         #comment dit stuk weg als je weer from scratch wil beginnen
         #met alle instellingen gedelete
        with open('data_kinderen.pkl', 'rb') as input:
            self.dummy = pickle.load(input)
            self.dummy2 = pickle.load(input)
            self.dummy3 = pickle.load(input)
            self.dummy4 = pickle.load(input)
            self.dummy5 = pickle.load(input)
            self.dummy6 = pickle.load(input)
            self.dummy7 = pickle.load(input)
        
        
        #huidig dummy kind
        self.huidig_kind = Child('Dummy', 'images/arjan.png', [], 13, 0, 0, 0, 0) #wordt bepaald in een functie aan de hand van welk kind er geklikt is.

        #[m,c]=[0,1]
        #beginview: kinderen
        #self.child = self.findChild(QtWidgets.QPushButton, 'Tim_old')
        #self.child.clicked.connect(self.set_book_window)

        #kinderen connecten aan volgende pagina
        self.child1 = self.findChild(QtWidgets.QPushButton, 'kind1')
        self.child1.clicked.connect(self.set_book_window)
        self.child1.clicked.connect(self.set_child1)

        self.child2 = self.findChild(QtWidgets.QPushButton, 'kind2')
        self.child2.clicked.connect(self.set_book_window)
        self.child2.clicked.connect(self.set_child2)

        self.child3 = self.findChild(QtWidgets.QPushButton, 'kind3')
        self.child3.clicked.connect(self.set_book_window)
        self.child3.clicked.connect(self.set_child3) 

        self.child4 = self.findChild(QtWidgets.QPushButton, 'kind4')
        self.child4.clicked.connect(self.set_book_window) 
        self.child4.clicked.connect(self.set_child4)

        self.child5 = self.findChild(QtWidgets.QPushButton, 'kind5')
        self.child5.clicked.connect(self.set_book_window) 
        self.child5.clicked.connect(self.set_child5)

        self.child6 = self.findChild(QtWidgets.QPushButton, 'kind6')
        self.child6.clicked.connect(self.set_book_window)
        self.child6.clicked.connect(self.set_child6)

        self.child7 = self.findChild(QtWidgets.QPushButton, 'kind7')
        self.child7.clicked.connect(self.set_book_window)
        self.child7.clicked.connect(self.set_child7)

        #view met de verschillende boeken
        self.book1 = self.findChild(QtWidgets.QPushButton, 'book1')
        self.book1.clicked.connect(self.set_page_window) 
        self.boek1_cover = self.findChild(QtWidgets.QLabel, 'boek_cover')
        self.boek1_cover.setPixmap(QPixmap('images/boek_cover.png'))
        
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
        #page_read voor elke pagina
        self.page_read1 = self.findChild(QtWidgets.QLabel, 'page_read1')
        self.page_read1.setPixmap(QPixmap('images/empty.JPEG'))
        self.page_read2 = self.findChild(QtWidgets.QLabel, 'page_read2')
        self.page_read2.setPixmap(QPixmap('images/empty.JPEG'))
        self.page_read3 = self.findChild(QtWidgets.QLabel, 'page_read3')
        self.page_read3.setPixmap(QPixmap('images/empty.JPEG'))
        self.page_read4 = self.findChild(QtWidgets.QLabel, 'page_read4')
        self.page_read4.setPixmap(QPixmap('images/empty.JPEG'))
        self.page_read5 = self.findChild(QtWidgets.QLabel, 'page_read5')
        self.page_read5.setPixmap(QPixmap('images/empty.JPEG'))
        self.page_read6 = self.findChild(QtWidgets.QLabel, 'page_read6')
        self.page_read6.setPixmap(QPixmap('images/empty.JPEG'))
        self.page_read7 = self.findChild(QtWidgets.QLabel, 'page_read7')
        self.page_read7.setPixmap(QPixmap('images/empty.JPEG'))
        self.page_read8 = self.findChild(QtWidgets.QLabel, 'page_read8')
        self.page_read8.setPixmap(QPixmap('images/empty.JPEG'))
        self.page_read9 = self.findChild(QtWidgets.QLabel, 'page_read9')
        self.page_read9.setPixmap(QPixmap('images/empty.JPEG'))
        self.page_read10 = self.findChild(QtWidgets.QLabel, 'page_read10')
        self.page_read10.setPixmap(QPixmap('images/empty.JPEG'))
        self.page_read11 = self.findChild(QtWidgets.QLabel, 'page_read11')
        self.page_read11.setPixmap(QPixmap('images/empty.JPEG'))

        self.vinkjeslijst = [self.page_read1, self.page_read2, self.page_read3, self.page_read4, self.page_read5, self.page_read6, self.page_read7, self.page_read8, self.page_read9, self.page_read10, self.page_read11]
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
        self.capture_img = self.findChild(QtWidgets.QLabel, 'capture_img')
        
        self.replay = self.findChild(QtWidgets.QPushButton, 'opnieuw')
        self.replay_img = self.findChild(QtWidgets.QLabel, 'opnieuw_img')
        self.replay_img.setPixmap(QPixmap('images/repeat.PNG'))
        self.replay.clicked.connect(self.replay_animation)

        self.geluid = self.findChild(QtWidgets.QPushButton, 'geluid')
        self.geluid_img = self.findChild(QtWidgets.QLabel, 'geluid_img')
        self.geluid_img.setPixmap(QPixmap('images/sound.png'))
        self.geluid.clicked.connect(self.play_sound)

        self.terug_overzicht = self.findChild(QtWidgets.QLabel, 'terug_overzicht')

        
        #Dit stukje gaat over de videoplayer, met self.thread.start() begint hij met het afspelen van de animatie
        self.videoplayer = self.findChild(QtWidgets.QLabel, 'videoplayer' )
        self.camplayer = self.findChild(QtWidgets.QLabel, 'camplayer' )
        self.thread = Thread(self)
        self.thread.changePixmap.connect(self.setImage)
        self.thread.activateReplayButton.connect(self.activate_replay_button)
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
        
        self.instellingen = self.findChild(QtWidgets.QPushButton, 'instellingen')
        self.instellingen.setEnabled(False)
        self.instellingen.clicked.connect(self.instellingen_menu) 

        self.instellingen_open = self.findChild(QtWidgets.QLabel, 'instellingen_open')
        self.instellingen_open.lower()
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

        #instellingen labels en knoppen
        self.instellingen_close = self.findChild(QtWidgets.QPushButton, 'instellingen_close')
        self.instellingen_close.lower()
        self.instellingen_close.setEnabled(False)
        self.instellingen_close.clicked.connect(self.close_instellingen)
        self.instelling_grid = self.findChild(QtWidgets.QWidget, 'instelling_grid')
        self.instelling_grid.lower()
        self.instelling_widg = self.findChild(QtWidgets.QWidget, 'instelling_widg')
        self.instelling_widg.lower()

        self.knopsmall_img = self.findChild(QtWidgets.QLabel, 'knopsmall_img')
        self.knopsmall_img.setPixmap(QPixmap('images/small.png'))
        self.knopsmall = self.findChild(QtWidgets.QPushButton, 'knopsmall')
        self.knopsmall.clicked.connect(self.set_small_buttons)
        self.knopmedium_img = self.findChild(QtWidgets.QLabel, 'knopmedium_img')
        self.knopmedium_img.setPixmap(QPixmap('images/medium_unactive.png'))
        self.knopmedium = self.findChild(QtWidgets.QPushButton, 'knopmedium')
        self.knopmedium.clicked.connect(self.set_medium_buttons)
        self.knoplarge_img = self.findChild(QtWidgets.QLabel, 'knoplarge_img')
        self.knoplarge_img.setPixmap(QPixmap('images/large_unactive.png'))
        self.knoplarge = self.findChild(QtWidgets.QPushButton, 'knoplarge')
        self.knoplarge.clicked.connect(self.set_large_buttons)

        self.instelling_geluid = self.findChild(QtWidgets.QLabel, 'instelling_geluid')
        self.instelling_geluid.setPixmap(QPixmap('images/sizes/music_s.png'))
        self.instelling_geluid_knop = self.findChild(QtWidgets.QPushButton, 'geluid_knop')
        self.instelling_geluid_knop.clicked.connect(self.geluid_aan_uit)

        self.instelling_opnieuw = self.findChild(QtWidgets.QLabel, 'instelling_opnieuw')
        self.instelling_opnieuw.setPixmap(QPixmap('images/repeat_instelling.png'))
        self.instelling_opnieuw_knop = self.findChild(QtWidgets.QPushButton, 'opnieuw_knop')
        self.instelling_opnieuw_knop.clicked.connect(self.opnieuw_aan_uit)
        
        self.letters_klein = self.findChild(QtWidgets.QPushButton, 'letters_klein')
        self.letters_klein.clicked.connect(self.font_small)
        self.letters_medium = self.findChild(QtWidgets.QPushButton, 'letters_medium')
        self.letters_medium.clicked.connect(self.font_medium)
        self.letters_groot = self.findChild(QtWidgets.QPushButton, 'letters_groot')
        self.letters_groot.clicked.connect(self.font_large)

        self.aanuit_img = self.findChild(QtWidgets.QLabel, 'aanuit_img')
        self.aanuit_img.setPixmap(QPixmap('images/switch_on.png'))
        self.aanuit_knop = self.findChild(QtWidgets.QPushButton, 'aanuit_knop')
        self.aanuit_knop.clicked.connect(self.aanuit_prikkelarm)

        #plaatjes kinderen
        self.child1_img = self.findChild(QtWidgets.QLabel, 'tim_img')
        self.child1_img.setPixmap(QPixmap('images/dier1.PNG'))

        self.child2_img = self.findChild(QtWidgets.QLabel, 'lieke_img')
        self.child2_img.setPixmap(QPixmap('images/dier2.PNG'))

        self.child3_img = self.findChild(QtWidgets.QLabel, 'jorik_img')
        self.child3_img.setPixmap(QPixmap('images/dier3.PNG'))

        self.child4_img = self.findChild(QtWidgets.QLabel, 'noraja_img')
        self.child4_img.setPixmap(QPixmap('images/dier4.PNG'))

        self.child5_img = self.findChild(QtWidgets.QLabel, 'annsophie_img')
        self.child5_img.setPixmap(QPixmap('images/dier7.PNG'))

        self.child6_img = self.findChild(QtWidgets.QLabel, 'annemiek_img')
        self.child6_img.setPixmap(QPixmap('images/dier5.PNG'))

        self.child7_img = self.findChild(QtWidgets.QLabel, 'arjan_img')
        self.child7_img.setPixmap(QPixmap('images/dier6.PNG'))

        #add kind knop
        #self.add = self.findChild(QtWidgets.QLabel, 'add')
        #pixmap11 = QPixmap('images/add.PNG')
        #self.add.setPixmap(pixmap11)

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
        
        self.name_kid = self.findChild(QtWidgets.QLabel, 'name_kid')
        self.img_kid = self.findChild(QtWidgets.QLabel, 'img_kid')

        
    #verander kind
    def set_child1(self):
        self.huidig_kind = self.dummy2
        for pagina in self.vinkjeslijst:
            pagina.setPixmap(QPixmap('images/empty.JPEG')) 
            #nu reset ie wat er al is gelezen, maar dit moet dus opgeslagen worden bij het afsluiten en opstarten van het programma
        self.huidig_kind.opnieuw_zichtbaar += -1
        self.opnieuw_aan_uit()
        self.huidig_kind.geluid_zichtbaar += -1
        self.geluid_aan_uit()
        self.huidig_kind.prikkelarm += -1
        self.aanuit_prikkelarm()
        if self.huidig_kind.font_size == 13:
            self.font_small()
        elif self.huidig_kind.font_size == 17:
            self.font_medium()
        else:
            self.font_large()
        if self.huidig_kind.knopgr ==0:
            self.set_small_buttons()
        elif self.huidig_kind.knopgr ==1:
            self.set_medium_buttons()
        else:
            self.set_large_buttons()


    def set_child2(self):
        self.huidig_kind = self.dummy
        for pagina in self.vinkjeslijst:
            pagina.setPixmap(QPixmap('images/empty.JPEG'))  
        self.huidig_kind.opnieuw_zichtbaar += -1
        self.opnieuw_aan_uit()  
        self.huidig_kind.geluid_zichtbaar += -1
        self.geluid_aan_uit()
        self.huidig_kind.prikkelarm += -1
        self.aanuit_prikkelarm()
        if self.huidig_kind.font_size == 13:
            self.font_small()
        elif self.huidig_kind.font_size == 17:
            self.font_medium()
        else:
            self.font_large()
        if self.huidig_kind.knopgr ==0:
            self.set_small_buttons()
        elif self.huidig_kind.knopgr ==1:
            self.set_medium_buttons()
        else:
            self.set_large_buttons()    

    def set_child3(self):
        self.huidig_kind = self.dummy3
        for pagina in self.vinkjeslijst:
            pagina.setPixmap(QPixmap('images/empty.JPEG'))  
        self.huidig_kind.opnieuw_zichtbaar += -1
        self.opnieuw_aan_uit()  
        self.huidig_kind.geluid_zichtbaar += -1
        self.geluid_aan_uit()
        self.huidig_kind.prikkelarm += -1
        self.aanuit_prikkelarm()
        if self.huidig_kind.font_size == 13:
            self.font_small()
        elif self.huidig_kind.font_size == 17:
            self.font_medium()
        else:
            self.font_large()
        self.change_buttons()
        if self.huidig_kind.knopgr ==0:
            self.set_small_buttons()
        elif self.huidig_kind.knopgr ==1:
            self.set_medium_buttons()
        else:
            self.set_large_buttons()

    def set_child4(self):
        self.huidig_kind = self.dummy4
        for pagina in self.vinkjeslijst:
            pagina.setPixmap(QPixmap('images/empty.JPEG'))  
        self.huidig_kind.opnieuw_zichtbaar += -1
        self.opnieuw_aan_uit()  
        self.huidig_kind.geluid_zichtbaar += -1
        self.geluid_aan_uit()
        self.huidig_kind.prikkelarm += -1
        self.aanuit_prikkelarm()
        if self.huidig_kind.font_size == 13:
            self.font_small()
        elif self.huidig_kind.font_size == 17:
            self.font_medium()
        else:
            self.font_large()
        self.change_buttons()
        if self.huidig_kind.knopgr ==0:
            self.set_small_buttons()
        elif self.huidig_kind.knopgr ==1:
            self.set_medium_buttons()
        else:
            self.set_large_buttons()

    def set_child5(self):
        self.huidig_kind = self.dummy5
        for pagina in self.vinkjeslijst:
            pagina.setPixmap(QPixmap('images/empty.JPEG'))  
        self.huidig_kind.opnieuw_zichtbaar += -1
        self.opnieuw_aan_uit()  
        self.huidig_kind.geluid_zichtbaar += -1
        self.geluid_aan_uit()
        self.huidig_kind.prikkelarm += -1
        self.aanuit_prikkelarm()
        if self.huidig_kind.font_size == 13:
            self.font_small()
        elif self.huidig_kind.font_size == 17:
            self.font_medium()
        else:
            self.font_large()
        self.change_buttons()
        if self.huidig_kind.knopgr ==0:
            self.set_small_buttons()
        elif self.huidig_kind.knopgr ==1:
            self.set_medium_buttons()
        else:
            self.set_large_buttons()

    def set_child6(self):
        self.huidig_kind = self.dummy6
        for pagina in self.vinkjeslijst:
            pagina.setPixmap(QPixmap('images/empty.JPEG'))  
        self.huidig_kind.opnieuw_zichtbaar += -1
        self.opnieuw_aan_uit()  
        self.huidig_kind.geluid_zichtbaar += -1
        self.geluid_aan_uit()
        self.huidig_kind.prikkelarm += -1
        self.aanuit_prikkelarm()
        if self.huidig_kind.font_size == 13:
            self.font_small()
        elif self.huidig_kind.font_size == 17:
            self.font_medium()
        else:
            self.font_large()
        self.change_buttons()
        if self.huidig_kind.knopgr ==0:
            self.set_small_buttons()
        elif self.huidig_kind.knopgr ==1:
            self.set_medium_buttons()
        else:
            self.set_large_buttons()

    def set_child7(self):
        self.huidig_kind = self.dummy7
        for pagina in self.vinkjeslijst:
            pagina.setPixmap(QPixmap('images/empty.JPEG'))  
        self.huidig_kind.opnieuw_zichtbaar += -1
        self.opnieuw_aan_uit()  
        self.huidig_kind.geluid_zichtbaar += -1
        self.geluid_aan_uit()
        self.huidig_kind.prikkelarm += -1
        self.aanuit_prikkelarm()
        if self.huidig_kind.font_size == 13:
            self.font_small()
        elif self.huidig_kind.font_size == 17:
            self.font_medium()
        else:
            self.font_large()
        self.change_buttons()
        if self.huidig_kind.knopgr ==0:
            self.set_small_buttons()
        elif self.huidig_kind.knopgr ==1:
            self.set_medium_buttons()
        else:
            self.set_large_buttons()
            

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
    

        

    def set_children_window(self):
        self.stackedWidget.setCurrentIndex(0)
        self.foldin_menu()
        print('changed window to children')
    def set_instellingen_window(self):
        self.stackedwidget.setCurrentIndex(1)
        self.foldin_menu()
    def set_page_window(self):
        self.stackedWidget.setCurrentIndex(2)
        self.foldin_menu()
        self.name_kid.setText(self.huidig_kind.name) 
        self.img_kid.setPixmap(QPixmap(self.huidig_kind.img))
        self.apply_checked()
        print('changed window to pages')  

    def apply_checked(self):
        #print(self.huidig_kind.pages_read)
        for pagina in self.huidig_kind.pages_read:
            self.vinkjeslijst[pagina-1].setPixmap(QPixmap('images/checked.PNG'))
    
    def set_book_window(self):
        self.stackedWidget.setCurrentIndex(4)
        self.foldin_menu()
        print('changed window to bookview')  
    def replay_animation(self):
        if self.thread.running == True:
            #self.thread.kill()
            #time.sleep(0.1)
            #knop doet niks tijdens afspelen
            return
        self.replay_img.setPixmap(QPixmap('images/repeat_unactive.png'))
        if self.doorklikken==False:
            self.previouspagebutton.hide()
            self.previouspagebutton.setEnabled(False)
            self.previouspagebutton_img.hide()
            self.nextpagebutton.hide()
            self.nextpagebutton.setEnabled(False)
            self.nextpagebutton_img.hide()
        self.thread.start()
        #self.thread2.start()
        print('thread started')
    def play_sound(self):
        self.thread3.pagenr=self.page_nr
        self.thread3.start()

    def turn_page_next(self):        
        if(self.page_nr<22):
            self.page_nr+=1
            if self.page_nr==21:
                self.terug_overzicht.setText("Terug naar pagina overzicht")
            else:
                self.terug_overzicht.setText(" ")
        self.pagenrlabel.setText(str(self.page_nr))
        if self.thread.running==True:
            self.thread.kill()
            time.sleep(0.1)
        if self.page_nr==22:
            self.set_page_window()
        else:
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
        if self.thread.running==True:
            self.thread.kill()
            time.sleep(0.1)
        load_page(self, self.page_order[self.page_nr-1])
        print('page set to: ' + str(self.page_nr))
        
    def foldout_menu(self):
        print("menu expanded")
        #self.thread3.start() #HAHA I found the quack
        #verander hamburgerknop in uitgeklapt menu
        self.hamburger_uit_img.setPixmap(QPixmap('images/allessamen.PNG'))
        self.hamburger_img.setPixmap(QPixmap('images/empty.JPEG'))
        #enable knoppen in menu
        self.hamburger.setEnabled(False)
        self.exit.setEnabled(True)
        self.instellingen.setEnabled(True)
        self.naar_klas.setEnabled(True)
        self.naar_boeken.setEnabled(True)
        self.naar_paginas.setEnabled(True)
        #laat eventuele tekst op knoppen verschijnen
        self.naar_klas.setText('Klas')
        self.naar_boeken.setText('Boeken')
        self.naar_paginas.setText('Pagina Overzicht')
    def foldin_menu(self):
        print("menu ingeklapt")
        #verander terug in menuknop
        self.hamburger_uit_img.setPixmap(QPixmap('images/empty.JPEG'))
        self.hamburger_img.setPixmap(QPixmap('images/menuknop.PNG'))
        #enable/disable knoppen
        self.hamburger.setEnabled(True)
        self.exit.setEnabled(False)
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
        self.instellingen_open.raise_()
        self.instellingen_open.setPixmap(QPixmap('images/instelling_backblack.PNG'))
        self.instellingen_close.raise_()
        self.instellingen_close.setEnabled(True)
        self.foldin_menu()
        self.instelling_grid.raise_()
        self.instelling_widg.raise_()
    
    def capture_choice(self):
        print('capturing choice')
        self.thread2.start()
    def close_instellingen(self):
        self.instellingen_open.lower()
        self.instellingen_open.setPixmap(QPixmap('images/empty.JPEG'))
        self.instellingen_close.lower()
        self.instellingen_close.setEnabled(False)
        self.instelling_grid.lower()
        self.instelling_widg.lower()

        load_page(self, self.page_nr)

    def set_small_buttons(self):
        self.huidig_kind.knopgr = 0
        self.knopsmall_img.setPixmap(QPixmap('images/small.png'))
        self.knopmedium_img.setPixmap(QPixmap('images/medium_unactive.png'))
        self.knoplarge_img.setPixmap(QPixmap('images/large_unactive.png'))
        self.change_buttons()
    def set_medium_buttons(self):
        self.huidig_kind.knopgr = 1
        self.knopsmall_img.setPixmap(QPixmap('images/small_unactive.png'))
        self.knopmedium_img.setPixmap(QPixmap('images/medium.png'))
        self.knoplarge_img.setPixmap(QPixmap('images/large_unactive.png'))
        self.change_buttons()
    def set_large_buttons(self):
        self.huidig_kind.knopgr = 2
        self.knopsmall_img.setPixmap(QPixmap('images/small_unactive.png'))
        self.knopmedium_img.setPixmap(QPixmap('images/medium_unactive.png'))
        self.knoplarge_img.setPixmap(QPixmap('images/large.png'))
        self.change_buttons()

    def change_buttons(self):
        #print("knoppen veranderen")
        if self.huidig_kind.knopgr == 0: 
            print("de knoppen zijn nu klein")
            self.previouspagebutton_img.resize(151,131)
            self.previouspagebutton_img.setPixmap(QPixmap('images/sizes/back_s.png'))
            self.previouspagebutton.setGeometry(540,950,71,81)

            self.nextpagebutton_img.resize(151,131)
            self.nextpagebutton_img.setPixmap(QPixmap('images/sizes/next_s.png'))
            self.nextpagebutton.setGeometry(1600,950,71,81)

            self.replay_img.resize(141,121)
            self.replay_img.setPixmap(QPixmap('images/sizes/repeat_s.png'))
            self.replay.setGeometry(1050,950,71,81)

            self.geluid_img.setGeometry(470,30,181,151)
            self.geluid_img.setPixmap(QPixmap('images/sizes/music_s.png'))
            self.geluid.setGeometry(470,30,151,121)

            
        elif self.huidig_kind.knopgr ==1:
            print("de knoppen zijn nu medium groot")
            self.previouspagebutton_img.resize(151,131)
            self.previouspagebutton_img.setPixmap(QPixmap('images/sizes/back_m.png'))
            self.previouspagebutton.setGeometry(540,950,81,91)

            self.nextpagebutton_img.resize(151,131)
            self.nextpagebutton_img.setPixmap(QPixmap('images/sizes/next_m.png'))
            self.nextpagebutton.setGeometry(1600,950,81,91)

            self.replay_img.resize(141,121)
            self.replay_img.setPixmap(QPixmap('images/sizes/repeat_m.png'))
            self.replay.setGeometry(1050,950,81,91)

            self.geluid_img.setGeometry(470,30,181,151)
            self.geluid_img.setPixmap(QPixmap('images/sizes/music_m.png'))
            self.geluid.setGeometry(470,30,151,121)
        else:
            print("de knoppen zijn nu groot")
            self.previouspagebutton_img.setGeometry(510,910,171,161)
            self.previouspagebutton_img.setPixmap(QPixmap('images/sizes/back_l.png'))
            self.previouspagebutton.setGeometry(530,920,121,121)

            self.nextpagebutton_img.setGeometry(1570,910,171,161)
            self.nextpagebutton_img.setPixmap(QPixmap('images/sizes/next_l.png'))
            self.nextpagebutton.setGeometry(1590,920,121,121)

            self.replay_img.setGeometry(1010,910,171,161)
            self.replay_img.setPixmap(QPixmap('images/sizes/repeat_l.png'))
            self.replay.setGeometry(1030,920,121,121)

            self.geluid_img.setGeometry(470,50,181,161)
            self.geluid_img.setPixmap(QPixmap('images/sizes/music_l.png'))
            self.geluid.setGeometry(480,60,151,131)

    
    def font_small(self):
        self.huidig_kind.font_size = 13
        self.letters_klein.setStyleSheet("QPushButton{color:orange;text-decoration:underline;border-top:3px transparent;border-bottom: 3px transparent;border-right: 10px transparent;border-left: 10px transparent;}")
        self.letters_medium.setStyleSheet("QPushButton{color:grey;text-decoration:none;border-top:3px transparent;border-bottom: 3px transparent;border-right: 10px transparent;border-left: 10px transparent;}")
        self.letters_groot.setStyleSheet("QPushButton{color:grey;text-decoration:none;border-top:3px transparent;border-bottom: 3px transparent;border-right: 10px transparent;border-left: 10px transparent;}")

    
    def font_medium(self):
        self.huidig_kind.font_size = 17 
        self.letters_klein.setStyleSheet("QPushButton{color:grey;text-decoration:none;border-top:3px transparent;border-bottom: 3px transparent;border-right: 10px transparent;border-left: 10px transparent;}")
        self.letters_medium.setStyleSheet("QPushButton{color:orange;text-decoration:underline;border-top:3px transparent;border-bottom: 3px transparent;border-right: 10px transparent;border-left: 10px transparent;}")
        self.letters_groot.setStyleSheet("QPushButton{color:grey;text-decoration:none;border-top:3px transparent;border-bottom: 3px transparent;border-right: 10px transparent;border-left: 10px transparent;}")

        
    def font_large(self):
        self.huidig_kind.font_size = 21
        self.letters_klein.setStyleSheet("QPushButton{color:grey;text-decoration:none;border-top:3px transparent;border-bottom: 3px transparent;border-right: 10px transparent;border-left: 10px transparent;}")
        self.letters_medium.setStyleSheet("QPushButton{color:grey;text-decoration:none;border-top:3px transparent;border-bottom: 3px transparent;border-right: 10px transparent;border-left: 10px transparent;}")
        self.letters_groot.setStyleSheet("QPushButton{color:orange;text-decoration:underline;border-top:3px transparent;border-bottom: 3px transparent;border-right: 10px transparent;border-left: 10px transparent;}")

    def geluid_aan_uit(self):
        self.huidig_kind.geluid_zichtbaar += 1
        if (self.huidig_kind.geluid_zichtbaar%2) == 1:
            self.instelling_geluid.setPixmap(QPixmap('images/music_unactive.png'))
            self.geluid_img.setPixmap(QPixmap('images/empty.JPEG'))
            self.geluid.setEnabled(False)
            self.geluidknop=False
            
        else:
            self.instelling_geluid.setPixmap(QPixmap('images/music.png'))
            self.geluid_img.setPixmap(QPixmap('images/music.png'))
            self.geluid.setEnabled(True)
            self.geluidknop=True
        

    def opnieuw_aan_uit(self):
        self.huidig_kind.opnieuw_zichtbaar += 1
        if (self.huidig_kind.opnieuw_zichtbaar%2) ==1:
            self.instelling_opnieuw.setPixmap(QPixmap('images/repeat_unactive.png'))
            self.replay_img.setPixmap(QPixmap('images/empty.JPEG'))
            self.replay.setEnabled(False)
            self.opnieuwknop = False
        else: 
            self.instelling_opnieuw.setPixmap(QPixmap('images/repeat_instelling.png'))
            self.change_buttons()
            self.replay.setEnabled(True)
            self.opnieuwknop = True
    def aanuit_prikkelarm(self): #deze functie kan ook de "doorklikmogelijkheid" worden, of misschien iets van automatisch voorlezen?
        self.huidig_kind.prikkelarm += 1
        if (self.huidig_kind.prikkelarm%2) ==1:
            self.aanuit_img.setPixmap(QPixmap('images/switch_off.png'))
            #er moet iets gebeuren dat het prikkelarm wordt (of andere dingen die gebeuren)
            self.doorklikken = False
        else:
            self.aanuit_img.setPixmap(QPixmap('images/switch_on.png'))
            self.doorklikken = True
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(app)
    window.show()
    #sys.exit()
    sys.exit(app.exec_()) 
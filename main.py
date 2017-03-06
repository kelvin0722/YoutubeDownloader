#!usr/bin/env python
import sys
import  pafy
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "windowdesign.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

path = "/home/kelvin/youtube_downloads"



 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    global path
  
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.labelArtist.setText(self.getartistname())
        self.youtubeurl.insertPlainText('https://www.youtube.com/watch?v=tP2l30oJVts')
        self.youtubeurl.toPlainText()
        self.labelViews.setText(self.getviews())
        self.LabelName.setText(self.getvideoname())
        self.pushButton.clicked.connect(self.download)

    def download(self):
        url = self.youtubeurl.toPlainText()
        video = pafy.new(url)

        try:
            best_vid = video.getbest()
            best_vid.download(filepath=path,quiet=False)
        except FileExistsError as e:
            print "%s"%(e)     
   
    def getviews(self):
        url = self.youtubeurl.toPlainText()
        video = pafy.new(url)
        views = video.viewcount
        return str(views)
    def getvideoname(self):
        videoname = 'Khaligraph jones'
        return videoname

    def getartistname(self):
        artistname = 'kelvin'

        return artistname
                 
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
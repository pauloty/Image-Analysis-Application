from HighDensityActions import *
from lbp_actions import *

from PyQt4 import QtCore, QtGui


from matplotlib.backends.backend_qt4agg import (
    FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)





from MainGui import Ui_MainWindow
from FirstLevel import * 




class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    
    # Ira salvar as imagens de alta e baixa densidade
    high = None
    low = None

    resultSubwindows = []
    
    mainImageSubWindow=None
    
    moduleFrame = None
    
    vsiFileName = None

    # Conecta acoes aos botoes
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)                                         
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.openImage)
        self.actionHigh_density.triggered.connect(self.highDensityAction)
        self.resizeEvent = self.rezize
        self.actionLocal_Binary_Pattern.triggered.connect(self.lbpAction)
    
    
        
    def rezize(self, args):
        del args
        if self.moduleFrame is not None:
            self.moduleFrame.resize(self.modulesFrame.width(), self.modulesFrame.height())      
   
    def highDensityAction(self):
        # Codigo adicionado para fazer a transicao entre os modulos
        if self.moduleFrame is not None:
            self.moduleFrame.close()
            self.moduleFrame = None
        if self.moduleFrame is None: 
            self.moduleFrame = HighDensity(self.modulesFrame)
            self.moduleFrame.setMainWindow(self)
            self.moduleFrame.resize(self.modulesFrame.width(), self.modulesFrame.height())    
            self.moduleFrame.show()

    def lbpAction(self):
        # Codigo adicionado para fazer a transicao entre os modulos
        if self.moduleFrame is not None:
            self.moduleFrame.close()
            self.moduleFrame = None
        if self.moduleFrame is None:
            self.moduleFrame = LBP(self.modulesFrame)
            self.moduleFrame.setMainWindow(self)
            self.moduleFrame.resize(self.modulesFrame.width(), self.modulesFrame.height())
            self.moduleFrame.show()
    
    def showResultSubWindows(self, images):
        
        graphicsViews=[]
        pixmaps = []
        scenes = []
        qImages = []
        
        for i in range(0, len(images)):
            self.resultSubwindows.append(QtGui.QMdiSubWindow())

            self.resultSubwindows[i].setObjectName(_fromUtf8("subWindow_"+str(i)))

            height, width = images[i].shape 
           
            qImages.append(QtGui.QImage(images[i].data, width, height, QtGui.QImage.Format_Indexed8))
            pixmaps.append(QtGui.QPixmap(qImages[i]))
                   
            graphicsViews.append(QtGui.QGraphicsView(self.resultSubwindows[i]))
            self.mdiArea.addSubWindow(self.resultSubwindows[i])
            graphicsViews[i].setGeometry(QtCore.QRect(30, 30, width+10, height+10))
            graphicsViews[i].setObjectName(_fromUtf8("graphicView_"+str(i)))
            
            scenes.append(QtGui.QGraphicsScene()) 
            scenes[i].setSceneRect(QtCore.QRectF(pixmaps[i].rect()))
            scenes[i].addPixmap(pixmaps[i])
            graphicsViews[i].setScene(scenes[i])
            scenes[i].update()
            
            self.resultSubwindows[i].resize(width+60,height+60)
            self.resultSubwindows[i].setWindowTitle(str(i))
            self.resultSubwindows[i].show()

    # Exibe janela do resultado do modulo LBP
    def lbpResultSubWindows(self, histograms):
        """ Metodo alternativo que carrega a imagem salva pelo metodo alternativo dentro do Extrators

        self.lbpResultWindows = QtGui.QMdiSubWindow()

        self.lbpResultWindows.setObjectName(_fromUtf8("subWindow"))
        #images = cv2.imread("D:\\User\\Desktop\\Histopathological-Image-Analysis-Application-master - Copia\\LBP_Result.png")
        #height, width, _ = images.shape

        #qImage = QtGui.QImage(images.data, width, height, QtGui.QImage.Format_Indexed8)
        pixmap = QtGui.QPixmap(_fromUtf8('LBP_Result.png'))

        graphicsView = QtGui.QGraphicsView(self.lbpResultWindows)

        self.mdiArea.addSubWindow(self.lbpResultWindows)

        graphicsView.setGeometry(QtCore.QRect(30, 30, pixmap.width() + 10, pixmap.height() + 10))
        graphicsView.setObjectName(_fromUtf8("graphicView"))

        scene = QtGui.QGraphicsScene()
        scene.addPixmap(pixmap)
        scene.setSceneRect(QtCore.QRectF(pixmap.rect()))
        scene.update()
        graphicsView.setScene(scene)

        self.lbpResultWindows.resize(pixmap.width() + 60, pixmap.height() + 60)
        self.lbpResultWindows.setWindowTitle('LBP Results')
        self.lbpResultWindows.show()
        """

        """  Metodo que exibe o plot ao inves de uma imagem """
        self._canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self._ax = self._canvas.figure.subplots()

        n_bins0 = int(histograms[0].max() + 1)
        n_bins1 = int(histograms[1].max() + 1)
        self._ax.hist(histograms[0].ravel(), n_bins0, range=(0, n_bins0), density=True, label='high')
        self._ax.hist(histograms[1].ravel(), n_bins1, range=(0, n_bins1), density=True, alpha=0.5, label='low')
        self._ax.legend(prop={'size':10})
        self._ax.set_ylabel("% of Pixels")
        self._ax.set_xlabel("LBP pixel bucket")
        self._ax.grid(True)

        widget = QtGui.QMainWindow()
        widget.setCentralWidget(self._canvas)
        widget.addToolBar(
            QtCore.Qt.BottomToolBarArea, NavigationToolbar(self._canvas, self)
        )
        self.lbpResultWindows = QtGui.QMdiSubWindow()
        self.lbpResultWindows.setWidget(widget)
        self.mdiArea.addSubWindow(self.lbpResultWindows)
        self.lbpResultWindows.setWindowTitle('LBP Results')
        self.lbpResultWindows.show()

    def openImage(self):
       
        dialog  =  QtGui.QFileDialog(self)
        dialog.setNameFilter("Images (*.png *.vsi *.jpg)")
        if dialog.exec_():
            self.vsiFileName = str(dialog.selectedFiles()[0])
               
        #open thumbnail
        image = QtGui.QImage(self.vsiFileName)
        
        pixmap =  QtGui.QPixmap(image) 
        
        scene =  QtGui.QGraphicsScene() 
        scene.setSceneRect(QtCore.QRectF(pixmap.rect()))
        scene.addPixmap(pixmap)
        
        if self.mainImageSubWindow is None:
            self.mainImageSubWindow = QtGui.QMdiSubWindow()
            self.mainImageSubWindow.setObjectName(_fromUtf8("Thumbnail"))
            self.graphicsView = QtGui.QGraphicsView(self.mainImageSubWindow)
            self.mdiArea.addSubWindow(self.mainImageSubWindow)
                     
        self.graphicsView.setGeometry(QtCore.QRect(30, 30, image.width()+10, image.height()+10))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        
        self.graphicsView.setScene(scene)
        scene.update()
        
        self.mainImageSubWindow.resize(image.width()+60, image.height()+60)
        self.mainImageSubWindow.setWindowTitle("VSI Thumbnail")
        self.mainImageSubWindow.show()

        '''
        msg = QMessageBox()
        msg.setInformativeText(fileNames[0])
        msg.exec_()
        ''' 

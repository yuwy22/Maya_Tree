__author__ = 'Peipei'

# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
import os.path

#___________________________________________________________________________________________________ Assignment1Widget
class Assignment4Widget(PyGlassWidget):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment4Widget."""
        super(Assignment4Widget, self).__init__(parent, **kwargs)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.confirmBtn.clicked.connect(self._handleConfirmButton)


        #self._statusBox, statusLayout = self._createElementWidget(self, QtGui.QComboBox, True)
        #statusLayout.addStretch()

       # self.objComboBox = object
        #self.shaderComboBox
    def makeCube(self):
        cmds.polyCube (w=5, d=5, h=4)
        #return cube
    def makeSphere(self):
        cmds.sphere( r=3 )

    def makeCylinder(self):

        #This callback creates a polygonal cylinder in the Maya scene.
        r = 50
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder')[0]
        #cmds.select(c)
        #response = nimble.createRemoteResponse(globals())
        #response.put('name', c)

        #return c
    def makeLeaf(self):
        fn1 = os.path.join(os.path.dirname(__file__), 'leaf.ma')
        cmds.file(fn1, i=True)
        #cmds.file('/Users/Peipei/Documents/maya/projects/default/scenes/leaf.ma', i=True)

    def makeLego(self):
        fn2 = os.path.join(os.path.dirname(__file__), 'lego.ma')
        cmds.file(fn2, i=True)
        #cmds.file('/Users/Peipei/Documents/maya/projects/default/scenes/lego.ma', i=True)

    def makeRing(self):
        fn3 = os.path.join(os.path.dirname(__file__), 'ring.ma')
        cmds.file(fn3, i=True)
        #cmds.file('/Users/Peipei/Documents/maya/projects/default/scenes/ring.ma', i=True)

    def goldShader(self):
        fn4 = os.path.join(os.path.dirname(__file__), 'gold.ma')
        cmds.file(fn4, o=True)
        #cmds.file('/Users/Peipei/Documents/maya/projects/default/scenes/gold1.ma', o=True)
        return 'gold'

    def leafShader(self):
        fn5 = os.path.join(os.path.dirname(__file__), 'leafShader.ma')
        cmds.file(fn5, o=True)
        #cmds.file('/Users/Peipei/Documents/maya/projects/default/scenes/leafShader.ma', o=True)
        return 'leaf'

    def woodShader(self):
        fn6 = os.path.join(os.path.dirname(__file__), 'wood.ma')
        cmds.file(fn6, o=True)
        #cmds.file('/Users/Peipei/Documents/maya/projects/default/scenes/wood.ma', o=True)
        return 'wood'

    def alumShader(self):
        fn7 = os.path.join(os.path.dirname(__file__), 'aluminum.ma')
        cmds.file(fn7, o=True)
        #cmds.file('/Users/Peipei/Documents/maya/projects/default/scenes/aluminum.ma', o=True)
        return 'aluminum'
#===================================================================================================
#                                                                    H A N D L E R S
#___________________________________________________________________________________________________ _handleComboBox
    #def _handleGoldButton(self):


    def handleComboBox(self):
        for j in range(self.shaderComboBox.count()):
           # print str(self.shaderComboBox.currentText())
            if (self.shaderComboBox.currentText() == 'Gold'):
                shader = self.goldShader()
                #print shader
            if (self.shaderComboBox.currentText() == 'Leaf'):
                shader = self.leafShader()
            if (self.shaderComboBox.currentText() == 'Wood'):
                shader = self.woodShader()
            if (self.shaderComboBox.currentText() == 'Aluminum'):
                shader = self.alumShader()
        for i in range(self.objComboBox.count()):
           # print i
            #print str(self.objComboBox.currentText())
            if str(self.objComboBox.currentText())=='Cylinder':
               # print str(self.objComboBox.currentText())
                self.makeCylinder()
            if str(self.objComboBox.currentText())=='Lego':
                self.makeLego()
            if str(self.objComboBox.currentText())=='Leaf':
                self.makeLeaf()
            if str(self.objComboBox.currentText())=='Ring':
                self.makeRing()
            if str(self.objComboBox.currentText())=='Cube':
                self.makeCube()
            if str(self.objComboBox.currentText())=='Sphere':
                self.makeSphere()
        return shader


#___________________________________________________________________________________________________ _handleReturnHome
    def _handleConfirmButton(self):
        sha = self.handleComboBox()
        #cmds.file('/Users/Peipei/Documents/maya/projects/default/scenes/'+sha+'.ma', o=True)
        #cube = cmds.polyCube (w=5, d=5, h=4)
        cmds.select(all=True)
        cmds.hyperShade(assign= sha)
    #cmds.sets(forceElement='gold'+'.SG')


#___________________________________________________________________________________________________ _handleReturnHome


#__________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

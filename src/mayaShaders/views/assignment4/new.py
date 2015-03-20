__author__ = 'Peipei'

# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment1Widget
class Assignment4Widget(PyGlassWidget):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment4Widget."""
        super(Assignment4Widget, self).__init__(parent, **kwargs)
        self.confirmBtn.clicked.connect(self._handleConfirmButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)

    def makeCube(self):
        cube = cmds.polyCube (w=5, d=5, h=4)
        return cube

    def makeCylinder(self):
        cylinder = cmds.cylinder( ch=True, radius=3, hr=3 )
        return cylinder

    def goldShader(self):
        gold = cmds.file('/Users/Peipei/Documents/maya/projects/default/scenes/gold.ma', o=True)
        return gold

#===================================================================================================
#                                                                    H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleConfirmButton(self, obj, s):
        object = obj
        shader = s
        cmds.file('/Users/Peipei/Documents/maya/projects/default/scenes/'+shader+'.ma', o=True)
        #cube = cmds.polyCube (w=5, d=5, h=4)

        cmds.select(object)
        cmds.hyperShade(assign= shader)
    #cmds.sets(forceElement='gold'+'.SG')





    def _handleCylinderButton(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        r = 50
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)

#___________________________________________________________________________________________________ _handleComboBox
    #def _handleGoldButton(self):


    def handleComboBox(self):
        for i in range(objComboBox.count()):
            if (self.currentIndex==0):
                object = self.makeCylinder()
        for j in range(shaderComboBox.count()):
            if (self.currentIndex == 0):
                shader = self.goldShader()
        return object, shader

        #if self.selectionMethod1CmbxcurrentText()==self.FETCH_TRACK_BY_NAME:
            #self.handleFetchByName()
        #elif self.selectionMethod1Cmbx.currentText() ==self.FETCH_TRACK_BY_INDEX:
            #self.handleFetchByIndex()

#__________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')






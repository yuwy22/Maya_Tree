__author__ = 'Peipei'
# MayaPyHomeWidget.py
# (C)2013
# Scott Ernst

from PySide import QtGui

from pyglass.widgets.PyGlassWidget import PyGlassWidget

from mayaShaders.enum.UserConfigEnum import UserConfigEnum
from mayaShaders.views.home.NimbleStatusElement import NimbleStatusElement

#___________________________________________________________________________________________________ MayaPyHomeWidget
class MayaShaderHomeWidget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of MayaPyHomeWidget."""
        super(MayaShaderHomeWidget, self).__init__(parent, **kwargs)
        self._firstView = True

        #self.assignment1Btn.clicked.connect(self._handleAssignment1)
        self.assignment4Btn.clicked.connect(self._handleAssignment4)

        self._statusBox, statusLayout = self._createElementWidget(self, QtGui.QVBoxLayout, True)
        statusLayout.addStretch()

        self._nimbleStatus = NimbleStatusElement(
            self._statusBox,
            disabled=self.mainWindow.appConfig.get(UserConfigEnum.NIMBLE_TEST_STATUS, True) )
        statusLayout.addWidget(self._nimbleStatus)
#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _activateWidgetDisplayImpl
    def _activateWidgetDisplayImpl(self, **kwargs):
        if self._firstView:
            self._nimbleStatus.refresh()
            self._firstView = False

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleAssignment1
    def _handleAssignment4(self):
        self.mainWindow.setActiveWidget('assignment4')

#___________________________________________________________________________________________________ _handleAssignment2
    #def _handleAssignment2(self):
        #self.mainWindow.setActiveWidget('assignment2')

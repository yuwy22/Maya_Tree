__author__ = 'Peipei'


# MayaPyMainWindow.py
# (C)2013
# Scott Ernst

from PySide import QtGui

from pyglass.windows.PyGlassWindow import PyGlassWindow

from mayaShaders.views.home.MayaShaderHomeWidget import MayaShaderHomeWidget
from mayaShaders.views.assignment4.Assignment4Widget import Assignment4Widget
#from mayaShaders.views.assignment2.Assignment2Widget import Assignment2Widget

#___________________________________________________________________________________________________ MayaPyMainWindow
class MayaShaderMainWindow(PyGlassWindow):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, **kwargs):
        PyGlassWindow.__init__(
            self,
            widgets={
                'home': MayaShaderHomeWidget,
                'assignment4':Assignment4Widget
                  },
            title='MayaShader',
            **kwargs )

        self.setMinimumSize(1024,480)
        self.setContentsMargins(0, 0, 0, 0)

        widget = self._createCentralWidget()
        layout = QtGui.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)


        self.setActiveWidget('home')

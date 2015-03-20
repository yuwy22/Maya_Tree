__author__ = 'Peipei'

from nimble import cmds
import os.path
#import maya.cmds as cmds

def gold_shader():
    #
    fn = os.path.join(os.path.dirname(__file__), 'gold1.ma')

    cmds.file(fn, o=True)
    cmds.file('/Users/Peipei/Documents/maya/projects/default/scenes/lego.ma', i=True)
    cmds.select(all=True)

    cmds.hyperShade(assign= 'gold')
    #cmds.sets(forceElement='gold'+'.SG')


gold_shader()

##
#Def handleSelectBtn(self)
#If self.selectionMethod1CmbxcurrentText()==self.FETCH_TRACK_BY_NAME:
    #Self.handleFetchByName()
#elseif self.selectionMethod1Cmbx.currentText() ==self.FETCH_TRACK_BY_INDEX:
    #self.handleFetchByIndex()


#http://furryball.aaa-studio.eu/files/furryBallNukeScripts.py

#####
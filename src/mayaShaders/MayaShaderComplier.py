__author__ = 'Peipei'

# MayaPyCompiler.py
# (C)2013
# Scott Ernst

from pyglass.compile.PyGlassApplicationCompiler import PyGlassApplicationCompiler
from pyglass.compile.SiteLibraryEnum import SiteLibraryEnum

from mayaShaders.MayaShaderApplication import MayaShaderApplication

#___________________________________________________________________________________________________ MayaPyCompiler
class MayaShaderCompiler(PyGlassApplicationCompiler):
    """A class for..."""

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: siteLibraries
    @property
    def siteLibraries(self):
        return [SiteLibraryEnum.PYSIDE]

#___________________________________________________________________________________________________ GS: binPath
    @property
    def binPath(self):
        return ['..', '..', 'bin']

#___________________________________________________________________________________________________ GS: appFilename
    @property
    def appFilename(self):
        return 'MayaShader'

#___________________________________________________________________________________________________ GS: appDisplayName
    @property
    def appDisplayName(self):
        return 'MayaShader'

#___________________________________________________________________________________________________ GS: applicationClass
    @property
    def applicationClass(self):
        return MayaShaderApplication

#___________________________________________________________________________________________________ GS: iconPath
    @property
    def iconPath(self):
        return ['apps', 'MayaShader']

####################################################################################################
####################################################################################################

if __name__ == '__main__':
    MayaShaderCompiler().run()


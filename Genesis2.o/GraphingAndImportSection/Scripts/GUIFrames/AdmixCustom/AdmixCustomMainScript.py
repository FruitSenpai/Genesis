import wx
#import the newly created GUI file
from GUIFrames.AdmixCustom.AdmixCustomMain import AdmixMainMenu as mainMenu
from GUIFrames.AdmixCustom.AdmixAncestryCustomScript import AdmixAncestryCustom as Ancestry
from GUIFrames.AdmixCustom.AdmixGroupCustomScript import AdmixGroupCustom as Group

class AdmixMainMenu(mainMenu):
    '''
    This contains the scripts to run the main admix customisation menu.
    '''

    def __init__(self,parent):
        mainMenu.__init__(self,parent)
        self.TestParent = parent

    def LoadAncestryOptions(self,event):
        ''' Loads ancestry options.'''
        print("Load Ancestry")
        self.child = Ancestry(self.Parent)
        self.child.Show()
        self.Destroy()
        pass

    def LoadGroupOptions( self, event ):
        ''' Loads group options.'''
        print("Load Group")
        self.child = Group(self.Parent)
        self.child.Show()
        self.Destroy()
        pass



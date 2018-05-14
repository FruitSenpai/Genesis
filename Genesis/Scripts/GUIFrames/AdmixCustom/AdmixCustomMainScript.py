import wx
#import the newly created GUI file
from GUIFrames.AdmixCustom.AdmixCustomMain import AdmixMainMenu as mainMenu
from GUIFrames.AdmixCustom.AdmixAncestryCustomScript import AdmixAncestryCustom as AncestryCust
from GUIFrames.AdmixCustom.AdmixGroupCustomScript import AdmixGroupCustom as GroupCust

class AdmixMainMenu(mainMenu):
     '''
     This contains the scripts to run the main admix customisation menu.
     '''

     def __init__(self,parent, graph, plotNB, innerNB):
          mainMenu.__init__(self,parent)
          self.TestParent = parent

          self.graph = graph
          self.plotNB = plotNB
          self.innerNB = innerNB

     def LoadAncestryOptions(self,event):
        ''' Loads ancestry options.'''
        print("Load Ancestry")
        self.child = AncestryCust(self.Parent, self.graph, self.plotNB, self.innerNB)
        self.child.Show()
        self.Destroy()
        pass

     def LoadGroupOptions( self, event ):
        ''' Loads group options.'''
        print("Load Group")
        self.child = GroupCust(self.Parent, self.graph, self.plotNB, self.innerNB)
        self.child.Show()
        self.Destroy()
        pass



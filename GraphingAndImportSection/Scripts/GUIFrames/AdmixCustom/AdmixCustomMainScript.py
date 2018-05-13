import wx
#import the newly created GUI file
from GUIFrames.AdmixCustom.AdmixCustomMain import AdmixMainMenu as mainMenu
from GUIFrames.AdmixCustom.AdmixAncestryCustomScript import AdmixAncestryCustom as AncestryCust
from GUIFrames.AdmixCustom.AdmixGroupCustomScript import AdmixGroupCustom as GroupCust

class AdmixMainMenu(mainMenu):
    """Used to respond to events on the Main Admix Customization GUI."""

    def __init__(self,parent, graph, plotNB, innerNB):
        """Initializes an AdmixMainMenu object along with its properties."""
        mainMenu.__init__(self,parent)
        self.TestParent = parent

        self.graph = graph
        self.plotNB = plotNB
        self.innerNB = innerNB

    def LoadAncestryOptions(self,event):
        """Loads the Admix Ancestry Customization GUI"""
        print("Load Ancestry")
        self.child = AncestryCust(self.Parent, self.graph, self.plotNB, self.innerNB)
        self.child.Show()
        self.Destroy()
        pass

    def LoadGroupOptions( self, event ):
        """Loads the Admix Group Customization GUI"""
        print("Load Group")
        self.child = GroupCust(self.Parent, self.graph, self.plotNB, self.innerNB)
        self.child.Show()
        self.Destroy()
        pass



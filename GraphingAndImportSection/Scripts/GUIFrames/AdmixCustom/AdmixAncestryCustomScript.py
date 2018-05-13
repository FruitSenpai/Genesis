import wx
#import the newly created GUI file
from GUIFrames.AdmixCustom.AdmixAncestryCustomFrame import AdmixAncestryCustom as Ancestry

class AdmixAncestryCustom(Ancestry):

    def __init__(self,parent):
        Ancestry.__init__(self,parent)

#FIllColours runs when the frame is created:It should filll the combo box with a list of assigned colours
#Look at the PCACustom Script to see how it is done
    def FillColours( self, event ):
	    event.Skip()
	
    def PrevAncestry( self, event ):
	    event.Skip()
	
    def NextAncestry( self, event ):
	    event.Skip()
	
    def ShiftAncestryLeft( self, event ):
	    event.Skip()
	
    def ShiftAncestryRight( self, event ):
	    event.Skip()
	
    def SetColour( self, event ):
	    event.Skip()
	
    def SortByAncestryDominance( self, event ):
	    event.Skip()
	
    def ChangeSortDirection( self, event ):
	    event.Skip()



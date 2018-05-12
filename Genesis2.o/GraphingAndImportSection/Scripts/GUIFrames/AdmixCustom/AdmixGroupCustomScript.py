import wx
#import the newly created GUI file
from GUIFrames.AdmixCustom.AdmixGroupCustomFrame import GroupFrame as Group

class AdmixGroupCustom(Group):

    def __init__(self,parent):
        Group.__init__(self,parent)

    def PrevGroup( self, event ):
	    event.Skip()
	
    def NextGroup( self, event ):
	    event.Skip()
	
    def ShiftGroupLeft( self, event ):
	    event.Skip()
	
    def ShiftGroupRight( self, event ):
	    event.Skip()
	
    def sortByAncestryDominance( self, event ):
	    event.Skip()
	
    def ChangeSortDirection( self, event ):
	    event.Skip()



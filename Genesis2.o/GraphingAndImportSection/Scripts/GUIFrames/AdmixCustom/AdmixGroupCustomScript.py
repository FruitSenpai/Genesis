import wx
#import the newly created GUI file
from GUIFrames.AdmixCustom.AdmixGroupCustomFrame import GroupFrame as Group

class AdmixGroupCustom(Group):

    '''
    This contains the code to run the Admix Custom Group.
    '''

    def __init__(self,parent):
        Group.__init__(self,parent)

    def PrevGroup( self, event ):
        '''Select previous group.'''
	    event.Skip()
	
    def NextGroup( self, event ):
        '''Select next group'''
	    event.Skip()
	
    def ShiftGroupLeft( self, event ):
        '''Shift group left.'''
    	    event.Skip()
	
    def ShiftGroupRight( self, event ):
        '''Shift group right.'''
	    event.Skip()
	
    def sortByAncestryDominance( self, event ):
        '''Sorts by ancestry dominance.'''
	    event.Skip()
	
    def ChangeSortDirection( self, event ):
        '''changes direction of sort.'''
	    event.Skip()



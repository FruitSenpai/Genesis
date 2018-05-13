import wx
#import the newly created GUI file
from GUIFrames.AdmixCustom.AdmixAncestryCustomFrame import AdmixAncestryCustom as Ancestry

class AdmixAncestryCustom(Ancestry):
    '''
    This contains the code to run the Admix Ancestory Customisation.
    '''
    def __init__(self,parent):
        Ancestry.__init__(self,parent)

#FIllColours runs when the frame is created:It should filll the combo box with a list of assigned colours
#Look at the PCACustom Script to see how it is done
    def FillColours( self, event ):
        '''Fills the combobox with a list of assigned colours. '''
	    event.Skip()
	
    def PrevAncestry( self, event ):
        '''Goes to previous ancestry.'''
	    event.Skip()
	
    def NextAncestry( self, event ):
        '''Goes to next ancestry.'''
	    event.Skip()
	
    def ShiftAncestryLeft( self, event ):
        '''Shift ancestry to the left.'''
	    event.Skip()
	
    def ShiftAncestryRight( self, event ):
        '''Shift ancestry to the right.'''
	    event.Skip()
	
    def SetColour( self, event ):
        '''Set the custom colour.'''
	    event.Skip()
	
    def SortByAncestryDominance( self, event ):
        '''Sort ancestry by dominance.'''
	    event.Skip()
	
    def ChangeSortDirection( self, event ):
        '''Change direction of sort.'''
	    event.Skip()



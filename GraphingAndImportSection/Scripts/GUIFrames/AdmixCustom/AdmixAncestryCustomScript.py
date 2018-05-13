import wx
#import the newly created GUI file
from GUIFrames.AdmixCustom.AdmixAncestryCustomFrame import AdmixAncestryCustom as AncestryFrame
from GUIFrames import DataHolder
from Graph.admix.AdmixGraph import AdmixGraph

class AdmixAncestryCustom(AncestryFrame):
    """Used to receive and respond to events from the Admix Ancestry Customization GUI."""
    def __init__(self,parent, graph, plotNB, innerNB):
        """Initializes an AdmixAncestryCustom object along with its properties."""
        AncestryFrame.__init__(self,parent)
        
        self.graph = graph
        self.plotNB = plotNB
        self.innerNB = innerNB

        self.numAncestries = len(graph.individualList[0].admixData)
        self.tracker = 0
        self.SetAncestryText()
        self.SetOrderText()

        self.Colour_ComboBox.Clear()
        for colour in AdmixGraph.colourList:
            self.Colour_ComboBox.Append(colour)

        self.SetSelectedColour()
        

#FIllColours runs when the frame is created:It should filll the combo box with a list of assigned colours
#Look at the PCACustom Script to see how it is done
    def FillColours( self, event ):
	    event.Skip()
	
    def PrevAncestry( self, event ):
            """Selects the previous ancestry in the ancestry list."""
            self.ChangeTracker(-1)
            self.SetAncestryText()
            self.SetOrderText()
            self.SetSelectedColour()
            event.Skip()
	
    def NextAncestry( self, event ):
            """Selects the next ancestry in the ancestry list."""
            self.ChangeTracker(1)
            self.SetAncestryText()
            self.SetOrderText()
            self.SetSelectedColour()
            event.Skip()
	
    def ShiftAncestryDown( self, event ):
            """Shifts the currently selected ancestry down."""
            if self.graph.shiftAncestryDown(self.tracker):
                self.ChangeTracker(-1)
            self.SetOrderText()
            self.SetSelectedColour()
            self.ReplotGraph()
            event.Skip()
	
    def ShiftAncestryUp( self, event ):
            """Shifts the currently selected ancestry up."""
            if self.graph.shiftAncestryUp(self.tracker):
                self.ChangeTracker(1)
            self.SetOrderText()
            self.SetSelectedColour()
            self.ReplotGraph()
            event.Skip()
	
    def SetColour( self, event ):
            """Set the colour of the currently selected ancestry."""
            colour = self.Colour_ComboBox.GetStringSelection()
            self.graph.ancestryList[self.tracker].colour = colour
            self.ReplotGraph()
            event.Skip()
	
    def SortByAncestryDominance( self, event ):
            """Sorts the ancestries in order of their dominances."""
            mostToLeast = self.Dom_CheckBox.GetValue()
            self.graph.sortByAncestryDominanceV2(mostToLeast)
            self.tracker = 0
            self.SetAncestryText()
            self.SetOrderText()
            self.SetSelectedColour()
            self.ReplotGraph()
            event.Skip()
	
    def ChangeSortDirection( self, event ):
	    event.Skip()

    def ChangeTracker(self, increment):
        """Increment the tracking variable by the specified increment amount."""
        self.tracker += increment
        if self.tracker >= self.numAncestries:
            self.tracker = 0

    def SetAncestryText(self):
        """Set the text of the ancestry name component to the name of the currently selected ancestry."""
        self.Anc_textCtrl.SetValue(self.graph.ancestryList[self.tracker].name)

    def SetOrderText(self):
        """Set the text of the ancestry order component to the order of the currently selected ancestry."""
        order = self.graph.ancestryList[self.tracker].orderInGraph
        self.Order_textCtrl.SetValue(str(order))

    def SetSelectedColour(self):
        """Set the colour of the ancestry colour component to the colour of the currently selected ancestry."""
        index = self.Colour_ComboBox.FindString(self.graph.ancestryList[self.tracker].colour)
        self.Colour_ComboBox.SetSelection(index)
 
    def ReplotGraph(self):
        """Deletes current figure and replots the graph."""
        index = self.innerNB.GetSelection()
        
        phenoCol = self.graph.getPhenoColumn()
        self.graph.plotGraph(False, phenoCol = phenoCol)

        self.innerNB.DeletePage(index)
            
        



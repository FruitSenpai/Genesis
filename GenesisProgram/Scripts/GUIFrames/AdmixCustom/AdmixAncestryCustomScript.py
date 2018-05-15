import wx
#import the newly created GUI file
from GUIFrames.AdmixCustom.AdmixAncestryCustomFrame import AdmixAncestryCustom as AncestryFrame
from GUIFrames import DataHolder
from Graph.admix.AdmixGraph import AdmixGraph

class AdmixAncestryCustom(AncestryFrame):
      '''
      This contains the code to run the Admix Ancestory Customisation.
      '''

      def __init__(self,parent, graph, plotNB, innerNB):
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
      def FillColours( self, event ):
            '''Fills the combobox with a list of assigned colours. '''
            event.Skip()
      
      def PrevAncestry( self, event ):
            '''Goes to previous ancestry.'''
            self.ChangeTracker(-1)
            self.SetAncestryText()
            self.SetOrderText()
            self.SetSelectedColour()
            event.Skip()
      
      def NextAncestry( self, event ):
            '''Goes to next ancestry.'''
            self.ChangeTracker(1)
            self.SetAncestryText()
            self.SetOrderText()
            self.SetSelectedColour()
            event.Skip()
      
      def ShiftAncestryDown( self, event ):
            '''Shift ancestry to the bottom.'''
            if self.graph.shiftAncestryDown(self.tracker):
                self.ChangeTracker(-1)
            self.SetOrderText()
            self.SetSelectedColour()
            self.ReplotGraph()
            event.Skip()
      
      def ShiftAncestryUp( self, event ):
            '''Shift ancestry above.'''
            if self.graph.shiftAncestryUp(self.tracker):
                self.ChangeTracker(1)
            self.SetOrderText()
            self.SetSelectedColour()
            self.ReplotGraph()
            event.Skip()
      
      def SetColour( self, event ):
            '''Set the custom colour.'''
            colour = self.Colour_ComboBox.GetStringSelection()
            self.graph.ancestryList[self.tracker].colour = colour
            self.ReplotGraph()
            event.Skip()
      
      def SortByAncestryDominance( self, event ):
            '''Sort ancestry by dominance.'''
            mostToLeast = self.Dom_CheckBox.GetValue()
            self.graph.sortByAncestryDominanceV2(mostToLeast)
            self.tracker = 0
            self.SetAncestryText()
            self.SetOrderText()
            self.SetSelectedColour()
            self.ReplotGraph()
            event.Skip()
      
      def ChangeSortDirection( self, event ):
            '''Change direction of sort.'''
            event.Skip()

      def ChangeTracker(self, increment):
        '''Changes tracker.'''
        self.tracker += increment
        if self.tracker >= self.numAncestries:
            self.tracker = 0

      def SetAncestryText(self):
        '''Sets ancestry.'''
        self.Anc_textCtrl.SetValue(self.graph.ancestryList[self.tracker].name)

      def SetOrderText(self):
        '''Sets order text.'''
        order = self.graph.ancestryList[self.tracker].orderInGraph
        self.Order_textCtrl.SetValue(str(order))

      def SetSelectedColour(self):
        '''Sets selected colour.'''
        index = self.Colour_ComboBox.FindString(self.graph.ancestryList[self.tracker].colour)
        self.Colour_ComboBox.SetSelection(index)
 
      def ReplotGraph(self):
        '''Replots graph.'''
        index = self.innerNB.GetSelection()
        
        phenoCol = self.graph.getPhenoColumn()
        self.graph.plotGraph(False, phenoCol = phenoCol)

        self.innerNB.DeletePage(index)

            
        



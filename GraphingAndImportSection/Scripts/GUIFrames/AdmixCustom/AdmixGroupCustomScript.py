import wx
#import the newly created GUI file
from GUIFrames.AdmixCustom.AdmixGroupCustomFrame import GroupFrame as Group

class AdmixGroupCustom(Group):
    """Used to receive and respond to events from the Admix Group Customization GUI."""
    def __init__(self,parent, graph, plotNB, innerNB):
        """Initializes an AdmixGroupCustom object along with its properties."""
        Group.__init__(self,parent)

        self.graph = graph
        self.plotNB = plotNB
        self.innerNB = innerNB

        self.colIndex = graph.groupColIndex
        self.numGroups = len(graph.admixGroupList[self.colIndex])
        self.tracker = 0

        self.SetGroupText()
        self.SetOrderText()
        self.SetHiddenCheck()

    def PrevGroup( self, event ):
            """Selects the previous group in the group list."""
            self.ChangeTracker(-1)
            self.SetGroupText()
            self.SetOrderText()
            self.SetHiddenCheck()
            event.Skip()
	
    def NextGroup( self, event ):
            """Selects the next group in the group list."""
            self.ChangeTracker(1)
            self.SetGroupText()
            self.SetOrderText()
            self.SetHiddenCheck()
            event.Skip()
	
    def ShiftGroupLeft( self, event ):
            """Shifts the currently selected group to the left."""
            if self.graph.shiftGroupDown(self.tracker):
                self.ChangeTracker(-1)
            self.SetOrderText()
            self.ReplotGraph()
            event.Skip()
	
    def ShiftGroupRight( self, event ):
            """Shifts the currently selected group to the right."""
            if self.graph.shiftGroupUp(self.tracker):
                self.ChangeTracker(1)
            self.SetOrderText()
            self.ReplotGraph()
            event.Skip()
	
    def sortByGroupDominance( self, event ):
            """Sorts the groups in order of their dominance(population)."""
            mostToLeast = self.CheckBox_Group.GetValue()
            self.graph.sortByGroupDominanceV2(mostToLeast)
            self.tracker = 0
            self.SetGroupText()
            self.SetOrderText()
            self.SetHiddenCheck()
            self.ReplotGraph()
            event.Skip()
	
    def ChangeSortDirection( self, event ):
	    event.Skip()

    def HideGroup(self, event):
            """Hide the currently selected group."""
            hide = self.CheckBox_Hide.GetValue()
            print(hide)
            self.graph.setGroupHidden(self.tracker, hide)
            self.ReplotGraph()
            event.Skip()

    def ChangeTracker(self, increment):
        """Increment the tracking variable by the specified increment amount."""
        self.tracker += increment
        if self.tracker >= self.numGroups:
            self.tracker = 0
        elif self.tracker < 0:
            self.tracker = self.numGroups - 1

    def SetGroupText(self):
        """Set the text of the group text component to the name of the currently selected group."""
        groupName = self.graph.admixGroupList[self.colIndex][self.tracker].name
        self.Group_textCtrl.SetValue(groupName)

    def SetOrderText(self):
        """Set the text of the group order component to the order of the currently selected group."""
        order = self.graph.admixGroupList[self.colIndex][self.tracker].orderInGraph
        self.Order_textCtrl1.SetValue(str(order))

    def SetHiddenCheck(self):
        """Set the value of the group hidden checkbox to the the currently selected group's hidden status."""
        value = self.graph.admixGroupList[self.colIndex][self.tracker].hidden
        self.CheckBox_Hide.SetValue(value)

    def ReplotGraph(self):
        """Deletes current figure and replots the graph."""
        index = self.innerNB.GetSelection()
        
        phenoCol = self.graph.getPhenoColumn()
        self.graph.plotGraph(False, phenoCol = phenoCol)

        self.innerNB.DeletePage(index)
        



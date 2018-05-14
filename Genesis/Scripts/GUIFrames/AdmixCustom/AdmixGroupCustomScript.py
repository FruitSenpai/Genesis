import wx
#import the newly created GUI file
from GUIFrames.AdmixCustom.AdmixGroupCustomFrame import GroupFrame as Group

class AdmixGroupCustom(Group):

    def __init__(self,parent, graph, plotNB, innerNB):
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
            self.ChangeTracker(-1)
            self.SetGroupText()
            self.SetOrderText()
            self.SetHiddenCheck()
            event.Skip()
	
    def NextGroup( self, event ):
            self.ChangeTracker(1)
            self.SetGroupText()
            self.SetOrderText()
            self.SetHiddenCheck()
            event.Skip()
	
    def ShiftGroupLeft( self, event ):
            if self.graph.shiftGroupDown(self.tracker):
                self.ChangeTracker(-1)
            self.SetOrderText()
            self.ReplotGraph()
            event.Skip()
	
    def ShiftGroupRight( self, event ):
            if self.graph.shiftGroupUp(self.tracker):
                self.ChangeTracker(1)
            self.SetOrderText()
            self.ReplotGraph()
            event.Skip()
	
    def sortByGroupDominance( self, event ):
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
            hide = self.CheckBox_Hide.GetValue()
            print(hide)
            self.graph.setGroupHidden(self.tracker, hide)
            self.ReplotGraph()
            event.Skip()

    def ChangeTracker(self, increment):
        self.tracker += increment
        if self.tracker >= self.numGroups:
            self.tracker = 0
        elif self.tracker < 0:
            self.tracker = self.numGroups - 1

    def SetGroupText(self):
        groupName = self.graph.admixGroupList[self.colIndex][self.tracker].name
        self.Group_textCtrl.SetValue(groupName)

    def SetOrderText(self):
        order = self.graph.admixGroupList[self.colIndex][self.tracker].orderInGraph
        self.Order_textCtrl1.SetValue(str(order))

    def SetHiddenCheck(self):
        value = self.graph.admixGroupList[self.colIndex][self.tracker].hidden
        self.CheckBox_Hide.SetValue(value)

    def ReplotGraph(self):
        index = self.innerNB.GetSelection()
        
        phenoCol = self.graph.getPhenoColumn()
        self.graph.plotGraph(False, phenoCol = phenoCol)

        self.innerNB.DeletePage(index)
        



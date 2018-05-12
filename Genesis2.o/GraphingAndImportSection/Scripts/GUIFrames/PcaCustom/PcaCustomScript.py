import wx
#import the newly created GUI file
from GUIFrames.PcaCustom.PcaCustomFrame import MyFrame2 as cusClass
from GUIFrames import DataHolder

class PcaCustom(cusClass):

    def __init__(self,parent,CurrText,currPage,nb,index):
        cusClass.__init__(self,parent)
        self.Text =CurrText;
        self.Graph = DataHolder.Graphs.get(self.Text)
        self.currPage = currPage
        self.index = index
        self.nb = nb
        if( hasattr( self.Graph,"_GroupClasses")):
            self.Group = self.Graph._GroupClasses[0].GetName()
            wordList = self.Graph._GroupClasses[0].GetColour().split(":")
            self.Colour = wordList[1]
            self.Marker = self.Graph._GroupClasses[0].GetMarker()
        else:
            self.Destroy()
            
        

    def FillBoxes(self,event):
        if( hasattr( self.Graph,"_GroupClasses")):
            GroupList = []
            ColourList = ['blue','purple','green','yellow','red','brown','orange','cyan']
            MarkerList = ['o','^','v','p','*','s','P','8','X']
            #self.Graph = DataHolder.Graphs.get(self.Figure)

            self.GroupCombo.Clear()
            self.ColourCombo.Clear()
            self.MarkerCombo.Clear()
            
            GroupList = self.Graph._GroupClasses
            print(len(GroupList))
            GroupComboChoices =[]
            for i in GroupList:            
                #GroupComboChoices.append(i.GetName)
                self.GroupCombo.Append(i.GetName())
            self.GroupCombo.Value = GroupList[0].GetName()
            
            for i in range(0,len( ColourList)):            
                #GroupComboChoices.append(i.GetName)
                self.ColourCombo.Append(ColourList[i])
            wordList = GroupList[0].GetColour().split(":")
            self.ColourCombo.Value = wordList[1]

            for i in range(0, len( MarkerList)):            
                #GroupComboChoices.append(i.GetName)
                self.MarkerCombo.Append(MarkerList[i])
            self.MarkerCombo.Value = GroupList[0].GetMarker()
        else:
            self.Destroy()

    def onExit(self,event):
        self.Destroy()

    def SetGroup(self,event):
        self.Group =  self.GroupCombo.Value
        print(self.Group)

    def SetColour(self,event):
        self.Colour =  self.ColourCombo.Value
        print(self.Colour)

    def SetMarker(self,event):
        self.Marker =  self.MarkerCombo.Value
        print(self.Marker)

    def onAccept( self, event ):
        GroupList =[]
        for i in range(0,len(self.Graph._GroupClasses)):
            GroupList.append(self.Graph._GroupClasses[i])
            
        testBoolean = False
        counter = 0
        max = len(GroupList)
        while (testBoolean is False):
            print(str(counter) + " " +GroupList[counter].GetName()+" "+self.Group)
            if(GroupList[counter].GetName() == self.Group):
                testBoolean = True
                break

            else:
                counter +=1
                if(counter>= max):
                    break

        print(self.Colour)
        print(self.Marker)
        
        GroupList[counter].SetColour(self.Colour) 
        GroupList[counter].SetMarker(self.Marker)  
        print(GroupList[counter].GetName() + " " +GroupList[counter].GetColour()+" "+GroupList[counter].GetMarker())
        del self.Graph._GroupClasses[counter]
        
        self.Graph._GroupClasses.insert(counter,GroupList[counter])
        print(str(counter))
        print(GroupList[counter].GetName() + " " +GroupList[counter].GetColour()+" "+GroupList[counter].GetMarker())
        print(self.Graph._GroupClasses[counter].GetName() + " " +self.Graph._GroupClasses[counter].GetColour()+" "+self.Graph._GroupClasses[counter].GetMarker())
        
        self.Graph.PlotPca(False)
        self.nb.DeletePage(self.index)
        self.Destroy()

        




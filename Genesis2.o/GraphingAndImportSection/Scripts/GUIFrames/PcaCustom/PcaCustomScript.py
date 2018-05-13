import wx
#import the newly created GUI file
from GUIFrames.PcaCustom.PcaCustomFrame import MyFrame2 as cusClass
from Graph.PcaGraphing.PcaGraph import PcaGraph as PCA
from GUIFrames import DataHolder

class PcaCustom(cusClass):
    '''
    The is the class that contains code to run the Pca custom frame.
    '''

    def __init__(self,parent,CurrText,currPage,nb,index):
        cusClass.__init__(self,parent)
        #Name of currently selected figure
        self.Text =CurrText;
        #Current graph
        self.Graph = DataHolder.Graphs.get(self.Text)
        #currPage
        self.currPage = currPage
        #index for removing
        self.index = index
        #reference to notebook
        self.nb = nb
        #Checks if it is a PcaGraph
        self.Group = self.Graph._GroupClasses[0].GetName()
        wordList = self.Graph._GroupClasses[0].GetColour().split(":")
        self.Colour = wordList[1]
        self.Marker = self.Graph._GroupClasses[0].GetMarker()
        self._BoxSize = str(self.Graph._GroupClasses[0].GetSize())

            
        
    #fills combo boxes when frame is created
    def FillBoxes(self,event):
        '''Fills comboboxes with customisation options'''
        
        GroupList = []
        ColourList = ['blue','purple','green','yellow','red','brown','orange','cyan']
        MarkerList = ['o','^','v','p','*','s','P','8','X']
        #self.Graph = DataHolder.Graphs.get(self.Figure)

        self.GroupCombo.Clear()
        self.ColourCombo.Clear()
        self.MarkerCombo.Clear()
        self.SizeBox.Value = ""
            
            
        GroupList = self.Graph._GroupClasses
        print(len(GroupList))
        GroupComboChoices =[]
        for i in GroupList:            
            self.GroupCombo.Append(i.GetName())
        self.GroupCombo.Value = GroupList[0].GetName()
            
        for i in range(0,len( ColourList)):            
            self.ColourCombo.Append(ColourList[i])
        wordList = GroupList[0].GetColour().split(":")
        self.ColourCombo.Value = wordList[1]

        for i in range(0, len( MarkerList)):            
            self.MarkerCombo.Append(MarkerList[i])
        self.MarkerCombo.Value = GroupList[0].GetMarker()

        self.SizeBox.Value = str(GroupList[0].GetSize())


    def onExit(self,event):
        '''Exit frame.'''
        self.Destroy()

    def SetGroup(self,event):
        '''Sets group.'''
        self.Group =  self.GroupCombo.Value
        print(self.Group)

    def SetColour(self,event):
         '''Sets colour.'''
        self.Colour =  self.ColourCombo.Value
        print(self.Colour)

    def SetMarker(self,event):
        self.Marker =  self.MarkerCombo.Value
        print(self.Marker)

    def SetSize(self,event):
        if(int(self.SizeBox.Value)>10 and int(self.SizeBox.Value)<=300):
            self._BoxSize = self.SizeBox.Value
        else:
            self.SizeBox.Value= self._BoxSize
        

#Finds correct group, changes the group class amd replots
    def onAccept( self, event ):
         '''
        Accepts input data.

        Finds the correct group , changes rhe group class and replots.
        '''
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
        print(self._BoxSize)
        
        GroupList[counter].SetColour(self.Colour) 
        GroupList[counter].SetMarker(self.Marker)
        GroupList[counter].SetSize(int(self._BoxSize)) 
        print(GroupList[counter].GetName() + " " +GroupList[counter].GetColour()+" "+GroupList[counter].GetMarker())
        del self.Graph._GroupClasses[counter]
        
        self.Graph._GroupClasses.insert(counter,GroupList[counter])
        print(str(counter))
        print(GroupList[counter].GetName() + " " +GroupList[counter].GetColour()+" "+GroupList[counter].GetMarker())
        print(self.Graph._GroupClasses[counter].GetName() + " " +self.Graph._GroupClasses[counter].GetColour()+" "+self.Graph._GroupClasses[counter].GetMarker())
        
        test =self.Graph.PlotPca(False)
        print(test)
        self.nb.DeletePage(self.index)
        #self.Destroy()

        




"""Creates an object that stores all the data needed to make a graph."""
import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import interactive
import random as rnd
import os
from wx.lib.pubsub import pub
from GUIFrames import DataHolder

from Graph.PcaGraphing.PcaGroup import PcaGroup 


class PcaGraph():
    """Creates an object that stores all the data needed to make a graph."""
    
    
    def __init__(self,NamesFirst,Groups,dictPhen,_Data,_xCol,_yCol,GraphName,panel):
        ##define variables to use later on for plotting the graph
        self.Names = NamesFirst
        self.GroupData =Groups
        self.PhenDict =dictPhen
        self.Data = _Data
        self.xCol =_xCol
        self.yCol =_yCol
        self._nb = panel
        self._Name = GraphName
        #self._DH = DataHolder
        self._GroupClasses = []
        
        self._Counter = 0

    def setNotebook(self, notebook):
        """Sets current notebook panel on which the graph can be plotted."""
        self._nb = notebook

    def getName(self):
        """Returns the name assigned to the graph."""
        return self._Name

    def setName(self, newName, oldName):
        """Sets graphs name.

        Replaces old name with new one. Replaces old graph with this new one in the DataHolder script."""
        self._Name = newName

        #get rid of obsolete dictionary keys
        figure = DataHolder.Figures.pop(oldName) #generates KeyError if not found
        graph = DataHolder.Graphs.pop(oldName)

        DataHolder.Graphs.update({newName:self})
        DataHolder.Figures.update({newName:figure})
        
    ##NOTE if you are re-rendering the graph with a save file then please set FIrstTIMe to False, if its first time then set it to True
    def PlotPca(self,FirstTime):
        """Plots Pca onto the notebook."""

        #variable for unittesting
        success= False
        
        #exception handling for making sure the graph wont crash if no data is entered
        try:
            if(self.Data == None):
                raise TypeError("Found Type Error")
            count =_FindLength(self.Data)
        except TypeError:
            print("Found TypeError with Data")
            
            count = 0
       
        x =[]
        y=[]
        #start from one to avoid the first line
        for i in range(1,count):
            x.append( self.Data[i][self.xCol])
            y.append( self.Data[i][self.yCol])
        

        #create an new figure for this graph
        if(self._nb != None):
            self._fig = self._nb.add(self._Name)
            self._ax = self._fig.gca()
        else:
            self._fig,self._ax = plt.subplots()

        ##Checks each individual group
        ##Per group each indiviual is checked to see if it belongs to the group
        ##If this is the case then its x and y co-ords are added to the x and y lists to be plotted 
        try:
            if(len(self.GroupData) >0):
                for group in range(len(self.GroupData)):
                    xtemp =[]
                    ytemp= []
                    #Creates a random group for the first time the data is created
                    if(FirstTime is True):
                        _marker = RandomMarker(self._Counter)
                        _Colour = RandomColour(self._Counter)
                        _currGroup = PcaGroup(self.GroupData[group],Colour = _Colour, Marker=_marker)
                        
                    #Should pull the current GroupData if FirstTime == False    
                    else:
                        _currGroup =  self._GroupClasses[group]
                    
                    for i in range(len(self.Names)):
                        if(self.Names[i] in self.PhenDict):
                            if(self.PhenDict.get(self.Names[i]) == self.GroupData[group]):
                                #Add x and y values to a temp list
                                xtemp.append(float(x[i]))
                                ytemp.append(float(y[i]))
                                #Add an individual to the group class
                                
                                _currGroup.AddIndividual(self.Names[i],float(x[i]),float(y[i]))

                    ##A check to make sure that we dont plot groups with 0 components
                    if(len(xtemp) >0):
                        self._ax.scatter(xtemp, ytemp, marker=_currGroup.GetMarker(), label=self.GroupData[group], s=_currGroup.GetSize(),c= _currGroup.GetColour() )
                        #Counter is just used to make sure that data marker and colour will not repeat
                        self._Counter = self._Counter+1

                    if(FirstTime is True):
                        
                        self._GroupClasses.append(_currGroup)
                    


            ##In case there is no phen data
            else :
                #if(len(xtemp) >0):
                xtemp =[]
                ytemp= []

                for i in range(1,len(x)):
                    xtemp.append(float(x[i]))
                    ytemp.append(float(y[i]))
                
                self._ax.scatter(xtemp, ytemp, marker='^',label= "Test", s=20, color = 'xkcd:blue')
            success = True
            
        except TypeError:
            print("TypeError graphing")
            sucesss = False
            
        except IndexError:
            print("IndexError graphing")
            success = False
        
        #creates legend for groups
        self._ax.legend()
        #Sets title
        self._ax.set_title(self._Name)
        #Adds graph to data holder
        DataHolder.Figures.update({self._Name:self._fig})

        #
        return success
       
        



def _FindLength(Data):
    """ Check size of File(how many lines)."""
    count = len(Data)
    return count

def RandomMarker(num):
    """Returns a random marker."""
    
    _num = num
    _markerList = ['o','^','v','p','*','s','P','8','X']
    _listLen = len(_markerList)
    while(_num>_listLen):
        _num = _num-_listLen

    _marker = ''
    
    try:
        _marker = _markerList[_num-1]
    except IndexError:
        _marker = _markerList[0]
        print("Went Out Of Index - Marker")
        
    return _marker

def RandomColour(num):
    """Returns a random colour."""

    #Choosing an option from a list
    #its not random but will not repeat for at least 40 groups
    _num= num
    _ColourList =['blue','purple','green','yellow','red','brown','orange','cyan']
    _listLen = len(_ColourList)
    _colourCount = 0
    while(_num>_listLen):
        _num= _num -_listLen
        _colourCount = _colourCount+1

    _Colour = ''
    _index =_num-1 +  _colourCount
    if(_index >= _listLen):
        index = (index -_listLen)
    try:
        _Colour=_ColourList[_index]
    except IndexError:
        _Colour = _ColourList[0]
        print("Went Out OF index - Colour")

    return _Colour


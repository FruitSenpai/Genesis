import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import interactive
import random as rnd
import os
from wx.lib.pubsub import pub

class PcaGroup():

    def __init__(self,GroupName,Colour = None, Marker = None,s = None):

        self._Name = GroupName
        
        if(Colour is None):
            self._Colour = ''

        else:
            self._Colour = 'xkcd:'+Colour

        if(Marker is None):
            self._marker = ''
        else:
            self._marker = Marker
        if(s is None):
            self._Size = 20
        else:
            self._Size = s

        self._individuals = {}

    def SetColour(self,colour):
        self._Colour = 'xkcd:'+colour

    def SetMarker(self, marker):
        self._marker = marker
        
    #Sets a key in the dictionary(key is the individual name, value is a list)
    #list [0] =  xdata------list[1] = ydata
    def AddIndividual(self, Name,xData,yData):
        _tempList = []
        _tempList.append(xData)
        _tempList.append(yData)
        self._individuals.update({Name:_tempList})

    def SetName(self, Name):
        self._Name = Name

    def SetSize(self,Size):
        self._Size = Size
        
    #returns string
    def GetColour(self):
        return self._Colour
    #returns string
    def GetMarker(self):
        return self._marker
    #returns dictionary
    def ReturnIndividuals(self):
        return self._individuals
    #return string
    def GetName(self):
        return self._Name

    def GetSize(self):
        return self._Size



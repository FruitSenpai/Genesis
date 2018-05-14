"""Holds group data for a specific group."""
import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import interactive
import random as rnd
import os
from wx.lib.pubsub import pub

class PcaGroup():
    """Holds group data for a specific group."""

    def __init__(self,GroupName,Colour = None, Marker = None,s = None):

        #Defines name
        self._Name = GroupName

        #Defines marker colour
        if(Colour is None):
            self._Colour = ''

        else:
            #"xkcd" is used so that colours can be defined as strings as opposed to letters or hex values
            self._Colour = 'xkcd:'+Colour

        #Defines marker
        if(Marker is None):
            self._marker = ''
        else:
            self._marker = Marker
            
        #defines marker size
        if(s is None):
            self._Size = 20
        else:
            self._Size = s
            
        #defines individuals who belong to this group
        self._individuals = {}

        

    def SetColour(self,colour):
        """Sets group marker colour."""
        self._Colour = 'xkcd:'+colour

    def SetMarker(self, marker):
        """Sets group marker."""
        self._marker = marker
        
    def AddIndividual(self, Name,xData,yData):
        """ Creates a dictionary

        The dictionarys key is the indiviuals name and the value is a list of floats. The value is defined as 'list [0] =  xdata------list[1] = ydata'."""
        _tempList = []
        _tempList.append(xData)
        _tempList.append(yData)
        self._individuals.update({Name:_tempList})

    def SetName(self, Name):
        """ Sets groups name."""
        self._Name = Name

    def SetSize(self,Size):
        """Sets a groups size."""
        self._Size = Size
        
    #returns string
    def GetColour(self):
        """Gets a groups marker colour."""
        return self._Colour
    #returns string
    def GetMarker(self):
        """Gets a groups marker."""
        return self._marker
    #returns dictionary
    def ReturnIndividuals(self):
        """Returns the individuals of a group."""
        return self._individuals
    #return string
    def GetName(self):
        """Gets a groups name."""
        return self._Name
    #returns int
    def GetSize(self):
        """Gets a groups marker size"""
        return self._Size



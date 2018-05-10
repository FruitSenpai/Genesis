import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import interactive
import random as rnd
import os
from wx.lib.pubsub import pub
from GUIFrames import DataHolder



class PcaGraph():
    
    ##Plots all pca points in different Group
    def __init__(self,NamesFirst,Groups,dictPhen,_Data,_xCol,_yCol,panel):
        ##define variables to use later on for plotting the graph
        self.Names = NamesFirst
        self.GroupData =Groups
        self.PhenDict =dictPhen
        self.Data = _Data
        self.xCol =_xCol
        self.yCol =_yCol
        self._nb = panel

        self._DH = DataHolder
        
        
    
    def PlotPca(self):

         ##getting and creating variables
        count =_FindLength(self.Data)
       
        x =[]
        y=[]
        
        for i in range(1,count):
            x.append( self.Data[i][self.xCol])
            y.append( self.Data[i][self.yCol])
        


        ##Checks each individual group
        ##Per group each indiviual is checked to see if it belongs to the group
        ##If this is the case then its x and y co-ords are added to the x and y lists to be plotted 

        #create an new figure for this graph
        #fig, ax = plt.subplots()
        #replace 'figure1' with name
        self._fig = self._nb.add('figure1')
        self._ax = self._fig.gca()

        ##runs of there is phen data(Possibly using group data is not ideal)
        if(len(self.GroupData) >0):
            for group in range(len(self.GroupData)):
                xtemp =[]
                ytemp= []
                
                for i in range(len(self.Names)):
                    if(self.Names[i] in self.PhenDict):
                        if(self.PhenDict.get(self.Names[i]) == self.GroupData[group]):
                            ##add x and y value to dictionary
                            xtemp.append(float(x[i]))
                            ytemp.append(float(y[i]))      

            ##just a check to make sure that we dont plot groups with 0 components
                if(len(xtemp) >0):
                    self._ax.scatter(xtemp, ytemp, marker='^', label=self.GroupData[group], s=10 )


        ##In case there is no phen data
        else :
            #if(len(xtemp) >0):
            xtemp =[]
            ytemp= []

            for i in range(1,len(x)):
                xtemp.append(float(x[i]))
                ytemp.append(float(y[i]))
            
            self._ax.scatter(xtemp, ytemp, marker='^',label= "Test", s=10, color = 'xkcd:blue')

        
        
        self._ax.legend()
        self._DH.Figures.update({'TestPca':self._fig})
       # self.RenderGraph('Heading','x','y')
        
        



def _FindLength(Data):
##Checking size of file(how many lines)
    count = len(Data)
    return count



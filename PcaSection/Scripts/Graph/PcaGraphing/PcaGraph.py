import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import interactive
import random as rnd
import os


class PcaGraph():
    
    ##Plots all pca points in different Group
    def __init__(self,NamesFirst,Groups,dictPhen,_Data,_xCol,_yCol):
        self.Names = NamesFirst
        self.GroupData =Groups
        self.PhenDict =dictPhen
        self.Data = _Data
        self.xCol =_xCol
        self.yCol =_yCol
    
    
    def PlotPca(self):
        #EvecString = os.getcwd()
       # EvecString= EvecString+'\..\..\Data\comm-SYMCL.pca.evec'

        ##takes all x and y values that were specified (NOTE THIS IS WHERE THE COLOUMNS FOR THE EVEC FOLDER WOULD BE CHANGED)
       # x, y = np.genfromtxt(EvecString,unpack=True, usecols = (1,2),skip_header=1)
        
 
        count =_FindLength(self.Data)
       # print (count)
        x =[]
        y=[]
        for i in range(1,count):
            x.append( self.Data[i][self.xCol])
            y.append( self.Data[i][self.yCol])
           # 
        #print(FindLength(y))
       # for i in range(0,len(x)):
      #     print('['+x[i]+','+y[i]+']')

        ##Checks each individual group
        ##Per group each indiviual is checked to see if it belongs to the group
        ##If this is the case then its x and y co-ords are added to the x and y lists to be plotted 
        fig, ax = plt.subplots()
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
                ax.scatter(xtemp, ytemp, marker='^', label=self.GroupData[group], s=10)

            self.RenderGraph('Heading','x','y')
       
                
    ##renders graph in pyplot
    def RenderGraph(self,Heading,xLabel,yLabel):
        # Plots graph

        plt.title(Heading)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend()
        ##interactive(True)
      ##  plt.show()




def _FindLength(Data):
##Checking size of file(how many lines)
    count = len(Data)
    return count

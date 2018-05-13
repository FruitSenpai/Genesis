"""Creates the Graph objects and plots them."""
import sys
import os

from  Graph.PcaGraphing import PcaDataExtractor as PcaEx
from  Graph.PcaGraphing.PcaGraph import PcaGraph

from Graph.admix import AdmixDataExtractor as admixEx
from Graph.admix.AdmixGraph import AdmixGraph

from GUIFrames import DataHolder

##
def CreatePca(PhenData,EvecData,pcaCol1,pcaCol2,phenCol,Name,panel):
    """Creates a pca using data given to it by the file importer. """

    Groups = []
    Names = []
    phenDic = {}

    #Data extraction class extracts the data that is needed to create the graph
    #Returns extracted in data in either a list or dictionary
    if(PhenData != None):
        phenDic = PcaEx.FindPhenData(PhenData,phenCol-1,0)
        Groups = PcaEx.FindPhenGroups(PhenData,phenCol-1)
    try:
        Names = PcaEx.GetIndividuals(True,EvecData,0)
        count = len(Names)
    except TypeError:
        print("Type Error Graph Create")
        Names = None

    #Create graph object
    pcagraph =PcaGraph(Names,Groups,phenDic,EvecData,pcaCol1,pcaCol2,Name,panel)
    #Tell graph object to plot
    #Test var is used for unittesting purposes
    TestVar =pcagraph.PlotPca(True)
    #Save graph for current session
    DataHolder.Graphs.update({Name:pcagraph})
    return TestVar
    

def CreateAdmix(admixData,famData,pheData,PheCol,nb, name):
        """Creates an admix using data given to it by the file importer. """
        
        #Create a list that will store the admix data as a float as opposed to a string
        AdmixData = []
        
        #specifies which column to use for group information in phenotype file
        phenoColumn = PheCol

        #Turn admix data from a string list to a float list
        for i in range(0,len(admixData)):
            AdmixData.append([])
            for x in range(0,len(admixData[i])):
                AdmixData[i].append(float(admixData[i][x]))

        #create new Admix graph and plot it        
        admixGraph = AdmixGraph(AdmixData, famData,nb, name, phenoData= pheData)
        
        #plots graph dependant on if there is phen data
        if(pheData != None):
            admixGraph.plotGraph(True,phenoCol = phenoColumn)
        else:
            admixGraph.plotGraph(True,phenoCol = None)
        #Save graph for current session
        DataHolder.Graphs.update({name:admixGraph})



	


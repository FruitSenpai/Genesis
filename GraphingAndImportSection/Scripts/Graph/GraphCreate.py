import sys
import os

##path = os.getcwd()
##path = path+'\PcaGraphing'
##sys.path.insert(0, path)

from  Graph.PcaGraphing import PcaDataExtractor as PcaEx
from  Graph.PcaGraphing.PcaGraph import PcaGraph

from Graph.admix import AdmixDataExtractor as admixEx
from Graph.admix.AdmixGraph import AdmixGraph

from GUIFrames import DataHolder

##Creates a pca using data given to it by the file importer
##Admix to be made
def CreatePca(PhenData,EvecData,pcaCol1,pcaCol2,phenCol,Name,panel):

    Groups = []
    Names = []
    phenDic = {}

    #Data extraction class extracts the data that is needed to create the graph
    #####Need to fix names though
    if(PhenData != None):
        phenDic = PcaEx.FindPhenData(PhenData,phenCol-1,0)
        Groups = PcaEx.FindPhenGroups(PhenData,phenCol-1)
    try:
        Names = PcaEx.GetIndividuals(True,EvecData,0)
        count = len(Names)
    except TypeError:
        print("Type Error Graph Create")
        Names = None

##plotPca and RenderGraph should follow and might be enveloped into one 
    pcagraph =PcaGraph(Names,Groups,phenDic,EvecData,pcaCol1,pcaCol2,Name,panel)
    TestVar =pcagraph.PlotPca(True)
    DataHolder.Graphs.update({Name:pcagraph})
    return TestVar
    

def CreateAdmix(admixData,famData,pheData,PheCol,nb, name):
    
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
        

        if(pheData != None):
            admixGraph.plotGraph(True, phenoCol = phenoColumn)
        else:
            admixGraph.plotGraph(True, phenoCol = None)

        DataHolder.Graphs.update({name:admixGraph})



	


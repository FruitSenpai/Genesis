import sys
import os

##path = os.getcwd()
##path = path+'\PcaGraphing'
##sys.path.insert(0, path)

from  PcaGraphing import PcaDataExtractor as PcaEx
from  PcaGraphing.PcaGraph import PcaGraph

from admix import AdmixDataExtractor as admixEx
from admix.AdmixGraph import AdmixGraph
##Creates a pca using data given to it by the file importer
##Admix to be made
def CreatePca(PhenData,EvecData):

    Groups = []
    Names = []

    #Data extraction class extracts the data that is needed to create the graph
    #####Need to fix names though
    phenDic = PcaEx.FindPhenData(PhenData,2,0)

    Groups = PcaEx.FindPhenGroups(PhenData,2)
        
    Names = PcaEx.GetIndividuals(True,EvecData,0)
    count = len(Names)

##plotPca and RenderGraph should follow and might be enveloped into one 
    pcagraph =PcaGraph(Names,Groups,phenDic,EvecData,1,2)
    pcagraph.PlotPca()
    

def CreateAdmix(admixData,famData,pheData):
	
	#Create a list that will store the admix data as a float as opposed to a string
	AdmixData = []
	
	#specifies which column to use for group information in phenotype file
	phenoColumn = 5

        #Turn admix data from a string list to a float list
	for i in range(0,len(admixData)):
            AdmixData.append([])
            for x in range(0,len(admixData[i])):
                AdmixData[i].append(float(admixData[i][x]))

        #create new Admix graph and plot it        
	admixGraph = AdmixGraph(AdmixData, famData, phenoData= pheData)
	admixGraph.plotGraph(phenoCol = phenoColumn)



	


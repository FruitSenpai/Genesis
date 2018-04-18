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

    phenData = {}
    Groups = []
    Names = []

    phenDic = PcaEx.FindPhenData(PhenData,2,0)

    Groups = PcaEx.FindPhenGroups(PhenData,2)
        
    Names = PcaEx.GetIndividuals(True,EvecData,0)
    count = len(Names)

##plotPca and RenderGraph should follow and might be enveloped into one 
    pcagraph =PcaGraph(Names,Groups,phenDic,EvecData,1,2)
    pcagraph.PlotPca()
    

def CreateAdmix(admixData,famData,pheData):
	
	#2D lists to contain file data. These will be moved to separate file classes once admix and pca structure is unified
	AdmixData = []
	##famData = []
	##pheData = []
        
	
	#get data from the specified files
	##admixData = admixEx.getAdmixData("small.Q.4")
	##famData = admixEx.getFamData("small.fam")
	##pheData = admixEx.getPhenoData("small.phe")
	
	#specifies which column to use for group information in phenotype file
	phenoColumn = 5

	for i in range(0,len(admixData)):
            AdmixData.append([])
            for x in range(0,len(admixData[i])):
                AdmixData[i].append(float(admixData[i][x]))

                
	admixGraph = AdmixGraph(AdmixData, famData, phenoData= pheData)
	admixGraph.plotGraph(phenoCol = phenoColumn)



	


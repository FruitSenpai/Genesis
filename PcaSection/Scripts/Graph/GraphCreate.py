import sys
import os

##path = os.getcwd()
##path = path+'\PcaGraphing'
##sys.path.insert(0, path)

from  PcaGraphing import PcaDataExtractor as PcaEx
from  PcaGraphing import PcaGraph

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
    PcaGraph.PlotPca(Names,Groups,phenDic,EvecData,1,2)
    PcaGraph.RenderGraph('Heading','x','y')

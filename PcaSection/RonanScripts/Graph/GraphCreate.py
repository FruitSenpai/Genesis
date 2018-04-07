import sys
import os

##path = os.getcwd()
##path = path+'\PcaGraphing'
##sys.path.insert(0, path)

from  PcaGraphing import PcaDataExtractor as PcaEx
from  PcaGraphing import PcaGraph


def CreatePca(PhenData,EvecData):

    
    
    phenData = {}
    Groups = []
    Names = []

    phenDic = PcaEx.FindPhenData(PhenData,2,0)
   # for key,val in phenDic.items():
      #  print(key +'=>'+val)
    Groups = PcaEx.FindPhenGroups(PhenData,2)
        
    Names = PcaEx.GetIndividuals(True,EvecData,0)
    count = len(Names)
    #for i in range(count):
       # print(Names[i])

    PcaGraph.PlotPca(Names,Groups,phenDic,EvecData,1,2)
    PcaGraph.RenderGraph('Heading','x','y')

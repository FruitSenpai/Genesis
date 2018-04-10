import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import os
import sys
'''
path = os.getcwd()
path = path+ '\..\..\FileManagement\\' 
sys.path.insert(0, path)

import FileImporter as fi
'''


##Finds All Groups(Dictionary)
##This function returns the number of individuals within a group as well as all the groups present within the phenotype file
def _checkIfUsedDic(data,Groups):
    hasBeenUsed = False
    
    if(len(Groups)>0):
        
        for x in range(len(Groups)):
            if(data in Groups):
                
                hasBeenUsed = True

    if(hasBeenUsed == False):
        Groups.update({data:1})
    if(hasBeenUsed == True):
        val = Groups.get(data)
        val+=1
        Groups.update({data:val})
        
    return Groups






##Creates a list of all the groups in the phenotype file
def _checkIfUsedList(data,Groups):
    hasBeenUsed = False
    
    if(len(Groups)>0):
        
        for x in range(len(Groups)):
            if(data ==Groups[x]):
                
                hasBeenUsed = True

    if(hasBeenUsed == False):
        Groups.append(data)
            
    return Groups





##Returns Pheno Data for individual name and associated group as dictionary
def FindPhenData(Data,GroupCol, NameCol):
    ##creates string with path to phen file
   # phenString = os.getcwd()
    #phenString= phenString+'\..\..\Data\comm.phe'

    ## phenotypeData will grab the Group name from the coloumn specified
    ##(NOTE THIS IS WHERE THE COLOUMN REPRESENTING THE PHEN FILE IS CHANGED)
    #phenotypeData = np.genfromtxt(phenString,unpack=True,usecols=2, dtype=str)
    phenotypeData = []
    key = []
    
    count =FindLength(Data)

    
    for i in range(count):

        phenotypeData.append(Data[i][GroupCol])

        ##key has the correspponding individial name for the phendata
        # key = np.genfromtxt(phenString,unpack=True,usecols=0, dtype=str)
        key.append(Data[i][NameCol])


  
    ##dictPhen has individual name and group name
    dictPhen = {}
    ##Groups contains all the groups in the phenfile


    for i in range(len(phenotypeData)):
        dictPhen.update({key[i]:phenotypeData[i]})

    return dictPhen
    



######Returns Phenotype Group data as a list
def FindPhenGroups(Data,GroupCol):
    ##creates string with path to phen file
  #  phenString = os.getcwd()
  #  phenString= phenString+'\..\..\Data\comm.phe'

    ## phenotypeData will grab the Group name from the coloumn specified
    ##(NOTE THIS IS WHERE THE COLOUMN REPRESENTING THE PHEN FILE IS CHANGED)
   ## phenotypeData = np.genfromtxt(phenString,unpack=True,usecols=2, dtype=str)
    ##key has the correspponding individial name for the phendata
    phenotypeData = []
    count =FindLength(Data)
    for i in range(count):
        phenotypeData.append(Data[i][GroupCol])

   
    ##Groups contains all the groups in the phenfile
    Groups = []
    GroupDic = {}
    
    for i in range(len(phenotypeData)):
        Groups = _checkIfUsedList(phenotypeData[i], Groups)



    return Groups


##Cretes list of Individuals from the PcaFile
def GetIndividuals(returnFirst,Data,NameCol):

 #   EvecString = os.getcwd()
  #  EvecString= EvecString+'\..\..\Data\comm-SYMCL.pca.evec'

    #A name in the evec file is formatted very specifically
    ## FirstCode:SecondCode

    ##NamesFirst contains the FirstCode half of the name
    NamesFirst=[]
    ##NamesSecond contains the SecondCode half of the name
    NamesSecond=[]
    ##contains all names from the evec file
  #  names = np.genfromtxt(EvecString,unpack=True, usecols = 0 ,skip_header=1, dtype=str)
    names = []
    count =FindLength(Data)
    for i in range(1,count):
        names.append(Data[i][NameCol])
    
    ##Name is split in half and the halves are placed in to their respective lists
    for i in range(len(names)):
        NamesTemp =names[i].split(':')
        NamesFirst.append(NamesTemp[0])
        NamesSecond.append(NamesTemp[1])

    if(returnFirst==True):
       return NamesFirst
    if(returnFirst == False):
        return NamesSecond


##Checking size of Data(how many lines)
def FindLength(Data):
        count = len(Data)
        return count


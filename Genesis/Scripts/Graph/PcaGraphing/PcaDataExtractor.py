""" Extracts data to be used in the PCA graph """

import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import os
import sys


##Finds All Groups(Dictionary)
def _checkIfUsedDic(data,Groups):
    """Returns the number of individuals within a group as well as all the groups present within the phenotype file."""
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







def _checkIfUsedList(data,Groups):
    """Creates a list of all the groups in the phenotype file."""
    
    hasBeenUsed = False
    
    if(len(Groups)>0):
        
        for x in range(len(Groups)):
            if(data ==Groups[x]):
                
                hasBeenUsed = True

    if(hasBeenUsed == False):
        Groups.append(data)
            
    return Groups






def FindPhenData(Data,GroupCol, NameCol):
    """Returns a dictionary with the key being an individual name and the value being its associated group."""
   
    phenotypeData = []
    key = []
    
    count =FindLength(Data)

    
    for i in range(count):

         ## phenotypeData will grab the Group name from the coloumn specified 
        phenotypeData.append(Data[i][GroupCol])

        ##key has the correspponding individial name for the phendata
        key.append(Data[i][NameCol])


  
    ##dictPhen has individual name and group name
    dictPhen = {}
    
    for i in range(len(phenotypeData)):
        dictPhen.update({key[i]:phenotypeData[i]})

    return dictPhen
    

def FindPhenGroups(Data,GroupCol):
    """ Returns Phenotype group data as a list."""


    ## phenotypeData will grab the Group name from the coloumn specified
    phenotypeData = []
    
    count =FindLength(Data)
    for i in range(count):
        phenotypeData.append(Data[i][GroupCol])

   
    ##Groups contains all the groups in the phenfile
    Groups = []
    GroupDic = {}

    #Checks which groups are used in this particular graph from the wide starting range 
    for i in range(len(phenotypeData)):
        Groups = _checkIfUsedList(phenotypeData[i], Groups)

    return Groups


##
def GetIndividuals(returnFirst,Data,NameCol):
    """ Creates list of individuals from the pca file."""

    #A name in the evec file is formatted very specifically
    ## FirstCode:SecondCode

    ##NamesFirst contains the FirstCode half of the name
    NamesFirst=[]
    ##NamesSecond contains the SecondCode half of the name
    NamesSecond=[]

    names = []
    count =FindLength(Data)
    #Gets all names from data file
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



def FindLength(Data):
    """ Checking size of Data(how many lines)"""
    count = len(Data)
    return count


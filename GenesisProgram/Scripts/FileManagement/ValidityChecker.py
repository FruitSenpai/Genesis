"""Checks the validity of filepaths with reagards to their chosen import destination."""
import os


def CheckPcaValid(fileName):
    """Checks if its a valid PCA file. """
    
    namelist = fileName.split('.')
    valid= False
    for i in range(0,len(namelist)):
        if(namelist[i] == 'pca'):
            valid = True
    
    if(valid == False):
       print('Invalid PCA')
       return False
    else:
        print('Valid PCA')
        return True
       


def CheckPhenValid(fileName):
    """Checks if its a valid phe file. """
    
    namelist = fileName.split('.')
    valid= False
    for i in range(0,len(namelist)):
        if(namelist[i] == 'phe'):
            valid = True
    
    if(valid == False):
       print('Invalid Phen')
       return False
    else:
        print('Valid Phen')
        return True


def CheckFamValid(fileName):
    """Checks if its a valid fam file. """
    
    namelist = fileName.split('.')
    valid= False
    for i in range(0,len(namelist)):
        if(namelist[i] == 'fam'):
            valid = True
    
    if(valid == False):
       print('Invalid Fam')
       return False
    else:
        print('Valid Fam')
        return True


def CheckAdmixValid(fileName):
    """Checks if its a valid admix file. """
    
    namelist = fileName.split('.')
    valid= False
    for i in range(0,len(namelist)):
        if(namelist[i] == 'Q'):
            valid = True
    
    if(valid == False):
       print('Invalid Admix')
       return False
    else:
        print('Valid Admix')
        return True



##First Parameter is which line we want to read starting at 0
##Second Paramter is which file to open
def CheckLineAmount(WhichLineToRead, phenString):
    """Checks amount of coloumns in line. """

    f = open(phenString)
    
    for i in range(0,WhichLineToRead+1):
        f.readline() 
    
    string = f.readline()
    #Take one line, split it up into a list.
    listString = string.split()
    #returns no. of coloumns
    return len(listString)


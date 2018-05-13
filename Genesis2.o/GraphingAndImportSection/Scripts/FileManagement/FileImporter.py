"""Handles the importing of files to make a graph"""
import sys
print(sys.path)
import FileManagement.File as File
import FileManagement.FileManager as fm
import os

import matplotlib.pyplot as plt

path = os.getcwd()
path = path+ '\..\Graph\\' 
sys.path.insert(0, path)

import Graph.GraphCreate as GraphCreate


class FileImporter():
    """Handles the importing of files to make a graph"""
    def __init__(self):
        self._fileManagers = []
       
    
    def CreateFile(self,Name,Data,Type,FM):
        """Creates a file.

        Creates a File object, gives it the edited data and stores the file in a file manager."""
        self._tempFile = File.File()
        self._tempFile.SetName(Name)
        self._tempFile.SetType(Type)
        self._tempFile.SetData(Data)
        
        self._tempFm = FM

        #Checks data type and adds it to relevant section of the File manager
        if(Type == 'Phen'):
               self._tempFm.SetPhenFile(self._tempFile)
              
        if(Type == 'Fam'):
               self._tempFm.SetFamFile(self._tempFile)
              
        if(Type == 'Admix'):
               self._tempFm.SetAdmixFile(self._tempFile)
             
        if(Type == 'Pca'):
               self._tempFm.SetPcaFile(self._tempFile)
               

        return self._tempFm
        
       
    
    def CreateFileManager(self,Name):
        """ Creates a file manager and adds it to the file importer."""
        self._FM = fm.FileManager()
        self._FM.SetName(Name)
        self._fileManagers.append(self._FM)
        return self._FM
    
    
    def AddFileManager(self,fileMan):
        """ Adds a already created file manager to the file importer. """
        self._fileManagers.append(fileMan)
    
    def GetManagers(self):
        """ Returns a list of all file managers. """
        return self._fileManagers


    def GetFileData(self,FilePath):
        """Takes the data from an imported file and returns it as a 2D list."""

        DataList = []

        
        try:
            ##Checking size of file(how many lines)
            #Makes sure that there is a file
            if(FilePath != None and os.stat(FilePath).st_size >0):
                countF = open(FilePath)
                count = len(countF.readlines())
                countF.close()
                
                      
                f = open(FilePath)
               
                for i in range(0,count):
                
                    tempString = f.readline()
                    tempList = tempString.split() 
                    DataList.append(tempList)


                return DataList
            ##Checks if file exists
            else :
                print('No File to extract Data from')
                return None
        except FileNotFoundError:
            return None

    def GetFileManager(self,fmName):
        """Returns specified file manager from list."""

        count = 0
        name = self._fileManagers[count].GetName()        

        while(name != fmName):
            name = self._fileManagers[count].GetName()
            
            if(count >= len(self._fileManagers)):
                print('CANNOT FIND FILE')
                break

            count += 1
                
        return self._fileManagers[count-1]

    def PrintFileManagers(self):
        """Print all file managers names to console."""
        for i in range(0,len(self._fileManagers)):
            print(self._fileManagers[i].GetName()+"---")

    def FindLength(self):
        """Returns length of self._filemanagers."""
        return len(self._fileManagers)


    def CreatePca(self,FI,pcaPath,phenPath,Name,pcaColoumnOne,PcaColoumnTwo,PhenColoumn,panel):
        """Creates PCA using imported data."""
        #Create File Manager
        FM = FI.CreateFileManager(Name)

        #Get the data from the path
        #Create File To Store Data
        #Get Data From File
        _PcaData =FI.GetFileData(pcaPath)
        FI.CreateFile('PCA IS THE NAME',_PcaData,'Pca',FM)
        DataPca = FI.GetFileManager(Name).GetPcaFile().GetData()
        

        #Get the data from the path if there is one
        #Create File To Store Data
        #Get Data From File
        _PhenData =FI.GetFileData(phenPath)
        if(_PhenData != None):
            
            FI.CreateFile('Phen IS THE NAME',_PhenData,'Phen',FM)
            DataPhen = FI.GetFileManager(Name).GetPhenFile().GetData()
        #checks if there is phen Data
        else:
            DataPhen = None
            

        GraphCreate.CreatePca(DataPhen,DataPca, pcaColoumnOne,PcaColoumnTwo,PhenColoumn,Name,panel)        
        

    def CreateAdmix(self, FI,admixPath,famPath,phenPath,Name,PheCol,nb):
        """Creates Admix using imported data."""
        #Create File Manager
        FM = FI.CreateFileManager(Name)

        #Get the data from the path
        #Create File To Store Data
        #Get Data From File
        AdmixData =FI.GetFileData(admixPath)
        FamData =FI.GetFileData(famPath)
        FI.CreateFile('Admix IS THE NAME',AdmixData,'Admix',FM)
        FI.CreateFile('Fam IS THE NAME',FamData,'Fam',FM)
        DataAdmix = FI.GetFileManager(Name).GetAdmixFile().GetData()
        DataFam = FI.GetFileManager(Name).GetFamFile().GetData()

        #Get the data from the path if there is one
        #Create File To Store Data
        #Get Data From File
        PheData =FI.GetFileData(phenPath)
        #Checks for phe data
        if(PheData !=None):
            FI.CreateFile('Phen IS THE NAME',PheData,'Phen',FM)
            DataAdmixPhen = FI.GetFileManager(Name).GetPhenFile().GetData()
        else:
            DataAdmixPhen = None

        GraphCreate.CreateAdmix(DataAdmix,DataFam,DataAdmixPhen,PheCol,nb, Name)
        
        
        
        






        
        
        
        

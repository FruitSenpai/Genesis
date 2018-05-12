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

    def __init__(self):
        self._fileManagers = []
       
    
    ##Creates a file and stores it in a file manager, returns a file manager for now untill i can figure out how to pass by reference
    def CreateFile(self,Name,Data,Type,FM):
        
        self._tempFile = File.File()
        self._tempFile.SetName(Name)
        self._tempFile.SetType(Type)
        self._tempFile.SetData(Data)
        
        self._tempFm = FM


        if(Type == 'Phen'):
               self._tempFm.SetPhenFile(self._tempFile)
              # print('Phen')
        if(Type == 'Fam'):
               self._tempFm.SetFamFile(self._tempFile)
              # print('fam')
        if(Type == 'Admix'):
               self._tempFm.SetAdmixFile(self._tempFile)
             #  print('Admix')
        if(Type == 'Pca'):
               self._tempFm.SetPcaFile(self._tempFile)
               #print('Pca')

        return self._tempFm
        
       
    #Creates a file manager and adds it to the file importer
    def CreateFileManager(self,Name):
        self._FM = fm.FileManager()
        self._FM.SetName(Name)
        self._fileManagers.append(self._FM)
        return self._FM
    #adds a already created file manager to the file importer
    def AddFileManager(self,fileMan):
        self._fileManagers.append(fileMan)
    #returns a list of all file managers
    def GetManagers(self):
        return self._fileManagers


##Outputs the data in the file as a 2d Array.
##Should make getting data easier plus we can now store it for later use
    def GetFileData(self,FilePath):

        DataList = []

        ##Checking size of file(how many lines)
        #Makes sure that there is a file
        if(FilePath != None):
            countF = open(FilePath)
            count = len(countF.readlines())
            countF.close()
            
                  
            f = open(FilePath)
           
            for i in range(0,count):
            
                tempString = f.readline()
                tempList = tempString.split() 
                DataList.append(tempList)

            '''
            for i in range(len(DataList)):
                print(DataList[i])
                print('\n')
            '''    

            return DataList
        ##Checks if file exists
        else :
            print('No File to extract Data from')
            return None

    def GetFileManager(self,fmName):

        count = 0
        name = self._fileManagers[count].GetName()
        print(len(self._fileManagers))
        

        while(name != fmName):
            name = self._fileManagers[count].GetName()
            print(name)
            
            if(count >= len(self._fileManagers)):
                print('CANNOT FIND FILE')
                break

            count += 1
                
        return self._fileManagers[count-1]
            
        '''
        print(len(self._fileManagers))
        for i in range(len(self._fileManagers)):
            print(self._fileManagers[i].GetPcaFile().GetName())
         '''

    def PrintFileManagers(self):
        for i in range(0,len(self._fileManagers)):
            print(self._fileManagers[i].GetName()+"---")

    def FindLength(self):
        return len(self._fileManagers)


    def CreatePca(self,FI,pcaPath,phenPath,Name,pcaColoumnOne,PcaColoumnTwo,PhenColoumn,panel):#''',pcaColoumnOne,PcaColoumnTwo,pcaColoumnThree,PhenColoumn '''
        #Create File Manager
        FM = FI.CreateFileManager(Name)

        #Get the data from the path
        #Create File To Store Data
        #Get Data From File
        _PcaData =FI.GetFileData(pcaPath)
        FI.CreateFile('PCA IS THE NAME',_PcaData,'Pca',FM)
        DataPca = FI.GetFileManager(Name).GetPcaFile().GetData()
        

        #Get the data from the path
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
        print(Name +" GRAAAAAAPh");
        
        

    def CreateAdmix(self, FI,admixPath,famPath,phenPath,Name,PheCol,nb):
        
        FM = FI.CreateFileManager(Name)

        AdmixData =FI.GetFileData(admixPath)
        FamData =FI.GetFileData(famPath)
        FI.CreateFile('Admix IS THE NAME',AdmixData,'Admix',FM)
        FI.CreateFile('Fam IS THE NAME',FamData,'Fam',FM)
        DataAdmix = FI.GetFileManager(Name).GetAdmixFile().GetData()
        DataFam = FI.GetFileManager(Name).GetFamFile().GetData()

        PheData =FI.GetFileData(phenPath)
        if(PheData !=None):
            FI.CreateFile('Phen IS THE NAME',PheData,'Phen',FM)
            DataAdmixPhen = FI.GetFileManager(Name).GetPhenFile().GetData()
        else:
            DataAdmixPhen = None

        GraphCreate.CreateAdmix(DataAdmix,DataFam,DataAdmixPhen,PheCol,nb)
        
        
        
        






        
        
        
        

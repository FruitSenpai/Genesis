
import File
import FileManager as fm
import os
import sys
path = os.getcwd()
path = path+ '\..\Graph\\' 
sys.path.insert(0, path)

import GraphCreate


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
        
       ## self._fileManagers.append(self._tempFm)

    def CreateFileManager(self,Name):
        self._FM = fm.FileManager()
        self._FM.SetName(Name)
        self._fileManagers.append(self._FM)
        return self._FM


##Outputs the data in the file as a 2d Array.
##Should make getting data easier plus we can now store it for later use
    def GetFileData(self,FilePath):

        DataList = []

        ##Checking size of file(how many lines)
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

    def GetFileManager(self,fmName):

        count = 0
        name = self._fileManagers[count].GetName()

        while(name != fmName):
            name = self._fileManagers[count].GetName()
            count += 1
            
            if(count >= len(self._fileManagers)):
                print('CANNOT FIND FILE')
                break

        return self._fileManagers[count]
            
        '''
        print(len(self._fileManagers))
        for i in range(len(self._fileManagers)):
            print(self._fileManagers[i].GetPcaFile().GetName())
         '''   


##Main
FI = FileImporter()
PcaData =FI.GetFileData('D:\Genesis\genesis-master\examples\PCA\comm-SYMCL.pca.evec')
PhenData =FI.GetFileData('D:\Genesis\genesis-master\examples\PCA\comm.phe')

FM = FI.CreateFileManager('FirstGraph')

FI.CreateFile('PCA IS THE NAME',PcaData,'Pca',FM)
FI.CreateFile('Phen IS THE NAME',PhenData,'Phen',FM)

DataPhen = FI.GetFileManager('FirstGraph').GetPhenFile().GetData()
DataPca = FI.GetFileManager('FirstGraph').GetPcaFile().GetData()

GraphCreate.CreatePca(DataPhen,DataPca)






        
        
        
        

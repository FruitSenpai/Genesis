import unittest
from Graph import GraphCreate
from Graph.PcaGraphing.PcaGraph import PcaGraph
from  Graph.PcaGraphing import PcaDataExtractor as PcaEx

class test_Graph(unittest.TestCase):
    #pass when given correct input
    def test_CompleteWithPhen(self):
        PcaData = GetFileData('..\\Data\\comm-SYMCL.pca.evec')
        PhenData = GetFileData("..\\Data\\comm.phe")
        _Test =GraphCreate.CreatePca(PhenData,PcaData,1,2,3,"Test",None)
        self.assertTrue(_Test)
    #Pass when given input and no phen data
    def test_CompleteWithoutPhen(self):
        PcaData = GetFileData('..\\Data\\comm-SYMCL.pca.evec')
        _Test =GraphCreate.CreatePca(None,PcaData,1,2,3,"Test",None)
        self.assertTrue(_Test)
     #Fail when given no inout with phen data
    def test_InCompleteWithPhen(self):
        PcaData = GetFileData('..\\Data\\comm-SYMCL.pca.evec')
        PhenData = GetFileData("..\\Data\\comm.phe")
        _Test =GraphCreate.CreatePca(PhenData,None,1,2,3,"Test",None)
        self.assertFalse(_Test)
        
        #self.assertRaises(TypeError,GraphCreate.CreatePca,PhenData,None,1,2,3,"Test",None)
    #pass when given no input what so ever
    def test_InCompleteWithoutPhen(self):
        PcaData = GetFileData('..\\Data\\comm-SYMCL.pca.evec')
        _Test =GraphCreate.CreatePca(None,None,1,2,3,"Test",None)
        print("HI")
        self.assertTrue(_Test)
        

def GetFileData(FilePath):

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

        
if __name__ == '__main__':
    unittest.main()

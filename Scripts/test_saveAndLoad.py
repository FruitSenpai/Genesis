import unittest
from Graph import GraphSaver
from Graph import GraphCreate
from Graph.PcaGraphing.PcaGraph import PcaGraph
from  Graph.PcaGraphing import PcaDataExtractor as PcaEx

class test_FileImporter(unittest.TestCase):
    #Makes sure data can always be extracted
    def setUp(self):
        self.PcaData = GetFileData('..\\Data\\comm-SYMCL.pca.evec')
        self.PhenData = GetFileData("..\\Data\\comm.phe")
        self.filePath ="..\\Data\\Test.gpf"
        self.filePath2 ="..\\Data\\Name.gpf"
        self._Test =GraphCreate.CreatePca( self.PhenData, self.PcaData,1,2,3,"Test",None)
        
    def tearDown(self):
        pass
    #tests the saving system works
    def test_SavePass(self):
        self.assertTrue(GraphSaver.saveGraph(self._Test,self.filePath))
        
    #tests the saving systems error catching
    def test_SaveFail(self):
        self.assertFalse(GraphSaver.saveGraph(self._Test,self._Test))
        self.assertFalse(GraphSaver.saveGraph(self._Test,8))

    #test load system works
    def test_LoadPass(self):
        _TestGraph = GraphSaver.loadGraph(self.filePath2)
        self.assertIsInstance(_TestGraph,PcaGraph)
    def test_LoadFail(self):
        _TestGraph = GraphSaver.loadGraph("")
        self.assertIsNone(_TestGraph)
        


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

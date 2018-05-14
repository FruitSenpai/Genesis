import unittest
from FileManagement import ValidityChecker as VC

class test_ValidityChecker(unittest.TestCase):
    
    def test_ValidityCheckerPass(self):
        _pca ='test.pca.evec'
        _phen ='test.phe'
        _admix ='test.Q.2'
        _Fam ='test.fam'
        
        pcaBool = VC.CheckPcaValid(_pca)
        PhenBool = VC.CheckPhenValid(_phen)
        AdmixBool = VC.CheckAdmixValid(_admix)
        FamBool = VC.CheckFamValid(_Fam)
        
        self.assertTrue(pcaBool)
        self.assertTrue(PhenBool)
        self.assertTrue(AdmixBool)
        self.assertTrue(FamBool)
        
    def test_ValidityCheckerFail(self):
        _pca ='test.pca1.'
        _phen ='test.pheno'
        _admix ='test.Q2'
        _Fam ='test.family'
        
        pcaBool = VC.CheckPcaValid(_pca)
        PhenBool = VC.CheckPhenValid(_phen)
        AdmixBool = VC.CheckAdmixValid(_admix)
        FamBool = VC.CheckFamValid(_Fam)
        
        self.assertFalse(pcaBool)
        self.assertFalse(PhenBool)
        self.assertFalse(AdmixBool)
        self.assertFalse(FamBool)



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

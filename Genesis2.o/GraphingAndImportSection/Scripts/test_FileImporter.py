import unittest
from FileManagement.FileImporter import FileImporter

class test_FileImporter(unittest.TestCase):
    #Makes sure data can always be extracted
    def test_TestGetFileData(self):
        fi = FileImporter()
        _var =fi.GetFileData('C:\\Users\\Athena II\\Documents\\GitHub\\Genesis\\GraphingAndImportSection\\Data\\comm-SYMCL.pca.evec')
        self.assertIsNotNone(_var)
        _var =fi.GetFileData(None)
        self.assertIsNone(_var)
        _var =fi.GetFileData('')
        self.assertIsNone(_var)
        _var =fi.GetFileData('C:\\Users\\Athena II\\Documents\\GitHub\\Genesis\\GraphingAndImportSection\\Data\\Empty.txt')
        self.assertIsNone(_var)






if __name__ == '__main__':
    unittest.main()

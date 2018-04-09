
import File


## a file manager will be responsible for holding all the files needed to create a graph
##contains the 4 import file types for now but will also contain customization data as well as annotation data
class FileManager():

    def __init__(self):

        self._Files = {}
        self._Name = 0

    def SetName(self,Name):
        self._Name = Name

    def GetName(self):
        return self._Name



    def GetPhenFile(self):
        if('Phen' in self._Files):
            return self._Files.get('Phen')
        else:
            print('No Phen File Found')
            return None

    def GetFamFile(self):
        if('Fam' in self._Files):
            return self._Files.get('Fam')
        else:
            print('No Fam File Found')
            return None

    def GetAdmixFile(self):
        if('Admix' in self._Files):
            return self._Files.get('Admix')
        else:
            print('No Admix File Found')
            return None

    def GetPcaFile(self):
        if('Pca' in self._Files):
            
            return self._Files.get('Pca')
        else:
            print('No Pca File Found')
            return None


    def SetPhenFile(self,theFile):
        self._Files.update({'Phen':theFile})

    def SetFamFile(self,theFile):
        self._Files.update({'Fam':theFile})

    def SetAdmixFile(self,theFile):
        self._Files.update({'Admix':theFile})

    def SetPcaFile(self,theFile):
        self._Files.update({'Pca':theFile})


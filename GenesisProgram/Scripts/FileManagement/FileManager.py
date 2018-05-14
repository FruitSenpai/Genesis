"""Responsible for holding all the files needed to create a graph."""
import FileManagement.File



##contains the 4 import file types.
class FileManager():
    """Creates an object to hold all data needed to create a graph."""
    def __init__(self):

        self._Files = {}
        self._Name = 0

    def SetName(self,Name):
        """Sets name of file manager."""
        self._Name = Name

    def GetName(self):
        """Returns name of file manager."""
        return self._Name



    def GetPhenFile(self):
        """Returns phen file."""
        if('Phen' in self._Files):
            return self._Files.get('Phen')
        else:
            print('No Phen File Found')
            return None

    def GetFamFile(self):
        """Returns fam file."""
        if('Fam' in self._Files):
            return self._Files.get('Fam')
        else:
            print('No Fam File Found')
            return None

    def GetAdmixFile(self):
        """Returns admix file."""
        if('Admix' in self._Files):
            return self._Files.get('Admix')
        else:
            print('No Admix File Found')
            return None

    def GetPcaFile(self):
        """Returns pca file."""
        if('Pca' in self._Files):
            
            return self._Files.get('Pca')
        else:
            print('No Pca File Found')
            return None


    def SetPhenFile(self,theFile):
        """Sets phen file."""
        self._Files.update({'Phen':theFile})

    def SetFamFile(self,theFile):
        """Sets fam file."""
        self._Files.update({'Fam':theFile})

    def SetAdmixFile(self,theFile):
        """Sets admix file."""
        self._Files.update({'Admix':theFile})

    def SetPcaFile(self,theFile):
        """Sets pca file."""
        self._Files.update({'Pca':theFile})




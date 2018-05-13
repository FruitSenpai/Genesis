""" Generic class to hold a single type of data for a graph.""" 

class File():
    """Create an object to hold data."""
    def __init__(self):

        self._Data=[]
        self._FileName = ''
        self._FileType = ''



    def SetName(self, name):
        """ Sets name of file."""
        self._FileName = name

    def SetType(self, typeString):
        """ Sets type of file."""
        self._FileType = typeString

    def SetData(self, theData):
        """ Adds data for the file to store."""
        self._Data = theData

        

    def GetName(self):
        """ Gets file name."""
        return self._FileName

    def GetType(self):
        """ Gets file type."""
        return self._FileType

    def GetData(self):
        """ Gets file Data."""
        return self._Data

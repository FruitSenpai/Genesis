

class File():

    def __init__(self):

        self._Data=[]
        self._FileName = ''
        self._FileType = ''



    def SetName(self, name):
        self._FileName = name

    def SetType(self, typeString):
        self._FileType = typeString

    def SetData(self, theData):
        self._Data = theData

        

    def GetName(self):
        return self._FileName

    def GetType(self):
        return self._FileType

    def GetData(self):
        return self._Data

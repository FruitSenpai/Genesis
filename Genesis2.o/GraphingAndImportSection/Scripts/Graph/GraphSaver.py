"""Saves and loads graphs."""
import pickle

def saveGraph(graph, fileName):
        """Saves graph object."""
        #closes file immediately after done
        with open(fileName, "wb") as outFile:
                pickle.dump(graph, outFile)

def loadGraph(filePath):
        """Loads graph object."""
        #closes file immediately after done
        with open(filePath, "rb") as binaryData: #read data in binary format
                graph = pickle.load(binaryData)
        
        return graph


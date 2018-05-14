"""Saves and loads graphs."""
import pickle

def saveGraph(graph, fileName):
        """Saves graph object."""
	#closes file immediately after done
        try:
                with open(fileName, "wb") as outFile:
                        pickle.dump(graph, outFile)
                        return True
        except OSError:
                print("OS ERROR GraphSave")
                return False

def loadGraph(filePath):
        """Loads graph object."""
	#closes file immediately after done
        try:
                with open(filePath, "rb") as binaryData: #read data in binary format
                        graph = pickle.load(binaryData)
                
                return graph
        except FileNotFoundError:
                return None

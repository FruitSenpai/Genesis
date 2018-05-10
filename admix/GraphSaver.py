import pickle

def saveGraph(graph, fileName):
	outFile = open(fileName, "wb")
	pickle.dump(graph, outFile)
	outFile.close()

def loadGraph(filePath):
	binaryData = open(filePath, "rb") #read data in binary format
	graph = pickle.load(binaryData)
	
	return graph


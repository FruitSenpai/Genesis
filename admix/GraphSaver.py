import pickle

def saveGraph(graph, fileName):
	#closes file immediately after done
	with open(fileName, "wb") as outFile:
		pickle.dump(graph, outFile)

def loadGraph(filePath):
	#closes file immediately after done
	with open(filePath, "rb") as binaryData: #read data in binary format
		graph = pickle.load(binaryData)
	
	return graph


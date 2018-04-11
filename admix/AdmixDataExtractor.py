import numpy as np

def getAdmixData(admixFilePath):
	admixData = []
	admixFile = open(admixFilePath, "r")

	for line in admixFile:
		admixData.append(np.fromstring(line, dtype= float, sep="  "))

	admixFile.close()
	return admixData

def getFamData(famFilePath):
	famData = []
	famFile = open(famFilePath, "r")

	for line in famFile:
		famData.append(line.split())
		#famData.append(np.fromstring(line, sep="  "))

	famFile.close()

	return famData

def getPhenoData(phenoFilePath):
	phenoData = []
	phenoFile = open(phenoFilePath, "r")
	
	for line in phenoFile:
		phenoData.append(line.split())
		#phenoData.append(np.fromstring(line, sep="  "))
	
	phenoFile.close()
	return phenoData

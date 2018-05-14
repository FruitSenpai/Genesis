#This class has functions which return 2D lists from specified files 

import numpy as np

#following functions get info from files and return them as 2D lists (will become obsolete when admix functionality is integrated with the file management stuff)
#getPhenoData and getFamData read in strings (and thus are redundant) whereas getAdmixData reads in floats

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

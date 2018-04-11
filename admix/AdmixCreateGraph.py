#This class takes data from the input files and renders the admix plot (is not prepared for not having a pheno file entered)

import numpy as np
import matplotlib.pyplot as plt

import AdmixDataExtractor as admixEx
from AdmixGraph import AdmixGraph

def CreateAdmix():
	
	#2D lists to contain file data. These will be moved to separate file classes once admix and pca structure is unified
	admixData = []
	famData = []
	pheData = []
	
	#get data from the specified files
	admixData = admixEx.getAdmixData("small.Q.4")
	famData = admixEx.getFamData("small.fam")
	pheData = admixEx.getPhenoData("small.phe")
	
	#specifies which column to use for group information in phenotype file
	phenoColumn = 5

	admixGraph = AdmixGraph(admixData, famData, phenoData= pheData)
	admixGraph.plotGraph(phenoCol = phenoColumn)

CreateAdmix()

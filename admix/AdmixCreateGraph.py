import numpy as np
import matplotlib.pyplot as plt

import AdmixDataExtractor as admixEx
from AdmixGraph import AdmixGraph

def CreateAdmix():
	
	admixData = []
	famData = []
	pheData = []

	admixData = admixEx.getAdmixData("small.Q.4")
	famData = admixEx.getFamData("small.fam")
	pheData = admixEx.getPhenoData("small.phe")
	
	phenoColumn = 5

	admixGraph = AdmixGraph(admixData, famData, phenoData= pheData)
	admixGraph.plotGraph(phenoCol = phenoColumn)

CreateAdmix()

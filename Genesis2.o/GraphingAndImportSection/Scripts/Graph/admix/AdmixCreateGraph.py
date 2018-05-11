#This class takes data from the input files and renders the admix plot (is not prepared for not having a pheno file entered)

import numpy as np
import matplotlib.pyplot as plt

from Graph.admix import AdmixDataExtractor as admixEx
from Graph.admix.AdmixGraph import AdmixGraph

#all the 2d list data will be passed as parameters here
#allow for changing of main headings and axes

def CreateAdmix(num):
	
	#2D lists to contain file data. These will be moved to separate file classes once admix and pca structure is unified
	admixData = []
	famData = []
	pheData = []
	
	#get data from the specified files
	admixData = admixEx.getAdmixData("small.Q." + str(num))
	famData = admixEx.getFamData("small.fam")
	pheData = admixEx.getPhenoData("small.phe")
	
	#to run with phenotype data uncomment the pheData line and the second phenoColumn line

	#specifies which column to use for group information in phenotype file
	#phenoColumn = None
	phenoColumn = 5

	admixGraph = AdmixGraph(admixData, famData, phenoData= pheData)
	admixGraph.plotGraph(phenoCol = phenoColumn)

CreateAdmix(2)
CreateAdmix(5)
CreateAdmix(4)


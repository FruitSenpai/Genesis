import numpy as np
import matplotlib.pyplot as plt

from AdmixIndividual import AdmixIndividual

class AdmixGraph:

	individualList = []
	groupList = []
	
	def __init__(self, individualData, famData, phenoData= None):
		
		if phenoData is None:
			addIndividuals(self, individualData, famData)
			print("no phenotype data")
		else:
			self.addIndividuals(individualData, famData)
			
			#set up secondary group lists for each secondary column in phe file
			for i in range(2, len(phenoData)):
				self.groupList.append([])

			self.addGroups(phenoData)

	def addIndividuals(self, individualData, famData):
		for i in range(len(individualData)):			
				person = AdmixIndividual(famData[i][0], famData[i][1], individualData[i])
				self.individualList.append(person)

	def addGroups(self, phenotypeData):
		
		for person in self.individualList:
			firstId = person.id1
			secondId = person.id2
			
			for phenoEntry in phenotypeData:
				
				if(phenoEntry[0] == firstId and phenoEntry[1] == secondId):
					#print("match")
					for colIndex in range(2, len(phenoEntry)):
						group = phenoEntry[colIndex]
						person.addGroup(group)
						self.checkGroupExistence(colIndex - 2, group)
						
		
	def checkGroupExistence(self, listColIndex, groupName):
		exist = False
		
		for group in self.groupList[listColIndex]:
			if (group == groupName):
				exist = True
				break
		
		if(exist == False):
			self.groupList[listColIndex].append(groupName)
	
	#sorts in reverse order for now
	def sortByGroupAlpha(self, listToSort, groupCol):
		listToSort.sort(key=lambda person: person.groups[groupCol], reverse = True)
	
	def findGroupPositions(self, pplList, groupIndex):
		posList = [[], []] #groupName-position pair
		currGroup = ""
		
		for pIndex in range(len(pplList)):
			if (pplList[pIndex].groups[groupIndex] != currGroup): #start new position
				currGroup = pplList[pIndex].groups[groupIndex]
				posList[0].append(currGroup)
				posList[1].append(pIndex)

		return posList
		
		
	def plotGraph(self, phenoCol= None):
		personList = self.individualList[:] #clone the list because we need to scale the values
		#admixList = list(self.individualList.admixData) 
		
		#scale all ancestry values for individuals so that the sum of ancestry points equals 1.0 (100%)
		for i in range(len(personList)):
			sum = 0
			for j in range(len(personList[i].admixData)):
				sum += personList[i].admixData[j]
			#print(i+1, ": ", sum)
			
			scalingFactor = 1.0 / sum #scaling factor to apply for the individual's ancestry points

			for j in range(len(personList[i].admixData)):
				personList[i].admixData[j] *= scalingFactor
				#admixList[i][j] *= scalingFactor
		#end scaling portion
		

		#group management stuff
		"""for person in personList:
			print(person.id1, " ", person.id2)"""
		
		"""for colList in self.groupList:
			for group in colList:
				print(group)"""
		
		print("For chosen column index the groups are: ")

		for group in self.groupList[phenoCol - 3]:
			print(group)

		self.sortByGroupAlpha(personList, phenoCol - 3)

		for person in personList:
			print(person.groups[phenoCol - 3])

		"""for person in personList:
			print(person.id1, " ", person.id2, " ", person.groups[0], " ", person.groups[1], " ", person.groups[2], " ", person.groups[3], " ")"""

		#now render the graph
		individuals_x = np.arange(len(personList))

		finalGraphList = []

		for i in range(len(personList)):
			finalGraphList.append(personList[i].admixData)

		individuals_y = np.column_stack(finalGraphList) #stack each individual's ancestry data as a single column
		

			
		tickList = self.findGroupPositions(personList, phenoCol - 3)
		
		
		#plot on the stack plot
		fig, ax = plt.subplots()
		ax.stackplot(individuals_x, individuals_y)
		plt.xticks(tickList[1], tickList[0])
		plt.show()

		
	

	
			
				

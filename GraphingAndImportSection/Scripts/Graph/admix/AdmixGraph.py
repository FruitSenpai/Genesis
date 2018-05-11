#This graph contains information and functions which control the properties of an admix graph

import copy
import numpy as np
import matplotlib.pyplot as plt

from Graph.admix.AdmixIndividual import AdmixIndividual
from Graph.admix.AdmixAncestry import AdmixAncestry
from Graph.admix.AdmixGroup import AdmixGroup

from GUIFrames import DataHolder

class AdmixGraph:

        #list of all individuals represented in graph
        individualList = []
        
        #2D list of all groups represented in graph (groups are seperated into their respective columns)
        #groupList = []
        admixGroupList = []

        #order of groups for selected column
        groupOrder = []

        #index for selected column of groups
        groupColIndex = 0
        
        #number of ancestries in the graph
        numAncestries = 0
        
        #list of ancestries and their properties (currently just colour)
        ancestryList = []
        
        #order of ancestries
        ancestryOrder = []

        #default list of colours
        colourList = ["red", "blue", "orange", "green", "yellow", "purple", "brown", "pink", "cyan"]

        def __init__(self, individualData, famData,nb, name, phenoData= None):
                
                self.individualList = []
                #self.groupList = []
                self.admixGroupList = []
                self.groupOrder = []            
                self.groupColIndex = 0
                self.ancestryList = []
                self.ancestryOrder = []
                self.numAncestries = len(individualData[0])
                self._nb = nb
                self._name = name

                if phenoData is None:
                        self.addIndividuals(individualData, famData)
                        print("no phenotype data")
                else:
                        self.addIndividuals(individualData, famData)
                        
                        #set up secondary group lists for each secondary column in phe file
                        for i in range(2, len(phenoData)):
                                self.admixGroupList.append([])
                                #self.groupList.append([])

                        self.addGroups(phenoData)
                
                self.setupAncestries()

                self._DH = DataHolder
                
        
        #create individual objects with id names as well as their admix data
        def addIndividuals(self, individualData, famData):
                for i in range(len(individualData)):                    
                                person = AdmixIndividual(famData[i][0], famData[i][1], individualData[i])
                                self.individualList.append(person)

        
        #for each individual, find their entry in the phenotype data and assign them their corresponding groups (pheno dependent)
        def addGroups(self, phenotypeData):
                
                for person in self.individualList:
                        firstId = person.id1
                        secondId = person.id2
                        
                        for phenoEntry in phenotypeData:
                                
                                #if current individual is found in the phenotype data
                                if(phenoEntry[0] == firstId and phenoEntry[1] == secondId):
                                        
                                        #add all groups for that entry
                                        for colIndex in range(2, len(phenoEntry)):
                                                group = phenoEntry[colIndex]
                                                person.addGroup(group)
                                                self.checkGroupExistence(colIndex - 2, group) #check if the group we're adding is in the graph's global group list
        
        def setupAncestries(self):
                for i in range(self.numAncestries):
                        ancestry = AdmixAncestry(i, AdmixGraph.colourList[i % self.numAncestries])
                        self.ancestryList.append(ancestry)
                        self.ancestryOrder.append(i)
                        
                        #calculate and set dominance for ancestry i
                        dominance = 0;
                        for person in self.individualList:
                                dominance += person.admixData[i]
                        
                        self.ancestryList[i].setDominance(dominance)
                                                
        
        #if the specified group name doesn't yet exist in the specified column in the global group list, add the group (pheno dependent). If it exists, increment the group's dominance
        def checkGroupExistence(self, listColIndex, groupName):
                exist = False
                
                for group in self.admixGroupList[listColIndex]:
                        if (group.name == groupName):
                                group.dominance += 1 #increment dominance because another individual exists
                                exist = True
                                break
                
                if(exist == False):
                        #self.groupList[listColIndex].append(groupName)
                        admixGroup = AdmixGroup(groupName, len(self.admixGroupList[listColIndex]))
                        self.admixGroupList[listColIndex].append(admixGroup)
        

        #sort individuals by the order dictated by their group order values (should go least to most)
        def sortByGroupOrder(self, groupCol):
                
                groupDic = {}
                
                #setup group dictionary
                for admixGroup in self.admixGroupList[groupCol]:
                        groupDic[admixGroup.name] = admixGroup

                for i in range(len(self.individualList) - 1):
                        for j in range(i, len(self.individualList)):
                                groupI = self.individualList[i].groups[groupCol] #person i's group name
                                groupJ = self.individualList[j].groups[groupCol] #person i's group name
                                
                                #use group names to find relevant admixGroup objects in dictionaries and then swap
                                if(groupDic[groupI].orderInGraph > groupDic[groupJ].orderInGraph):
                                        tempPerson = self.individualList[i]
                                        self.individualList[i] = self.individualList[j]
                                        self.individualList[j] = tempPerson;
                                        
                                        
                                

        #sorts individuals by group alphabetical order (currently does reverse alphabetical order) (pheno dependent) (WON'T WORK WITH NEW STRUCTURE)
        def sortByGroupAlpha(self, listToSort, groupCol):
                listToSort.sort(key=lambda person: person.groups[groupCol], reverse = True)
        
        #sorts individuals by group dominance (most dominant to least dominant group) (pheno dependent)
        def sortByGroupDominance(self, listToSort, groupCol):
                
                #stores the dominance values for each group
                dominanceDic = {}

                #initialize dominance list values
                for group in self.groupList[groupCol]:
                        dominanceDic[group] = 0

                #sum individuals to find group dominance
                for person in listToSort:
                        #if this person's group is in the dictionary, increment that group's dominance
                        if (person.groups[groupCol]) in dominanceDic:
                                dominanceDic[person.groups[groupCol]] += 1

                        else:
                                print("there's a problem here")

                #sort group by dominance now using the dominance dictionary
                for i in range(len(listToSort) - 1):
                        for j in range(i, len(listToSort)):
                                groupI = listToSort[i].groups[groupCol]
                                groupJ = listToSort[j].groups[groupCol]
                                
                                
                                if(dominanceDic[groupI] < dominanceDic[groupJ]):
                                        tempPerson = listToSort[i]
                                        listToSort[i] = listToSort[j]
                                        listToSort[j] = tempPerson
                
        
        def sortByGroupDominanceV2(self, groupCol):
                
                #reassign group orders
                for i in range(len(self.admixGroupList[groupCol]) - 1):
                        for j in range(i, len(self.admixGroupList[groupCol])):
                                admixGroupI = self.admixGroupList[groupCol][i]
                                admixGroupJ = self.admixGroupList[groupCol][j]
                                
                                if(admixGroupI.dominance < admixGroupJ.dominance):
                                        tempGroup = self.admixGroupList[groupCol][i]
                                        self.admixGroupList[groupCol][i] = self.admixGroupList[groupCol][j]
                                        self.admixGroupList[groupCol][j] = tempGroup

                                        admixGroupI.orderInGraph = j
                                        admixGroupJ.orderInGraph = i
                                        

                                        

                #after group orders are reassigned, sort the actual data
                self.sortByGroupOrder(groupCol)
                
                
                                        
        #sorts admix data columns by dominant ancestry (sorts least to most dominant)
        def sortByAncestryDominance(self, listToSort):
                
                ancestrySumList = []
                
                #initialize the ancestry columns in ancestry sum list to 0
                firstPersonData = listToSort[0]
                for value in firstPersonData:
                        ancestrySumList.append(0)
                
                #sum total points for each ancestry
                for personData in listToSort:
                        for index in range(len(personData)):
                                ancestrySumList[index] += personData[index]
                
                """#print sums before sorting
                for sum in ancestrySumList:
                        print(sum)"""

                #sort based on ancestry points (better way to do this?)
                for i in range(len(ancestrySumList) - 1):
                        for j in range(i, len(ancestrySumList)):
                                if(ancestrySumList[i] > ancestrySumList[j]):
                                        tempSumList = ancestrySumList[i]
                                        ancestrySumList[i] = ancestrySumList[j]
                                        ancestrySumList[j] = tempSumList
                                        
                                        for person in listToSort:
                                                tempVal = person[i]
                                                person[i] = person[j]
                                                person[j] = tempVal

                                        """tempValList = listToSort[i]
                                        listToSort[i] = listToSort[j]
                                        listToSort[j] = tempValList"""

                """#print sums after sorting
                for sum in ancestrySumList:
                        print(sum)"""           
        
        #sorts least to most dominant
        def sortByAncestryDominanceV2(self):
                
                for i in range(len(self.ancestryList) - 1):
                        for j in range(i, len(self.ancestryList)):
                                if(self.ancestryList[i].dominance > self.ancestryList[j].dominance):
                                        tempAncestry = self.ancestryList[i]
                                        self.ancestryList[i] = self.ancestryList[j]
                                        self.ancestryList[j] = tempAncestry

                """#tempList = self.ancestryList[:]
                #tempList = self.ancestryList.copy()
                tempList = copy.deepcopy(self.ancestryList)

                for i in range(len(tempList) - 1):
                        for j in range(i, len(tempList)):
                                if(tempList[i].dominance > tempList[j].dominance):
                                        tempAncestry = tempList[i]
                                        tempList[i] = tempList[j]
                                        tempList[j] = tempAncestry
                
                
                for i in range(len(tempList)):
                        print(str(tempList[i].orderInGraph) + "\t" + str(tempList[i].dominance))
                #now copy orders from temp list onto actual list
                for i in range(len(tempList)):
                        print(str(tempList[i].orderInGraph) + "\t" + str(tempList[i].dominance))
                        self.ancestryList[i].orderInGraph = tempList[i].orderInGraph

                #after reassigning dominance values, reassign values in ancestryOrder list (not needed, no?)
                for i in range(len(self.ancestryList)):
                        self.ancestryOrder[i] = tempList[i].orderInGraph"""
                

        def returnGraphData(self):
                data = ""
                
        
        #finds where each group begins in the list so that it's known where to place group labels on the graphs (pheno dependent)
        def findGroupPositions(self, pplList, groupIndex):
                
                #the first column contains group names and the other the positions of the corresponding group
                posList = [[], []] #groupName-position pair
                currGroup = ""
                
                for pIndex in range(len(pplList)):
                        if (pplList[pIndex].groups[groupIndex] != currGroup): #if the next group has been found
                                currGroup = pplList[pIndex].groups[groupIndex]
                                posList[0].append(currGroup)
                                posList[1].append(pIndex)

                return posList
        '''
        def testGroups(self):
                
                for i in range(len(self.admixGroupList[self.groupColIndex])):
                        group = self.admixGroupList[self.groupColIndex][i]
                        print(str(i) + ":\t" + str(group.orderInGraph) + "\t" + group.name + "\t" + str(group.dominance))

                """for i in range(len(self.admixGroupList[self.groupColIndex])):
                        group = self.admixGroupList[self.groupColIndex][i]
                        print(group.name + "\t" + str(group.orderInGraph) + "\t" + str(group.dominance))"""
                

        def testAncestries(self):
                for i in range(len(self.ancestryList)):
                        ancestry = self.ancestryList[i]
                        print(str(i) + ":\t" + str(ancestry.orderInData) + "\t" + ancestry.colour + "\t" + str(ancestry.dominance))
                """for i in range(len(self.ancestryList)):
                        ancestry = self.ancestryList[i]
                        print(ancestry.colour + "\t" + str(ancestry.orderInGraph) + "\t" + str(self.ancestryOrder[i]) + "\t" + str(ancestry.dominance))"""
'''
        #plot the graph 
        def plotGraph(self, phenoCol= None):
                
                if phenoCol is not None:
                        self.groupColIndex = phenoCol - 3
                
                #group management stuff
                
                if phenoCol is not None:
                        #self.sortByGroupAlpha(personList, self.groupColIndex) #sort the list by group alphabetical order
                        #self.sortByGroupDominance(personList, self.groupColIndex) #sort the list by group dominance
                        self.sortByGroupDominanceV2(self.groupColIndex)
                        print("hey")
                
                personList = copy.deepcopy(self.individualList) #clone the individuals list because we need to scale the values 
                
                #scale all ancestry points for individuals so that the sum of ancestry points for each individual equals 1.0 (100%)
                for i in range(len(personList)):
                        
                        #current sum of ancestry points for this individual
                        sum = 0
                        for j in range(len(personList[i].admixData)):
                                sum += personList[i].admixData[j]
                        
                        scalingFactor = 1.0 / sum #scaling factor to apply for the individual's ancestry points

                        for j in range(len(personList[i].admixData)):
                                personList[i].admixData[j] *= scalingFactor
                #end scaling portion

                #now render the graph
                individuals_x = np.arange(len(personList))
                
                #processed data to plot
                processedAdmixList = []

                for i in range(len(personList)):
                        processedAdmixList.append(personList[i].admixData)

                #before stacking values, sort by dominance
                #self.sortByAncestryDominance(processedAdmixList)
                self.sortByAncestryDominanceV2()
                
                #format data for plotting functions
                rotatedList = np.column_stack(processedAdmixList) #stack each individual's ancestry data as a single column
                
                #add columns to the individuals_y list by specified ancestry order
                individuals_y = [None] * self.numAncestries

                #seems to work, wrap head around later
                for i in range(len(self.ancestryList)):
                        individuals_y[i] = rotatedList[self.ancestryList[i].orderInData]
                

                #list containing label info for the x-axis
                if phenoCol is not None:        
                        tickList = self.findGroupPositions(personList, self.groupColIndex)
                
                

                #test colour list
                ancestryColours = [None] * self.numAncestries
                for i in range(0, self.numAncestries):
                        #replace i index in ancestryList with index of ancestry order
                        #ancestryColours.append(self.ancestryList[self.ancestryOrder[i]].colour)
                        ancestryColours[i] = self.ancestryList[i].colour #also works, wrap head around later
                
                
                #self.testGroups()
                #self.testAncestries()
                #colorList[0] = 'C3'
                #plot on the stack plot
                #replace "figure2" with name so multiple can be plotted        
                self._fig = self._nb.add(self._name)
                self._ax = self._fig.gca()
                self._ax.stackplot(individuals_x, individuals_y, colors = ancestryColours)

                if phenoCol is not None:
                        self._ax.set_xticks(tickList[1],minor = False)
                        self._ax.set_xticklabels(tickList[0],minor=False)
                self._DH.Figures.update({self._name:self._fig})
                self._DH.Graphs.update({self._name:self})
                        
               
                
               
		#plt.show()

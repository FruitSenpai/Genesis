#This graph contains information and functions which control the properties of an admix graph

import copy
import numpy as np
import matplotlib.pyplot as plt

from Graph.admix.AdmixIndividual import AdmixIndividual
from Graph.admix.AdmixAncestry import AdmixAncestry
from Graph.admix.AdmixGroup import AdmixGroup

from GUIFrames import DataHolder

class AdmixGraph:
        """Used to store attributes and functions which control admixture graphs."""
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
                """Initializes an AdmixGraph object along with its properties."""
                self.individualList = []
                #self.groupList = []
                self.admixGroupList = [] #list of all groups present in this graph
                self.groupOrder = []            
                self.groupColIndex = 0
                self.ancestryList = [] #list of all ancestries present in this graph
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

        def getGroupColIndex(self):
            """Returns the current group column index."""
            return self.groupColIndex

        def getPhenoColumn(self):
            """Returns the current phenotype column."""
            return self.groupColIndex + 3

        def setNotebook(self, notebook):
            """Sets a reference to the notebook which stores this graph's figure."""
            self._nb = notebook

        def getName(self):
            """Returns the name of this graph."""
            return self._name

        #update name of graph as well as external references
        def setName(self, newName, oldName):
            """Set the name of this graph and remove all references to the old name in external data structures"""
            self._name = newName

            #get rid of obsolete dictionary keys
            figure = DataHolder.Figures.pop(oldName) #generates KeyError if not found
            graph = DataHolder.Graphs.pop(oldName)

            DataHolder.Graphs.update({newName:self})
            DataHolder.Figures.update({newName:figure})

                
                
        
        def addIndividuals(self, individualData, famData):
                """Create individual objects with id names as well as their admix data."""
                for i in range(len(individualData)):                    
                                person = AdmixIndividual(famData[i][0], famData[i][1], individualData[i])
                                self.individualList.append(person)

        
        
        def addGroups(self, phenotypeData):
                """For each individual, find their entry in the phenotype data and assign them their corresponding groups (pheno dependent)."""
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
                                                self.checkGroupExistence(colIndex - 2, person, group) #check if the group we're adding is in the graph's global group list
        
        def setupAncestries(self):
                """Setup all the ancestries using the length of a single individual's admixData list."""
                for i in range(self.numAncestries):
                        ancestry = AdmixAncestry("Anc." + str(i), i, i, AdmixGraph.colourList[i % self.numAncestries])
                        self.ancestryList.append(ancestry)
                        self.ancestryOrder.append(i)
                        
                        #calculate and set dominance for ancestry i
                        dominance = 0;
                        for person in self.individualList:
                                dominance += person.admixData[i]
                        
                        self.ancestryList[i].setDominance(dominance)
                                                
        
        
        def checkGroupExistence(self, listColIndex, person, groupName):
                """If the specified group name doesn't yet exist in the specified column in the global group list, add the group (pheno dependent). If it exists, increment the group's dominance."""        
                exist = False
                
                for group in self.admixGroupList[listColIndex]:
                        if (group.name == groupName):
                                group.dominance += 1 #increment dominance because another individual exists
                                group.individuals.append(person)
                                exist = True
                                break
                
                if(exist == False):
                                #self.groupList[listColIndex].append(groupName)
                                admixGroup = AdmixGroup(groupName, len(self.admixGroupList[listColIndex]))
                                admixGroup.individuals.append(person)
                                self.admixGroupList[listColIndex].append(admixGroup)
        
	
        def setGroupHidden(self, indexInOrder, hide):
                """Set the visibility of the selected group."""
                group = self.admixGroupList[self.groupColIndex][indexInOrder]
                group.setGroupHidden(hide)

        def sortByGroupOrder(self):
                """Sort individuals by the order dictated by their ascending group order values."""
                groupDic = {}
                
                #setup group dictionary
                for admixGroup in self.admixGroupList[self.groupColIndex]:
                        groupDic[admixGroup.name] = admixGroup

                for i in range(len(self.individualList) - 1):
                        for j in range(i, len(self.individualList)):
                                groupI = self.individualList[i].groups[self.groupColIndex] #person i's group name
                                groupJ = self.individualList[j].groups[self.groupColIndex] #person i's group name
                                
                                #use group names to find relevant admixGroup objects in dictionaries and then swap
                                if(groupDic[groupI].orderInGraph > groupDic[groupJ].orderInGraph):
                                        tempPerson = self.individualList[i]
                                        self.individualList[i] = self.individualList[j]
                                        self.individualList[j] = tempPerson;
                                        
                                        
                                

        

        def sortByGroupAlphaV2(self):
                """Sorts individuals by group alphabetical order (pheno dependent)."""
                #reassign group orders
                for i in range(len(self.admixGroupList[self.groupColIndex]) - 1):
                        for j in range(i, len(self.admixGroupList[self.groupColIndex])):
                                admixGroupI = self.admixGroupList[self.groupColIndex][i]
                                admixGroupJ = self.admixGroupList[self.groupColIndex][j]
                                
                                if(admixGroupI.name.lower() > admixGroupJ.name.lower()):
                                        tempGroup = self.admixGroupList[self.groupColIndex][i]
                                        self.admixGroupList[self.groupColIndex][i] = self.admixGroupList[self.groupColIndex][j]
                                        self.admixGroupList[self.groupColIndex][j] = tempGroup

                                        admixGroupI.orderInGraph = j
                                        admixGroupJ.orderInGraph = i
		
		#after group orders are reassigned, sort the actual data
                self.sortByGroupOrder()


        
                
        
        def sortByGroupDominanceV2(self, mostToLeast):
                """Sorts individuals by group dominance (pheno dependent)."""
                success = False

                try:
                        #reassign group orders in a selection sort
                        for i in range(len(self.admixGroupList[self.groupColIndex]) - 1):
                                for j in range(i, len(self.admixGroupList[self.groupColIndex])):
                                        admixGroupI = self.admixGroupList[self.groupColIndex][i]
                                        admixGroupJ = self.admixGroupList[self.groupColIndex][j]
                                
                                        if mostToLeast:
                                               if(admixGroupI.dominance < admixGroupJ.dominance):
                                                       tempGroup = self.admixGroupList[self.groupColIndex][i]
                                                       self.admixGroupList[self.groupColIndex][i] = self.admixGroupList[self.groupColIndex][j]
                                                       self.admixGroupList[self.groupColIndex][j] = tempGroup

                                                       admixGroupI.orderInGraph = j
                                                       admixGroupJ.orderInGraph = i
                                        else:
                                               if(admixGroupI.dominance > admixGroupJ.dominance):
                                                       tempGroup = self.admixGroupList[self.groupColIndex][i]
                                                       self.admixGroupList[self.groupColIndex][i] = self.admixGroupList[self.groupColIndex][j]
                                                       self.admixGroupList[self.groupColIndex][j] = tempGroup

                                                       admixGroupI.orderInGraph = j
                                                       admixGroupJ.orderInGraph = i
                                  
                                        

                                        
                        #after group orders are reassigned, sort the actual data
                        self.sortByGroupOrder()
                        success = True
                except ValueError:
                        success = False
                
                return success


        def shiftGroupUp(self, index):
                """Shifts the selected group further up in the graph."""
                success = False
                #check if the specified group is already in the last position
                if (index + 1) < len(self.admixGroupList[self.groupColIndex]): 
                    prevIndex = index
                    nextIndex = index + 1

                    tempGroup = self.admixGroupList[self.groupColIndex][prevIndex]
                    self.admixGroupList[self.groupColIndex][prevIndex] = self.admixGroupList[self.groupColIndex][nextIndex]
                    self.admixGroupList[self.groupColIndex][nextIndex] = tempGroup

                    tempOrder = self.admixGroupList[self.groupColIndex][prevIndex].orderInGraph
                    self.admixGroupList[self.groupColIndex][prevIndex].orderInGraph = self.admixGroupList[self.groupColIndex][nextIndex].orderInGraph
                    self.admixGroupList[self.groupColIndex][nextIndex].orderInGraph = tempOrder
                    
                    self.sortByGroupOrder()
                    success = True

                return success

        def shiftGroupDown(self, index):
                """Shifts the selected group further down in the graph."""
                success = False
                #check if the specified group is already in the first position
                if (index > 0): 
                    currIndex = index
                    previousIndex = index - 1

                    tempGroup = self.admixGroupList[self.groupColIndex][currIndex]
                    self.admixGroupList[self.groupColIndex][currIndex] = self.admixGroupList[self.groupColIndex][previousIndex]
                    self.admixGroupList[self.groupColIndex][previousIndex] = tempGroup

                    tempOrder = self.admixGroupList[self.groupColIndex][currIndex].orderInGraph
                    self.admixGroupList[self.groupColIndex][currIndex].orderInGraph = self.admixGroupList[self.groupColIndex][previousIndex].orderInGraph
                    self.admixGroupList[self.groupColIndex][previousIndex].orderInGraph = tempOrder

                    self.sortByGroupOrder()
                    success = True

                return success
		           
        
        #sorts least to most dominant
        def sortByAncestryDominanceV2(self, mostToLeast):
                """Sorts admix data columns by dominant ancestry."""
                success = False
                try:
                        for i in range(len(self.ancestryList) - 1):
                                for j in range(i, len(self.ancestryList)):

                                        if mostToLeast:
                                                if(self.ancestryList[i].dominance < self.ancestryList[j].dominance):
                                                        tempAncestry = self.ancestryList[i]
                                                        self.ancestryList[i] = self.ancestryList[j]
                                                        self.ancestryList[j] = tempAncestry

                                                        tempOrder = self.ancestryList[i].orderInGraph
                                                        self.ancestryList[i].orderInGraph = self.ancestryList[j].orderInGraph
                                                        self.ancestryList[j].orderInGraph = tempOrder
                                        else:
                                                if(self.ancestryList[i].dominance > self.ancestryList[j].dominance):
                                                        tempAncestry = self.ancestryList[i]
                                                        self.ancestryList[i] = self.ancestryList[j]
                                                        self.ancestryList[j] = tempAncestry

                                                        tempOrder = self.ancestryList[i].orderInGraph
                                                        self.ancestryList[i].orderInGraph = self.ancestryList[j].orderInGraph
                                                        self.ancestryList[j].orderInGraph = tempOrder
                        success = True
                except ValueError:
                        success = False
                return success


                
                

        def shiftAncestryUp(self, index):
                """Shifts the selected ancestry further up in the graph."""
                success = False
                #check if the specified ancestry is already in the last position
                if (index + 1) < len(self.ancestryList): 
                    prevIndex = index
                    nextIndex = index + 1

                    tempGroup = self.ancestryList[prevIndex]
                    self.ancestryList[prevIndex] = self.ancestryList[nextIndex]
                    self.ancestryList[nextIndex] = tempGroup

                    tempOrder = self.ancestryList[prevIndex].orderInGraph
                    self.ancestryList[prevIndex].orderInGraph = self.ancestryList[nextIndex].orderInGraph
                    self.ancestryList[nextIndex].orderInGraph = tempOrder
                    
                    success = True

                return success

        def shiftAncestryDown(self, index):
                """Shifts the selected ancestry further down in the graph."""
                success = False
                #check if the specified ancestry is already in the first position
                if (index > 0): 
                    currIndex = index
                    previousIndex = index - 1

                    tempGroup = self.ancestryList[currIndex]
                    self.ancestryList[currIndex] = self.ancestryList[previousIndex]
                    self.ancestryList[previousIndex] = tempGroup
                    
                    tempOrder = self.ancestryList[currIndex].orderInGraph
                    self.ancestryList[currIndex].orderInGraph = self.ancestryList[previousIndex].orderInGraph
                    self.ancestryList[previousIndex].orderInGraph = tempOrder

                    success = True

                return success


                
        def findGroupPositions(self, pplList, groupIndex):
                """Finds where each group begins in the list so that it's known where to place group labels on the graphs (pheno dependent)."""
                #the first column contains group names and the other the positions of the corresponding group
                posList = [[], []] #groupName-position pair
                currGroup = ""
                
                for pIndex in range(len(pplList)):
                        if (pplList[pIndex].groups[groupIndex] != currGroup): #if the next group has been found
                                currGroup = pplList[pIndex].groups[groupIndex]
                                posList[0].append(currGroup)
                                posList[1].append(pIndex)

                return posList
        

        #plot the graph
        def plotGraph(self, isFirstTime, phenoCol= None):
                """Plots the graph onto a figure"""
                if phenoCol is not None:
                        self.groupColIndex = phenoCol - 3
                
                #group management stuff
                
                if phenoCol is not None:
                        if isFirstTime:
                            self.sortByGroupAlphaV2()

                
                indList = copy.deepcopy(self.individualList) #clone the individuals list because we need to scale the values and hide some people

                personList = []
                for person in indList:
                        if person.hidden is False:
                                personList.append(person)
                
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

                
                #format data for plotting functions
                rotatedList = np.column_stack(processedAdmixList) #stack each individual's ancestry data as a single column
                
                #add columns to the individuals_y list by specified ancestry order
                individuals_y = [None] * self.numAncestries

                #seems to work, wrap head around later
                for i in range(len(self.ancestryList)):
                        individuals_y[i] = rotatedList[self.ancestryList[i].orderInData]
                        #individuals_y[self.ancestryList[i].orderInData] = rotatedList[self.ancestryList[i].orderInData]
                

                #list containing label info for the x-axis
                if phenoCol is not None:        
                        tickList = self.findGroupPositions(personList, self.groupColIndex)
                
                

                #test colour list
                ancestryColours = [None] * self.numAncestries
                for i in range(0, self.numAncestries):
                        #replace i index in ancestryList with index of ancestry order
                        #ancestryColours.append(self.ancestryList[self.ancestryOrder[i]].colour)
                        ancestryColours[i] = self.ancestryList[i].colour
                        #ancestryColours[self.ancestryList[i].orderInData] = self.ancestryList[self.ancestryList[i].orderInData].colour #this makes some more sense?
                
                        
                self._fig = self._nb.add(self._name)
                self._ax = self._fig.gca()
                self._ax.stackplot(individuals_x, individuals_y, colors = ancestryColours)

                if phenoCol is not None:
                        self._ax.set_xticks(tickList[1],minor = False)
                        self._ax.set_xticklabels(tickList[0],minor=False)
                DataHolder.Figures.update({self._name:self._fig})
                DataHolder.Graphs.update({self._name:self})
                self._ax.set_title(self._name)
                        
               
                
               
		#plt.show()

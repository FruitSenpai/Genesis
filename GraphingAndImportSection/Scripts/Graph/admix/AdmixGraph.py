#This graph contains information and functions which control the properties of an admix graph

import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import interactive

from Graph.admix.AdmixIndividual import AdmixIndividual

class AdmixGraph:

        #list of all individuals represented in graph
        individualList = []

        #2D list of all groups represented in graph (groups are seperated into their respective columns)
        groupList = []

        def __init__(self, individualData, famData, phenoData= None):

                self.individualList = []
                self.groupList = []

                if phenoData is None:
                        self.addIndividuals( individualData, famData)
                        print("no phenotype data")
                else:
                        self.addIndividuals(individualData, famData)

                        #set up secondary group lists for each secondary column in phe file
                        for i in range(2, len(phenoData)):
                                self.groupList.append([])

                        self.addGroups(phenoData)

        #create individual objects with id names as well as their admix data
        def addIndividuals(self, individualData, famData):
                for i in range(len(individualData)):
                                person = AdmixIndividual(famData[i][0], famData[i][1], individualData[i])
                                self.individualList.append(person)

        #for each individual, find their entry in the phenotype data and assign them their corresponding groups
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


        #if the specified group name doesn't yet exist in the specified column in the global group list, add the group
        def checkGroupExistence(self, listColIndex, groupName):
                exist = False

                for group in self.groupList[listColIndex]:
                        if (group == groupName):
                                exist = True
                                break

                if(exist == False):
                        self.groupList[listColIndex].append(groupName)

        #sorts individuals by group alphabetical order (currently does reverse alphabetical order)
        def sortByGroupAlpha(self, listToSort, groupCol):
                listToSort.sort(key=lambda person: person.groups[groupCol], reverse = True)

        #sorts individuals by group dominance (most dominant to least dominant group)
        def sortByGroupDominance(self, listToSort, groupCol):

                #stores the dominance values for each group
                dominanceDic = {}



                #initialize dominance list values
                for group in self.groupList[groupCol]:
                        dominanceDic[group] = 0


                #find dominance of each individual
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

        #finds where each group begins in the list so that it's known where to place group labels on the graphs
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

        #plot the graph
        def plotGraph(self, phenoCol= None):
                
                
                personList = self.individualList[:] #clone the individuals list because we need to scale the values

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


                #group management stuff
                if phenoCol is not None:
                        #self.sortByGroupAlpha(personList, phenoCol - 3) #sort the list by group alphabetical order
                        self.sortByGroupDominance(personList, phenoCol - 3) #sort the list by group dominance

                #now render the graph
                individuals_x = np.arange(len(personList))

                #processed data to plot
                processedAdmixList = []

                for i in range(len(personList)):
                        processedAdmixList.append(personList[i].admixData)

                #before stacking values, sort by dominance
                self.sortByAncestryDominance(processedAdmixList)

                #format data for plotting functions
                individuals_y = np.column_stack(processedAdmixList) #stack each individual's ancestry data as a single column

                if phenoCol is not None:
                        #list containing label info for the x-axis
                        tickList = self.findGroupPositions(personList, phenoCol - 3)


                #plot on the stack plot
                fig, ax = plt.subplots()
                ax.stackplot(individuals_x, individuals_y)
                if phenoCol is not None:
                        plt.xticks(tickList[1], tickList[0])
                ##interactive(True)
                ##plt.show()
                return fig

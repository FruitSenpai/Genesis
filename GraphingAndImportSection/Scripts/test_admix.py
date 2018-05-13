import unittest
import numpy as np
from FileManagement.FileImporter import FileImporter
from Graph.admix import AdmixGraph

class test_admix(unittest.TestCase):

	def setUp(self):
		self.FI = FileImporter()
		admixData = self.getAdmixData('Data/small.Q.4')
		famData = self.getFamData('Data/small.fam')
		pheData = self.getPhenoData('Data/small.phe')

		self.graph = AdmixGraph.AdmixGraph(admixData, famData, None, "graph", phenoData = pheData)
		self.graph.groupColIndex = 2

	def tearDown(self):
		pass
		
	def test_ShiftGroupUp(self):
		
		#more than one group in column

		#test that group shifts up
		group = self.graph.admixGroupList[self.graph.groupColIndex][0]
		self.graph.shiftGroupUp(0)
		self.assertEqual(group, self.graph.admixGroupList[self.graph.groupColIndex][1])

		#test that group stays where it is if it's the last group
		lastIndex = len(self.graph.admixGroupList[self.graph.groupColIndex]) - 1
		group = self.graph.admixGroupList[self.graph.groupColIndex][lastIndex]
		self.graph.shiftGroupUp(lastIndex)
		self.assertEqual(group, self.graph.admixGroupList[self.graph.groupColIndex][lastIndex])
		
		#one group in column
		#check group stays in place if only group
		
		self.graph.groupColIndex = 0
		group = self.graph.admixGroupList[0][0]
		self.graph.shiftGroupUp(0)
		self.assertEqual(group, self.graph.admixGroupList[0][0])
		self.graph.groupColIndex = 2

	def test_ShiftGroupDown(self):

		#more than one group in column
		lastIndex = len(self.graph.admixGroupList[self.graph.groupColIndex]) - 1

		#test that group shifts down
		group = self.graph.admixGroupList[self.graph.groupColIndex][0]
		self.graph.shiftGroupUp(0)
		self.assertEqual(group, self.graph.admixGroupList[self.graph.groupColIndex][1])

		#test that group stays where it is if it's the first group
		group = self.graph.admixGroupList[self.graph.groupColIndex][0]
		self.graph.shiftGroupDown(lastIndex)
		self.assertEqual(group, self.graph.admixGroupList[self.graph.groupColIndex][0])
		
		#one group in column
		#check group stays in place if only group
		
		self.graph.groupColIndex = 0
		group = self.graph.admixGroupList[0][0]
		self.graph.shiftGroupUp(0)
		self.assertEqual(group, self.graph.admixGroupList[0][0])
		self.graph.groupColIndex = 2

	def test_AncestryShiftUp(self):
		
		ancestry = self.graph.ancestryList[0]
		self.graph.shiftAncestryUp(0)
		self.assertEqual(ancestry, self.graph.ancestryList[1])
		
		#test that last ancestry doesn't get shifted up
		lastIndex = len(self.graph.ancestryList) - 1
		ancestry = self.graph.ancestryList[lastIndex]
		self.graph.shiftAncestryUp(lastIndex)
		self.assertEqual(ancestry, self.graph.ancestryList[lastIndex])

	def test_AncestryShiftDown(self):

		ancestry = self.graph.ancestryList[0]
		self.graph.shiftAncestryDown(0)
		self.assertEqual(ancestry, self.graph.ancestryList[0])
		
		#test that first ancestry doesn't get shifted down
		ancestry = self.graph.ancestryList[0]
		self.graph.shiftAncestryDown(0)
		self.assertEqual(ancestry, self.graph.ancestryList[0])
	
	def test_SortByGroupDominance(self):
		#tests that it sorts most to least
		self.assertIs(self.graph.sortByGroupDominanceV2(True), True)

		#tests that it sorst least to most
		self.assertIs(self.graph.sortByGroupDominanceV2(False), True)

	def test_SortByAncestryDominance(self):
		#tests that it sorts most to least
		self.assertIs(self.graph.sortByAncestryDominanceV2(True), True)

		#tests that it sorst least to most
		self.assertIs(self.graph.sortByAncestryDominanceV2(False), True)

	def getAdmixData(self, admixFilePath):
		admixData = []
		admixFile = open(admixFilePath, "r")

		for line in admixFile:
			admixData.append(np.fromstring(line, dtype= float, sep="  "))

		admixFile.close()
		return admixData

	def getFamData(self, famFilePath):
		famData = []
		famFile = open(famFilePath, "r")

		for line in famFile:
			famData.append(line.split())
			#famData.append(np.fromstring(line, sep="  "))

		famFile.close()

		return famData

	def getPhenoData(self, phenoFilePath):
		phenoData = []
		phenoFile = open(phenoFilePath, "r")
		
		for line in phenoFile:
			phenoData.append(line.split())
			#phenoData.append(np.fromstring(line, sep="  "))
		
		phenoFile.close()
		return phenoData

if __name__ == '__main__':
    unittest.main()

	

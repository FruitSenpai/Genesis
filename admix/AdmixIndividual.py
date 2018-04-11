class AdmixIndividual:
	id1 = "id1"
	id2 = "id2"
	admixData = []
	groups = []

	def __init__(self, id1, id2, admixData):
		self.id1 = id1
		self.id2 = id2
		self.admixData = admixData
		self.groups = []

	def addGroup(self, groupName):
		self.groups.append(groupName)
	

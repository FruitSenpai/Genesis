#contains information about admix individuals

class AdmixIndividual:
	
	#the two id's which make a key which uniquely identifies the individual
	id1 = "id1"
	id2 = "id2"
	
	#list of the individual's ancestry points
	admixData = []
	
	#list of all groups this individual belongs to 
	groups = [] 

	def __init__(self, id1, id2, admixData):
		self.id1 = id1
		self.id2 = id2
		self.admixData = admixData
		self.groups = []
	
	#add group name to group list
	def addGroup(self, groupName):
		self.groups.append(groupName)
	

class AdmixGroup:
	name = ""
	orderInGraph = 0
	dominance = 1

	def __init__(self, name, order):
		self.name = name
		self.orderInGraph = order
		self.dominance = 1 #initialize to 1 because the initialization of this group implies that at least one individual exists in this group

	def setOrder(self, order):
		self.orderInGraph = order

	def setDominance(self, dom):
		self.dominance = dom

class AdmixGroup:
	"""Stores Group attributes as well as all individuals belonging to the group."""
	name = ""
	orderInGraph = 0
	dominance = 1

	def __init__(self, name, order):
		"""Initializes an AdmixGroup object along with its properties."""
		self.name = name
		self.orderInGraph = order
		self.dominance = 1 #initialize to 1 because the initialization of this group implies that at least one individual exists in this group
		self.individuals = [] #list of individuals belonging to this group
		self.hidden = False

	def setOrder(self, order):
		"""Set the order of appearance of this group in the graph."""
		self.orderInGraph = order

	def setDominance(self, dom):
		"""Set the dominance(population) of this group."""
		self.dominance = dom

	def setGroupHidden(self, hide):
		"""Set the visibility of this group and its individuals"""
		self.hidden = hide
		for person in self.individuals:
			person.setHidden(hide)

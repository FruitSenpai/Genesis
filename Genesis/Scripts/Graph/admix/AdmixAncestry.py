class AdmixAncestry:
	"""Stores the properties of the ancestry."""
	colour = "red"
	dominance = 0
	orderInData = 0

	def __init__(self, name, orderData, orderGraph, col):
		"""Initializes an AdmixAncestry object along with its properties."""
		self.name = name
		self.colour = col
		self.dominance = 0
		self.orderInData = orderData #order of this ancestry in the admix data (never changes)
		self.orderInGraph = orderGraph #order of this ancestry in the graph

	def setColour(self, col):
		"""Sets the colour of this ancestry."""
		self.colour = col

	def setDominance(self, dom):
		"""Sets the dominance of this ancestry."""
		self.dominance = dom

	def setOrder(self, order):
		"""Sets the order of this ancestry in the graph."""
		self.orderInData = order

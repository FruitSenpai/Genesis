class AdmixAncestry:

	colour = "red"
	dominance = 0
	orderInData = 0

	def __init__(self, order, col):
		self.colour = col
		self.dominance = 0
		self.orderInData = order

	def setColour(self, col):
		self.colour = col

	def setDominance(self, dom):
		self.dominance = dom

	def setOrder(self, order):
		self.orderInData = order

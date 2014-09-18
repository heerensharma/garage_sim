'''
This simple class is created to contain the information of a slot.
It contains primarily if a slot is occupied or not and query slot ID.
'''

class Slot(object):
	
	def __init__(self,slot_id):
		self.slot_id = slot_id
		self.occupied = False
		# self.occupant = None

	def getSlotID(self):
		return self.slot_id

	def setOccupied(self):
		self.occupied = True

	def setUnOccupied(self):
		self.occupied = False

	def getOccupied(self):
		return self.occupied
		
	# def getOccupantDetails(self):
	# 	return self.occupant

	# def setOccupantDetails(self,vehicle_details):
	# 	self.occupant = vehicle_details

#Vehicle class is defined

class Vehicle(object):
	
	def __init__(self,id,vtype):
		self.vehicle_type = vtype
		self.vehicle_id = id


	def getVehicleID(self,):
		return self.vehicle_id

	def getVehicleType(self,):
		return self.vehicle_type


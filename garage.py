from level import Level
import random
from vehicle import Vehicle
'''
This is the main class for Garage 
Here are all the prime methods to stimulate various actions of Garage System.
And Interact with Level class which contains the information about the Level of 
a Garage.
'''

class Garage(object):

	def __init__(self,init_levels=2, init_slots=10):
		self.levels = [Level(levelId,int(init_slots)) for levelId in range(0,int(init_levels))]
		self.vehicle_dict=dict()

	#add new Level to the Garage
	def addLevel(self,init_slots=10):
		self.levels.append(Level(len(self.levels),int(init_slots)))
		return "New Level with ID %d is added with slots %d \n" % (len(self.levels)-1,int(init_slots))


	#add more slots to an existing level
	def addSlotstoLevel(self,levelId,num_slots):
		if int(levelId) not in [level.getLevelID() for level in self.levels]:
			return "This level ID already exist. Please choose another ID.\n"
		for level in self.levels:
			if level.getLevelID() == levelId:
				level.addSlots(int(num_slots))
		return "Slots have been added successfully\n"
		

	#This method will show Levels and their respective total number of slots
	def getGarageInfo(self):
		output=""
		for level in self.levels:
			output+="Level "+str(level.getLevelID())+": "+"Total Slots: "+str(level.getTotalSlots())+"\n"
		return output

	#This returns the total number of free slots in garage
	def queryFreeSlots(self):
		total_free_slots=0
		for level in self.levels:
			total_num = level.getFreeSlots()
			total_free_slots+=total_num
		return total_free_slots


	#This method is parking the entered vehicle ID and throwing unsuccessful message when 
	#there are no more spaces available
	def parkVehicle(self,vehicleID,vehicle_type):
		if vehicleID in self.vehicle_dict.keys():
			return "Vehicle ID already parked. Please check vehicle ID again.\n"

		vehicle_obj = Vehicle(vehicleID,vehicle_type)
		parked=False
		for level in self.levels:
			if level.getFreeSlots() != 0: 
				parked = True
				selected_level = level
				self.vehicle_dict[vehicleID] = selected_level
				selected_level.occupySlot(vehicle_obj)
				break

		if not parked:
			return "No empty places. Please come again later. \n"				
		else:
			return "Vehicle with ID: %s is successfully parked \n" % vehicleID		


	#unpark an existing vehicle
	def unParkVehicle(self,vehicleID):
		try:
			parkedLevel = self.vehicle_dict[vehicleID]
		except KeyError:
			return "Vehicle ID doesn't found. Please check vehicle ID again \n"
		parkedLevel.leaveSlot(vehicleID)
		self.vehicle_dict.pop(vehicleID)
		return "Vehicle with ID: %s successfully unparked\n" % vehicleID

	#method to query a spcific vehicle
	def queryVehicle(self,vehicleID):
		try:
			levelID= self.vehicle_dict[vehicleID].getLevelID()
		except KeyError:
			return -1,-1 
		slot_num = self.vehicle_dict[vehicleID].getVehicleInfo(vehicleID)
		return levelID, slot_num

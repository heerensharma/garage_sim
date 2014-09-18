from slot import Slot
# import Queue
import random


'''
This class contains the information regarding the specific level.
It comprises adding new slots the levels, query the total number of free slots,
Occupy a free slot, leave an occupied slot, 
and if a vehicle is present at a particular then delegate that information. 
'''

class Level(object):

	def __init__(self,level_id,slots=10):
		self.level_id=level_id
		self.totalslots=slots	
		self.slotsList = [Slot(i) for i in range(0,slots)]
		self.free_slots_queue = [slot.getSlotID() for slot in self.slotsList]
		self.vehicle_dict = dict()

	def getFreeSlots(self):
		# temp=0
		# for slot in self.slotsList:
		# 	if not slot.getOccupied():
		# 		temp+=1
		# return temp
		return len(self.free_slots_queue)	
	
	def getTotalSlots(self):
		return len(self.slotsList)

	def getLevelID(self):
		return self.level_id

	def addSlots(self,new_slots):
		self.slotsList+= [Slot(i) for i in range(self.totalslots,self.totalslots+new_slots)] 
		self.free_slots_queue+=[i for i in range(self.totalslots,self.totalslots+new_slots)]
		self.totalslots += new_slots
	
	def occupySlot(self,vehicle_details):
		random_spot = random.choice(self.free_slots_queue)
		self.vehicle_dict[vehicle_details.getVehicleID()] = random_spot
		self.free_slots_queue.remove(random_spot)
		# print self.free_slots_queue
		self.slotsList[random_spot].setOccupied()
	
	def leaveSlot(self,vehicle_id):
		self.free_slots_queue.append(self.vehicle_dict[vehicle_id])
		# print self.free_slots_queue
		self.slotsList[self.vehicle_dict[vehicle_id]].setUnOccupied()
		self.vehicle_dict.pop(vehicle_id, None)

	def getVehicleInfo(self,vehicle_id):
		return self.vehicle_dict[vehicle_id]




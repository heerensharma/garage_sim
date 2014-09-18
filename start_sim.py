from garage import Garage
import curses
import shelve

'''
This is primarily the console application script.
It gives the user different actions to perform.
Objects are saved in-memory.
This is really basic approach.
In real time solution, a standardized schema is required to be used.
Options are self explanatory and takes valid input from users.
'''


#this method is for the first time instantiation of the this simulation program
def initGarageState(screen,db):
	try:
		garage_obj=db["Garage"]
	except KeyError:
		screen.addstr("This is first time application is getting used \n")
		screen.addstr("Please enter the initial number of levels\n")
		while True:
			try:
				initial_levels = int(screen.getstr())
				break
			except ValueError:
				screen.addstr("Please enter valid value for Initial number of levels\n")
		screen.addstr("Please enter Initial number of slots\n")
		while True:
			try:
				initial_slots = int(screen.getstr())
				break
			except ValueError:
				screen.addstr("Please enter valid value for Initial number of slots\n")

		garage_obj = Garage(init_levels=initial_levels, init_slots=initial_slots)
		db["Garage"] = garage_obj
	return garage_obj


#this method is for the clearing of the screen after every user query
#It helps to better visualize the efforts of each input
def clearScreen(screen):
	event = screen.getch()
	if event == curses.KEY_ENTER or event == curses.KEY_DOWN:
		print "Fine"
	screen.clear()




screen = curses.initscr()




# curses.noecho()
curses.curs_set(0)
screen.keypad(1)

screen.addstr("Garage Application\n")
screen.addstr("==================\n")

db = shelve.open("./Persistent/garage_obj.dat")
garage_obj =initGarageState(screen,db)
screen.clear()

			
while True: 
	try:
		

		screen.addstr("Please press one of the following options to get started\n")
		screen.addstr("1. Start New Garage\n")
		screen.addstr("2. Add New Parking Level\n")
		screen.addstr("3. Add New Parking Slots at a Level\n")
		screen.addstr("4. Enter a vehicle in garage\n")
		screen.addstr("5. Exit a vehicle from garage\n")
		screen.addstr("6. Query a Vehicle\n")
		screen.addstr("7. Query Total Number of free parking slots\n")
		screen.addstr("8. Get Garage Info\n")
		screen.addstr("9. Exit from program\n")
		# screen.addstr(temp)

		input_char = chr(screen.getch())

		if input_char == '1':
			
			screen.addstr("Please enter the initial number of levels\n")
			while True:
				try:
					initial_levels = int(screen.getstr())
					break
				except ValueError:
					screen.addstr("Please enter valid value for Initial number of levels\n")
			screen.addstr("Please enter Initial number of slots\n")
			while True:
				try:
					initial_slots = int(screen.getstr())
					break
				except ValueError:
					screen.addstr("Please enter valid value for Initial number of slots\n")

			garage_obj = Garage(init_levels=initial_levels, init_slots=initial_slots)
			db["Garage"] = garage_obj
			clearScreen(screen)

		if input_char == '2':
			screen.addstr("Please enter Initial number of slots for new Level\n")
			while True:
				try:
					initial_slots = int(screen.getstr())
					break
				except ValueError:
					screen.addstr("Please enter valid value for Initial number of slots\n")
				
			screen.addstr(garage_obj.addLevel(init_slots=initial_slots))
			db["Garage"] = garage_obj
			clearScreen(screen)
							

		if input_char == '3':
			screen.addstr("Select the Level to add new slots\n")
			level_num = int(screen.getstr())
			temp_str = "Please enter number of slots to add to Level: "+str(level_num)+"\n"
			screen.addstr(temp_str)
			slots_to_add = int(screen.getstr())
			screen.addstr(garage_obj.addSlotstoLevel(level_num,slots_to_add))
			db["Garage"] = garage_obj
			clearScreen(screen)
							

		if input_char == '4':
			screen.addstr("Please enter the vehicle ID to park\n")
			vehicle_id = screen.getstr()
			screen.addstr("Please enter vehicle type {car, bike}\n")
			vehicle_type = screen.getstr()
			screen.addstr(garage_obj.parkVehicle(vehicle_id,vehicle_type))
			db["Garage"] = garage_obj
			clearScreen(screen)
							

		if input_char == '5':
			screen.addstr("Please enter the vehicle ID to unpark\n")
			vehicle_id = screen.getstr()
			screen.addstr(garage_obj.unParkVehicle(vehicle_id))
			db["Garage"] = garage_obj
			clearScreen(screen)
							

		if input_char == '6':
			screen.addstr("Please enter the vehicle ID to query\n")
			vehicle_id = screen.getstr()
			levelid, slotnum = garage_obj.queryVehicle(vehicle_id)
			if levelid == -1 and slotnum == -1:
				screen.addstr("This Vehicle ID is not in database. Please check again \n")
			else:
				temp_str="Vehicle present at Level: "+str(levelid)+" and Slot Number: "+str(slotnum)+"\n"
				screen.addstr(temp_str)
			db["Garage"] = garage_obj
			clearScreen(screen)
							

		if input_char == '7':
			temp_str = "Total number of free parking slots = "+ str(garage_obj.queryFreeSlots())+"\n"
			screen.addstr(temp_str)
			# screen.addstr(temp_str)
			db["Garage"] = garage_obj
			clearScreen(screen)
							

		if input_char == '8':
			screen.addstr(garage_obj.getGarageInfo())
			db["Garage"] = garage_obj
			clearScreen(screen)
							

		if input_char == '9':
			# db = shelve.open("./Persistent/garage_obj.dat")
			db["Garage"] = garage_obj
			db.close()
			break
	
	#This exception clause will the save the current state of garage even when Keyboard 
	#interrupt occurs or System Exits unexpectedly
	except (KeyboardInterrupt, SystemExit):
		db["Garage"] = garage_obj
		db.close()
	
	except Exception as e:
		screen.clear()
		db["Garage"] = garage_obj
		# db.close()
		continue

curses.endwin()



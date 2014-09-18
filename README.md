Garage Simulation
==========

This is a very basic console application. An in memory database (persistent objects) is used for simplicity and instead of providing GUI, console application is used (it's a new experience for me). For the general information, there is a console that will be open up with several numbered options and user can press the respective options to query the different things. In addition, if someone likes to add new levels or slots to a level, respective queries will be asked on the moment. 


##Start Simulation##
As this application is developed in python, all is required is a python console.
To launch the application, please enter the following command in console (shell/bash)

```
$ cd garage_sim/
$ python start_sim.py
```



##Known Issues##
1. This assignment can be done with several different approaches and software architectures. But simplicity for the proof of concept is kept in mind while doing this assignment. Approach taken in completed object oriented. Hence, for different entities of system, different classes are created. 

2. Takin the other simple approach, instead of creating separate database and query it, all the information is stored in form of persistent object (in this case of Garage class object). 

3. This is developed under Debain-based OS. Hence apart from this, please let author know if there is some problems associated with other OS. 

4. To demonstrate the user input validation is implemented in first two options shown in application. This can be enforced in other fields (like typing valid integer strings) as well.   
 

##Developer's Section##

This program is consisted of 5 python scripts and 1 folder named **Persistent**. In this folder the objects are saved and gathered at the start of the simulation. Whenever, the program is instantiated for the very first time, then only the user will asked to fill up levels and number of slots at each level. Apart from this, information about garage state will be taken from this memory mapped objects. Following are brief description of all python files: 

1. *garage.py*: This is core file. It represents the state of the whole Garage and moreover it composed of different methods to query specific details about Garage like parking a vehicle, querying an already parked vehicle, add new levels to garage, add new slots to garage, total number of free slots in Garage, etc. It interact closely with Level class which is described in next point. Object of this class is stored in form of persistent object. 
2. *level.py*: As name suggests, it represents the state of a level in Garage. It includes level ID, number of free slots in garage, information of parked vehicle, slots in information. Whenever a car is requested to park in a level and if level has free space, then it chooses a random free spot and gives back parking information back to Garage class.
3. *slot.py*: It represent the information about slot. Whether it is occupied or unoccupied and slot ID.
4. *vehicle.py*: It represent vehicle information. There are primarily two fields: Vehicle ID and type of Vehicle.
5. *start_sim.py*: This is main console class. It instantiats a new console session and gives user variety of options to simulate garage. Apart from this, it takes user input and reflect the changes of state of garage.






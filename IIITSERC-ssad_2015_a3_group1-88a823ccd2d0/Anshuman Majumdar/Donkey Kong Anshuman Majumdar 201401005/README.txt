-------------------------------------------------------
| DONKEY KONG - made by Anshuman Majumdar (201401005) |
-------------------------------------------------------

GAME Regulations :

	- To start the game type "python main.py" in the Terminal
	- Objective of the game is to rescue the Queen(Mozilla Thunderbird)
	- Player(Google Chrome) can Move, Jump or Climb the Stairs(Batman Tunnel)
	- Getting into contact with the Fireballs released by the Donkey(Facebook) will get the Player killed
	- Player has only 3 extra lives
	- Each coin is worth 5 points and penalty for a death is -25

CONTROL Mappings :

	- Move Right      :    Right Arrow Key (->)
	- Move Left       :    Left Arrow Key (<-)
	- Move Up         :    Up Arrow Key (^)
	- Move Down       :    Down Arrow Key (v)
	- Jump            :    Space Bar (._.)
	- Quit            :    Q key (q)

CLASSES Description :

	- There is a parent class named Sprite in baseSprites.py Module and all the live objects in the game are inherited from it
	- There are three different Modules named prince.py, fireball.py and level[1,2,3].py which respectively describe the Prince, 
	  Fireballs and walls/stairs Level Classes
	- The Level classes in level[1,2,3].py modules are inherited from a Class Level contained in the baseLevels.py Module and
	  they describe the Walls and the Stairs

OBJECT Movements :

	- The object movements are implemented using velocities
	- The velocities increase in the direction of which the key is pressed
	- A gravity function is implemented in the Prince and Fireballs Classes that simulates gravity while jumping

OOP Concepts :

	- Modularity -- The entire source code is divied into separate modules with each module having its own functionality
	- Inheritance -- There are Superclasses like Sprite and Level in baseSprites.p and baseLevels.py respectively which inherit
	                 other classes like Prince, Fireballs and levels in other Modules
	- Polymorphisn -- Methods like update, movement etc. have been redefined in the Subclasses according to the Class's needs
	- Encapsulation -- Protection in given to static and constant variables throughout the Modules



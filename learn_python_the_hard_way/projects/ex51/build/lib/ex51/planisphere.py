from nose.tools import *

class Room(object):
    # Khởi tạo giá trị các biến, path để default là {} chứ không truyền vào
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths= {}
        
    def go(self, direction):
        return self.paths.get(direction, None)          # trả về value tương ứng vơi key = 'direction'
    
    def add_paths(self, paths):
        self.paths.update(paths)
        
central_corridor = Room("Central corridor",
"""
The Gothons of Planet Percal #25 have invaded destroyed
your ship and destroyed you entire crew. You are the last
surviving member and you last mission is get the neutron
destruct bomb the ship up after getting into an escape 
pod\n
You're running down the central corridor to the 
Weapons Armory when a Gothons jumps out, red saaly skin,
dark grimy teeth, and evil clown costume flowing around
his hate filled body. He's blocking the door to the Armory
and about to pull a weapon to blast you.""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be diding. It's dead quiet, too quiet. 
You stand up and run to the far side of the room and find the neutron
bomb in this container. There's a keypad lock on the box and you need
the code to get the bomb out. If you get the code wrong 10 times then
the lock closes forever and you can't get the bomb. The code is 3 digits.""")

the_bridge = Room("The Bridge",
"""
You burse onto the Bridge with the netron destruct bomb 
under your arm and surprise 5 Gothons who are trying to 
take control of the ship. Each of them has an even uglier
clown costume than the last. They haven't pulled their weapons 
out yet, as they see tehe active bomb under your arm and 
don't want to set it off.""")

escape_pod = Room("Escape Pod",
"""
You rush thorugh the ship desperately trying to make it to
the escape pod  before the whole ship explodes. It seems 
like hardly any Gothons are on the ship, so your run is clear
of interference. YOu get to the chamber with the escape pods,
and now need to pick one to take. Some of them could be damaged
but you don't have time to look. There's 5 poss, 
which one do you take?""")

the_end_winner = Room("The End",
"""
You jump into pod {guess} and hit the eject button.
The pod easily slides out into space heading to 
the planet below. AS it flies to the planet., you 
look back and see your ship implliide then explode 
like a bright star, taking out he Gothon ship at the 
same time. You won! """)

the_end_loser = Room("The End",
"""
You jump into pod {guess} and hit the eject button. 
The pod escapes out intot the void of space, then 
implodes as the hull ruptures, crushing you body 
into jam jelly.
""")

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
    })

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod})
    
laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
    })
    
central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
    })
    
START = 'central_corridor'

def load_room(name):
    """
    There is a potential security problem here.
    Who gets to set name? Can tha expose a variable?
    """
    return globals().get(name)
    
def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What's a better solution than thsi globals lookup?
    """
    for key, value in globals().item():
        if value == room:
            return key
      
        
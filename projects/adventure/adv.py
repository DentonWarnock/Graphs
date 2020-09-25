from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
opposite_directions = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}

def traverse_graph():    
    # create a set for visited rooms
    visited = set()    
    # add starting room to visited
    visited.add(player.current_room)
     
    
    # while we have not visited each room
    while len(visited) < len(world.rooms):        
        current_room = player.current_room        
        
        # make list of valid exits of non visted rooms
        valid_exits = []        
        for direction in current_room.get_exits():            
            if current_room.get_room_in_direction(direction) not in visited: 
                valid_exits.append(direction)
                
        # randomize exits - creates DFS        
        random.shuffle(valid_exits)
        
        # if we have a valid exit/direction to travel
        if len(valid_exits) > 0:        
            direction = valid_exits[0]  
                      
            # travel in the random direction
            player.travel(direction)         
            
            # store new room we are now in
            new_room = player.current_room            
                    
            # add new room to visited
            visited.add(new_room)
            
            # add direction to traversal_path
            traversal_path.append(direction)   
                    
            
        # else we have been here before or we're at an end
        else:
            # travel in the opposite direction from last move
            player.travel(opposite_directions[traversal_path[-1]])
            
            # add direction to traversal_path
            traversal_path.append(opposite_directions[traversal_path[-1]])
                
    
    return traversal_path    
        
    
traversal_path = traverse_graph()


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")




#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

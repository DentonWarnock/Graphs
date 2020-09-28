from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
opposite_direction = {
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
    
    path = []
    stack = []
    
    # while we have not visited each room
    while len(visited) < len(room_graph):        
        # make list of all valid exits of non visited rooms ['n', 's']
        valid_exits = []        
        for direction in player.current_room.get_exits():            
            if player.current_room.get_room_in_direction(direction) not in visited: 
                valid_exits.append(direction)
                
        # randomize the exits - making this a DFS - however results improved without (992 vs 996)
        # random.shuffle(valid_exits)
        
        # if we have a valid exit/direction to travel
        if len(valid_exits) > 0:        
            # travel in the first direction
            direction = valid_exits[0]                     
            player.travel(direction)
            # add new current room to visited
            visited.add(player.current_room)            
            # add direction to path and stack
            path.append(direction)  
            stack.append(direction)                     
            
        # else we need to reverse directions from the stack until we find a new exit
        else:
            # get last direction from stack
            last_valid_direction = stack.pop()
            # travel in the opposite direction
            player.travel(opposite_direction[last_valid_direction])            
            # add direction to path
            path.append(opposite_direction[last_valid_direction])
        
        # continue until all rooms are visited
    
    return path    
        
    
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

from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


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

Prevroom = [None]
Directory = {'n': 's': 'e': 'w': 's': 'e', 'w', 'n'}
visit = {}
room = {}
print(room_graph[5][3])


def Options(roomID):
    choices = []
    if 'n' in room_graph[roomID][1].keys():
        choices.append('n')
    if 's' in room_graph[roomID][1].keys():
        choices.append('s)
    if 'e' in room_graph[roomID][1].keys():
        choices.appned('e')
    if 'w' in room_graph[roomID][1].keys():
        choices.append('w')
    return choices
while len(visit) < len(room_graph):
    roomID = player.current_room.id
    if roomID not in room:
        visit[roomID] = roomID
        room[roomID] = Options(roomID)

    if len(room[roomID]) < 1:
        oldroom = trackoldroom.pop()
        traversal_path.append(oldroom)
        player.travel(oldroom)

    else:
        newdirection = room[roomID].pop(0)
        traversal_path.append(newdirection)
        trackoldroom.append(dirOposite[newdirection])
        player.travel(newdirection)
    



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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

import random

# Environment with two rooms
class Environment:
    def __init__(self):
        # Room 1 and Room 2 can be 'Clean' or 'Dirty'
        self.rooms = {
            'Room1': random.choice(['Clean', 'Dirty']),
            'Room2': random.choice(['Clean', 'Dirty'])
        }
        self.agent_location = 'Room1'

    def status(self, room):
        return self.rooms[room]

    def clean(self, room):
        self.rooms[room] = 'Clean'

    def is_clean(self):
        return all(status == 'Clean' for status in self.rooms.values())

    def __str__(self):
        return f"Rooms: {self.rooms}, Agent at: {self.agent_location}"

# Simple Reflex Vacuum Agent
class VacuumAgent:
    def __init__(self):
        self.score = 0

    def perceive_and_act(self, env):
        room = env.agent_location
        status = env.status(room)

        print(f"Agent is at {room}, which is {status}")

        # Clean if dirty
        if status == 'Dirty':
            env.clean(room)
            self.score += 10
            print(f"Cleaned {room}. Score: {self.score}")
        else:
            print(f"{room} is already clean. Score: {self.score}")

        # Move to the other room (flip between Room1 and Room2)
        next_room = 'Room2' if room == 'Room1' else 'Room1'
        env.agent_location = next_room

# Simulation
env = Environment()
agent = VacuumAgent()

print("Initial Environment:")
print(env)

for _ in range(4):  # Run for 4 steps (2 full cycles between rooms)
    agent.perceive_and_act(env)
    print(env)

print(f"Final Score: {agent.score}")

from collections import deque


class Fish:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

def survivingFish(fish_list):
    stack = []
    for fish in fish_list:
        alive = True
        while alive and fish.velocity < 0 and stack and stack[-1].velocity > 0:
            top_fish = stack[-1]
            if abs(top_fish.velocity) > abs(fish.velocity):
                alive = False
            elif abs(top_fish.velocity) < abs(fish.velocity):
                stack.pop()
            else:
                stack.pop()
                alive = False
        if alive:
            stack.append(fish)
    return stack

def survivingFishLeftToRight(fish_list):
    survivors = []
    for fish in fish_list:
        while survivors and fish.velocity < 0 and survivors[-1].velocity > 0:
            top_fish = survivors[-1]
            if abs(top_fish.velocity) > abs(fish.velocity):
                fish = None
                break   
            elif abs(top_fish.velocity) < abs(fish.velocity):
                survivors.pop()
            else:
                survivors.pop()
                fish = None
                break
        if fish is not None:
            survivors.append(fish)
    return survivors

def survivingFishQueue(fish_list):
    left_queue = deque()
    right_queue = deque()

    for fish in fish_list:
        if fish.velocity > 0:
            right_queue.append(fish)
        else:
            while right_queue and right_queue[-1].velocity < abs(fish.velocity):
                right_queue.pop()
            if right_queue and right_queue[-1].velocity == abs(fish.velocity):
                right_queue.pop()
            elif not right_queue:
                left_queue.append(fish)

    return list(left_queue) + list(right_queue)

# Ví dụ sử dụng
fish_list = [Fish(0, 2), Fish(3, -1), Fish(5, 4), Fish(6, -2)]
result = survivingFish(fish_list)
print("Surviving fish:")
for fish in result:
    print(f"Position: {fish.position}, Velocity: {fish.velocity}")

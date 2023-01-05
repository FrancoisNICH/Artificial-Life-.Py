import random
import time
import uuid

class Cell:
    def __init__(self, x, y):
        self.id = uuid.uuid4()
        self.x = x
        self.y = y
        self.speed = 1
        self.direction = random.choice(["North", "South", "East", "West"])
        self.color = random.choice(["Red", "Green", "Blue"])
        self.size = random.uniform(0.5, 2)
        self.lifespan = 100
        self.hunger = 50

    def move(self, food):
        if food.x > self.x:
            self.x += self.speed
        elif food.x < self.x:
            self.x -= self.speed
        if food.y > self.y:
            self.y += self.speed
        elif food.y < self.y:
            self.y -= self.speed

    def display(self):
        print(f"ID: {self.id}")
        print(f"Position: ({self.x}, {self.y})")
        print(f"Lifespan: {self.lifespan}")
        print(f"Hunger: {self.hunger}")
        print(f"Speed: {self.speed}")
        print(f"Direction: {self.direction}")
        print(f"Color: {self.color}")
        print(f"Size: {self.size}")

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def create_food():
    x = random.uniform(-40, 40)
    y = random.uniform(-40, 40)
    return Food(x, y)

cells = [Cell(0, 0) for i in range(5)]
food = create_food()
while True:
    for cell in cells:
        cell.move(food)
        cell.display()
        cell.hunger -= 1
        cell.lifespan -= 1
        if cell.hunger <= 0 or cell.lifespan <= 0:
            cells.remove(cell)
        print()
    if not cells:
        break
    food = create_food()
    time.sleep(1)

import random

# Critter class representing a single critter
class Critter:
    def __init__(self):
        self.brain = []  # empty brain
        self.genes = []  # basic genes
        self.energy = 0  # energy level
        
    def forward(self):
        # movement behavior that allows critter to eat food
        self.energy += 1
        
    def reproduce(self):
        # create a new critter with mutated genes
        child = Critter()
        child.genes = self.genes[:]  # copy parent's genes
        child.mutate()  # mutate the child's genes
        return child
        
    def mutate(self):
        # randomly mutate genes
        for i in range(len(self.genes)):
            if random.random() < 0.1:  # 10% chance of mutation
                self.genes[i] = random.randint(0, 1)

# Simulation class to run the evolution process
class Simulation:
    def __init__(self):
        self.critters = []  # list of critters in the simulation
        
    def run(self):
        # main loop of the simulation
        while True:
            # get user input to continue the simulation
            choice = input("Press enter to continue, q to quit: ")
            if choice == "q":
                break
                
            # iterate over all critters and allow them to take actions
            for critter in self.critters:
                # random chance for a critter to perform a behavior
                if random.random() < 0.5:
                    critter.forward()
                
                # if critter has enough energy, allow it to reproduce
                if critter.energy > 5:
                    self.critters.append(critter.reproduce())
                    critter.energy = 0  # reset energy level
                    
            # display the current state of the simulation
            self.display()
            
    def display(self):
        # display the number of critters and their energy levels
        print(f"Critters: {len(self.critters)}")
        for critter in self.critters:
            print(f"Critter {self.critters.index(critter)}: {critter.energy}")
            
# main function to run the simulation
def main():
    sim = Simulation()
    
    # add starting critters to the simulation
    for i in range(5):
        sim.critters.append(Critter())
        
    sim.run()
    
# run the main function if the script is executed
if __name__ == "__main__":
    main()

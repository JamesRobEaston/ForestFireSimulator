from Forest import Forest
import time

class FireSimulator:

    #Constructor
    #Precondition(s) : display is a method that takes a Forest object as a
    #                  parameter and will be used to display the forest
    def __init__(self, givenDisplayMethod):
        self.coordinates = [0,0]
        self.display = givenDisplayMethod
    
    #Simulates a forest fire
    #Precondition(s) : getIgnitionChance and getDensity are methods that return
    #                  a double to be used for the chance that a tree will catch
    #                  on fire and for the density of the forest, respectively
    #                  incrementFire is a bool that determines which method in forest
    #                  will be used to spread the fire
    #Postcondition : returns the percentage of trees that burned down
    def simulate(self, getDensity, getIgnitionChance, incrementFire):
        self.forest = Forest()
        density = float(getDensity())
        ignitionChance = float(getIgnitionChance())
        self.forest.createForest(density)
        self.forest.ignite(ignitionChance)
        if(incrementFire):
            simulateFireSpread = self.forest.incrementFire
        else:
            simulateFireSpread = self.forest.updateFire
        self.display(self.forest)
        while(self.forest.getStillBurning()):
            coordinates = [0,0]
            while(coordinates[0] < 12):
                coordinates = simulateFireSpread(ignitionChance, coordinates)
                self.display(self.forest)
                time.sleep(1)
        numBurned = float(self.forest.getTotalNumOfTrees() - self.forest.getCurrNumOfTrees())
        percentTreesBurned = numBurned/(float(self.forest.getTotalNumOfTrees()))
        return percentTreesBurned

    #Returns forestList in forest
    def getForest(self):
        return self.forest.getForestList()
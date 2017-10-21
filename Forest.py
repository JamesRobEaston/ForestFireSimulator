import random
from Tree import Tree
from Block import Block

class Forest:
    
    #Constructor
    #forestList is a representation of the forest and holds Tree and Block objects
    #totalNumOfTrees is the total number of trees
    #currNumOfTrees is the current number of trees
    #stillBurning is true when the forest is and fire and false when it is not
    def __init__(self):
        self.forestList = []
        self.totalNumOfTrees = 0;
        self.currNumOfTrees = 0;
        self.stillBurning = True;

    #Fills the forestList with arrays of ForestObjects
    #Precondition : density is a float
    #Postcondition : forestList will be a 13x11 array of Forest objects (13 rows, 11 columns)
    def createForest(self, density):
        chance = 0.0
        density = float(density)
        for i in range(12):
            row = []
            for j in range(11):
                chance = random.random() * 100
                if(chance <= density):
                    row.append(Tree(False, False))
                    self.totalNumOfTrees += 1
                else:
                    row.append(Block())

            self.forestList.append(row)

        self.currNumOfTrees = self.totalNumOfTrees

    #Determines if a tree will catch on fire and, if so, randomly chooses a tree to light.
    #Precondition(s) : ignitionChance is a float
    #Postcondition : Either no tree will ignite or one random tree will ignite
    def ignite(self,ignitionChance):
        chance = random.random() * 100
        ignitionChance = float(ignitionChance)
        stillBurning = chance <= ignitionChance
        if stillBurning:
            #Tree at row y, column x will be ignited
            y = random.randint(0, 11)
            x = random.randint(0, 10)
            while(not isinstance(self.forestList[y][x], Tree)):
                y = random.randint(0, 11)
                x = random.randint(0, 10)       
            self.forestList[y][x].setIsOnFire(True)

    #If the object at row y, column x is a tree, ignites the tree
    #Precondition(s) : x and y are ints
    #Postcondition : If the ForestObject at row y, column x is a tree, isOnFire will be true
    def igniteCoords(self, y, x):
        x = int(x)
        y = int(y)
        if isinstance(self.forestList[y][x], Tree):
            self.forestList[y][x].setIsOnFire(True)

    #Returns forestList
    def getForestList(self):
        return self.forestList

    #Returns totalNumOfTrees
    def getTotalNumOfTrees(self):
        return self.totalNumOfTrees
    
    #Returns currNumOfTrees
    def getCurrNumOfTrees(self):
        return self.currNumOfTrees

    #Returns stillBurning
    def getStillBurning(self):
        return self.stillBurning;

    #Returns the ForestObject at row y, column x
    #Precondition(s) : x and y are ints
    #Postcondition : Will return the ForestObject at row y, column x
    def getForestObject(self, x, y):
        x = int(x)
        y  = int(y)
        return self.forestList[y][x]

    #Uses ignitionChance to determine whether fire will spread. 
    #Updates all trees, compared to incrementFire which only updates one
    #coordinates is not used, it is only necessary that it has the same number of parameters as
    #incrementFire()
    #Precondition(s) : ignitionChance is a float
    #Postcondition : All previously burning trees will be destroyed and
    #                all surrounding trees will be tested to burn
    def updateFire(self, ignitionChance, coordinates):
        ignitionChance = float(ignitionChance)
        for i in range(12):
            for j in range(11):
                if self.forestList[i][j].isOnFire:
                    self.spreadFire(ignitionChance, i, j, False)
                    
        self.stillBurning = self.determineShouldContinueBurning();
        return [13,12]
            
    #Uses ignitionChance to determine whether fire will spread. 
    #Updates one tree, compared to updateFire which updates all trees
    #Precondition(s) : ignitionChance is a float
    #                  list holds two coordinates from which incrementFire should continue burning
    #Postcondition : Any previously burning trees encountered will be destroyed and
    #                all surrounding trees up to the values returned will be tested to burn
    def incrementFire(self, ignitionChance, coordinates):
        ignitionChance = float(ignitionChance)
        for i in range(12 - coordinates[0]):
            row = coordinates[0] + i
            for j in range(11 - coordinates[1]):
                col = coordinates[1] + j
                if self.forestList[row][col].isOnFire and (not self.forestList[row][col].isDestroyed):
                    somethingHasBeenChanged = self.spreadFire(ignitionChance, row, col, True)
                    break;    
            if somethingHasBeenChanged:
                break;
        self.stillBurning = self.determineShouldContinueBurning();
        #returns a list of coordinates to continue from, if col == 10 and row == 11 then an
        #out-of-bounds value is returned
        if row == 11 and col == 10:
            return [12,11]
        return [row, col]
    
    
    #Is used to determine if the forest is still on fire
    #Precondition(s) : None
    #Postcondition(s) : True will be returned if the forest is still on fire and False if it is not
    def determineShouldContinueBurning(self):
        for i in range(12):
            for j in range(11):
                if self.forestList[i][j].isOnFire:
                    return True
        
    #Used to spread fire to the trees adjacent to the tree at forestList[y][x]
    #Precondition(s) : ignitionChance is a float
    #                  x is an int
    #                  y is an int
    #                  incrementFire is a boolean
    #Postcondition(s) : all trees adjacent to to the tree at forestList[y][x] will have an opportunity
    #                   catch on fire. If incrementFire is true, then only one tree will catch on fire
    def spreadFire(self, ignitionChance, y, x, incrementFire):
        if random.random() * 100 <= ignitionChance and  y is not 0:
            isBlock = isinstance(self.forestList[y-1][x], Block)
            isNotOnFire = not self.forestList[y-1][x].isOnFire
            isNotDestroyed = not self.forestList[y-1][x].isDestroyed
            if isNotOnFire and isNotDestroyed and (not isBlock):
                self.forestList[y-1][x].setIsOnFire(True)
                if incrementFire:
                    return False
        if random.random() * 100 <= ignitionChance and  y is not 11:
            isBlock = isinstance(self.forestList[y+1][x], Block)
            isNotOnFire = not self.forestList[y+1][x].isOnFire
            isNotDestroyed = not self.forestList[y+1][x].isDestroyed
            if isNotOnFire and isNotDestroyed and (not isBlock):
                self.forestList[y+1][x].setIsOnFire(True)
                if incrementFire:
                    return False
        if random.random() * 100 <= ignitionChance and  x is not 0:
            isBlock = isinstance(self.forestList[y][x-1], Block)
            isNotOnFire = not self.forestList[y][x-1].isOnFire
            isNotDestroyed = not self.forestList[y][x-1].isDestroyed
            if isNotOnFire and isNotDestroyed and (not isBlock):
                self.forestList[y][x-1].setIsOnFire(True)
                if incrementFire:
                    return False
        if random.random() * 100 <= ignitionChance and  x is not 10:
            isBlock = isinstance(self.forestList[y][x+1], Block)
            isNotOnFire = not self.forestList[y][x+1].isOnFire
            isNotDestroyed = not self.forestList[y][x+1].isDestroyed
            if isNotOnFire and isNotDestroyed and (not isBlock):
                self.forestList[y][x+1].setIsOnFire(True)
                if incrementFire:
                    return False
        
        self.forestList[y][x].setIsDestroyed(True)
        self.currNumOfTrees -= 1
        return False
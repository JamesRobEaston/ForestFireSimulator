from FireSimulator import FireSimulator

#Used by the simulator to determine how to display the forest
#Precondition(s): forest is a Forest object
#Postcondition(s): A string representation of the forest will be displayed
def display(forest):
    forestList = forest.getForestList()
    string = "\n|-------------------------------|\n"
    for i in range(12):
        for j in range(11):
            string += forestList[i][j].toString()
        if i != 13:
            string += "\n|-------------------------------|\n"
    print(string + "\n")
    
#Used by the simulator to determine how to receive the desired density from the user
#Precondition(s): None
#Postcondition(s): A float of the desired density will be returned 
def getDensity():
    density = float(input("What would you like the density to be?"))
    return density

#Used by the simulator to determine how to receive the desired ignition chance from the user
#Precondition(s): None
#Postcondition(s): A float of the desired ignition chance will be returned 
def getIgnitionChance():
    ignitionChance = float(input("What would you like the ignition chance to be?"))
    return ignitionChance

def main():
    fireSimulator = FireSimulator(display)
    cont = True
    while(cont):
        percentTreesBurned = fireSimulator.simulate(getDensity, getIgnitionChance, False)
        print('\nPercentage of trees burned: {:.2%}'.format(percentTreesBurned))
        cont = input("\nWould you like to simulate again? (Put True or False)\n")
        cont = cont in ['True', 'true']

if __name__ == '__main__':
    main()
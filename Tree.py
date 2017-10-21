class Tree:
    
    def __init__(self, isDestroyed, isOnFire):
        self.isDestroyed = isDestroyed
        self.isOnFire = isOnFire
    #Sets isOnFire to value of boolean
    #Precondition : boolean is a boolean
    #Postcondition : isOnFire will be equivalent to boolean
    def setIsOnFire(self, boolean):
        if not self.isDestroyed:
            boolean = bool(boolean)
            self.isOnFire = boolean

    #Sets isDestroyed to value of boolean
    #Precondition : boolean is a boolean
    #Postcondition : isDestroyed will be equivalent to boolean
    def setIsDestroyed(self, boolean):
        if self.isOnFire:
            boolean = bool(boolean)
            self.isDestroyed = boolean
            self.isOnFire = False
        
    def toString(self):
        returnString = ""
        if self.isDestroyed:
            returnString = "|D|"
        elif self.isOnFire:
            returnString ="|F|"
        else:
            returnString = "|T|"
        return returnString
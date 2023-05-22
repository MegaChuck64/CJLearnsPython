class Game:
    
    def __init__(self):
        self.state = "starting"
        self.level = 0
        self.Run()

    def Run(self):
        while(True):
            if (self.state == "starting"):
                self.StartState()
            elif (self.state == "running"):
                self.RunningState()
            elif (self.state == "exiting"):
                break
    
        print("Goodbye!")            

    def RunningState(self):
        print("Running")
        #handle game logic here
        inp = input(">>")
        if (inp == "exit"):
            self.state = "exiting"
        elif (inp == "help"):
            self.HelpState()
        elif (inp == "?"):
            self.CurrentOptions()
        elif (inp == "w"):
            self.level = self.level + 1
            print("Moved forward")
        elif (inp == "s"):
            self.level = self.level - 1
            if (self.level < 0):
                self.level = 0
            print("Moved backward")
        elif (inp == "l"):
            self.LookAround()
        elif (inp == "p"):
            self.PickUpItem()
        elif (inp == "u"):
            print("Use Item")
        elif (inp == "i"):
            print("Open Inventory")
        elif (inp == "m"):
            print("Open Map")
        elif (inp == "j"):
            print("Open Journal")
        elif (inp == "c"):
            print("Open Character Sheet")
        elif (inp == "e"):
            print("Open Equipment")
        elif (inp == "q"):
            print("Open Quest Log")
        elif (inp == "t"):
            print("Talk to NPC")
        elif (inp == "r"):
            print("Rest")
        elif (inp == "f"):
            print("Fight")            
        else:
            print("Unknown command: " + inp)

    def PickUpItem(self):
        print("Pick Up Item")
        #list some items based on the current level
        print("You found a sword")
        print("You found a potion")
        print("You found a key")

    
    def LookAround(self):
        print("Look Around")
        #list some things based on the current level
        print("You are in a forest")
        print("There is a path to the north")
        print("There is a path to the south")        

    def CurrentOptions(self):
        print("Current Options: \n")

        #list some options based on the current level
        print("w - Move forward")
        print("s - Move backward")
        print("l - Look around")
        print("p - Pick up item")
        print("u - Use item")
        print("i - Open inventory")
        print("m - Open map")
        print("j - Open journal")
        print("c - Open character sheet")
        print("e - Open equipment")
        print("q - Open quest log")
        print("t - Talk to NPC")
        print("r - Rest")
        print("f - Fight")
        print("h - Help")
        print("? - List current options")
        print("exit - Exit game")
    


    def HelpState(self):
        print("Help")
        print("Commands: \n")
        print("exit - exits the game \n")
        print("help - displays this help message \n")
        print("? - lists current options \n")

    
    def StartState(self):
        print("Enter Name: \n")
        name = input(">>")
        print("Hello " + name + "!")
        self.state = "running"



#entry point
game = Game()

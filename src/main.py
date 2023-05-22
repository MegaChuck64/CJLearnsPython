class Game:
    
    def __init__(self):
        self.state = "starting"
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
        print("Enter Command: \n")
        command = input(">>")
        if (command == "exit"):
            self.state = "exiting"
        elif (command == "help"):
            print("Commands: \n")
            print("exit: exits the game \n")
            print("help: displays this message \n")
        else:
            print("Invalid Command, type 'help' for a list of commands \n")            
        
    
    def StartState(self):
        print("Enter Name: \n")
        name = input(">>")
        print("Hello " + name + "!")
        self.state = "running"



#entry point
game = Game()

import pyautogui as pyg
import keyboard, time

class Bot:
    def __init__(self):
        # used for visual detection later
        self.bop = "bop.png"
        self.bite = "bite.png"
        self.fish_caught = 0
    def fish(self):

        while not keyboard.is_pressed("q"):
            print("Exit anytime by pressing: \t \"Q\"")
            time.sleep(2)
            print("Fishing...")
            # fishing logic here
    def quit(self):
        print("exiting...")
        exit(0)

# entry point


if __name__ == "__main__":
    bot = Bot()
    bot.fish()
else:
    print("Do not do that!")
    exit(1)
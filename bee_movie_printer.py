from pynput.keyboard import Key, Controller
import time
import random

def main():
    should_tts = True
    keyboard = Controller()
    delay = 2 #adjust to get into your chosen platform
    time.sleep(delay)

    file = open("bee_movie_script.txt", "r")
    
    for line in file:
        
        if(not line.isspace()):
            if(should_tts): keyboard.type("/tts ")
            keyboard.type(line)
            delay = random.randrange(1, 3)
            time.sleep(delay)
    

if __name__ == "__main__":
    main();


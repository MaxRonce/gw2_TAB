from pynput import keyboard
import time

# Boolean to control the recording state
recording = False
key_start = 'Key.home'
key_stop = 'Key.esc'

key_start_time = 0
pause_start_time = 0
last_key = None

# Record all the pressed keys in a list
# list_pressed_keys = [(key, time_pressed),pause_time, (key, time_pressed),pause_time, ...]
list_pressed_keys = []

def on_press(key):
    global recording, key_start_time, last_key
    try:
        # Convert the key to a string
        key = key.char
    except AttributeError:
        # Handle special keys like 'Key.space' and 'Key.enter'
        key = str(key)

    # Check if the 'Enter' key is pressed to start recording
    if key == str(key_start) and not recording:
        recording = True
        print('Recording started.')
        return

    # Add the pressed key to the list only if recording is active
    if recording and key != last_key:
        # Print the currently pressed keys
        key_start_time = time.time()


        pause_time = time.time() - pause_start_time
        # round at 3 decimals
        pause_time = round(pause_time, 3)
        print("Pause : ", pause_time)

        # Add the pressed key to the list
        list_pressed_keys.append(pause_time)

        # Update last_key
        last_key = key


def on_release(key):
    global recording, pause_start_time, key_start_time, last_key
    try:
        # Convert the key to a string
        key = key.char
    except AttributeError:
        # Handle special keys like 'Key.space' and 'Key.enter'
        key = str(key)

    # Remove the released key from the list only if recording is active
    if recording and key == last_key:
        # Print the currently pressed keys
        print("Currently pressed keys:", key)
        pressed_time = time.time() - key_start_time
        #round at 3 decimals
        pressed_time = round(pressed_time, 3)
        print("Time pressed:", pressed_time)

        # Add the pressed key to the list
        list_pressed_keys.append((key, pressed_time))

        # Start pause timer
        pause_start_time = time.time()

        # Stop the keylogger if the 'Esc' key is pressed
        if key == str(key_stop):
            return False

        # Reset last_key
        last_key = None

# Create a listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the listener
listener.start()

# Keep the program running
listener.join()

print('Recording stopped.')

#Delete the first pause time and the last key
list_pressed_keys.pop(0)
list_pressed_keys.pop()

# Print the list of pressed keys
print(list_pressed_keys)

#Print the list in a .txt file
with open('keyboard_input.txt', 'w', encoding="UTF-8") as f:
    for item in list_pressed_keys:
        f.write(f"{item}\n")





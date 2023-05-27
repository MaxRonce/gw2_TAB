from pynput import keyboard
from pynput.keyboard import Controller
import time

keyboard_input_list = [('&', 0.12810921669006348), 0.48992061614990234, ('é', 0.1401209831237793),
                       0.7221205234527588, ('"', 0.2186875343322754), 0.5084376335144043, ("'", 0.17564988136291504),
                       0.6950976848602295, ('(', 0.23720431327819824), 1.080428123474121]

# list_pressed_keys = [(key, time_pressed),pause_time, (key, time_pressed),pause_time, ...]

key_start = 'Key.home'
key_stop = 'Key.esc'
start_execution = False

# keyboard controller
kbc = Controller()

def on_press(key):
    global start_execution
    try:
        # Convert the key to a string
        key = key.char
    except AttributeError:
        key = str(key)

    # Check if the 'Home' key is pressed to start execution
    if key == str(key_start) and not start_execution:
        start_execution = True
        print('Execution started.')
        for i in keyboard_input_list:
            if type(i) is tuple:
                # Press and hold the key
                kbc.press(i[0])
                # Hold the key for the specified amount of time
                time.sleep(i[1])
                # Release the key
                kbc.release(i[0])
            else:
                # Pause for the specified amount of time
                time.sleep(i)
        return False  # This will stop the listener

    # Check if the 'Escape' key is pressed to stop execution
    if key == str(key_stop):
        return False  # This will stop the listener

# Create a listener
listener = keyboard.Listener(on_press=on_press)

# Start the listener
listener.start()

# Keep the program running
listener.join()

from pynput import keyboard
from pynput.keyboard import Controller
import time
from file_reader import convert_file_to_list

#keyboard_input_list = [('&', 0.12810921669006348), 0.48992061614990234, ('é', 0.1401209831237793),
#                      0.7221205234527588, ('"', 0.2186875343322754), 0.5084376335144043, ("'", 0.17564988136291504),
#                     0.6950976848602295, ('(', 0.23720431327819824), 1.080428123474121]
keyboard_input_list = convert_file_to_list('input_records.txt')
print(list)

# Add this to the top of your script, where you import modules
from pynput.keyboard import Key

# Then create a mapping dictionary for special keys
special_keys = {
    'Key.f1': Key.f1,
    'Key.f2': Key.f2,
    'Key.f3': Key.f3,
    'Key.f4': Key.f4,
    'Key.f5': Key.f5,
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7' : '7',
    '8' : '8',
    '9' : '9',
    '0' : '0',
    # add more special keys if needed
}

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
                try :
                    # Press the key
                    print("Pressed: ", i[0])
                    kbc.press(special_keys[i[0]])

                    # Pause for the specified amount of time
                    time.sleep(i[1])
                    # Release the key
                    kbc.release(special_keys[i[0]])
                except ValueError:
                    pass


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

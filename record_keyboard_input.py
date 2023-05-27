from pynput import keyboard, mouse
import time
import threading

# Boolean to control the recording state
recording = False
key_start = 'Key.home'
key_stop = 'Key.esc'



key_start_time = 0
mouse_start_time = 0
pause_start_time = 0
last_key = None

# Record all the pressed keys and mouse events in a list
# list_pressed_inputs = [(input, time_elapsed), pause_time, (input, time_elapsed), pause_time, ...]
list_pressed_inputs = []

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
        print("Pause: ", pause_time)

        # Add the pause time to the list
        list_pressed_inputs.append(pause_time)

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
        print("Currently pressed key:", key)
        pressed_time = time.time() - key_start_time
        # round at 3 decimals
        pressed_time = round(pressed_time, 3)
        print("Time pressed:", pressed_time)

        # Add the pressed key to the list
        list_pressed_inputs.append((key, pressed_time))

        # Start pause timer
        pause_start_time = time.time()

        # Stop the keylogger if the 'Esc' key is pressed
        if key == str(key_stop):
            print('Recording stopped.')
            stop_recording()
            return False

        # Reset last_key
        last_key = None



def on_click(x, y, button, pressed):
    # Ignore mouse click events if not recording
    global recording, mouse_start_time, pause_start_time
    if recording:

        #avoid left and right click

        if button == mouse.Button.left or button == mouse.Button.right:
            return

        if pressed:
            # Start on click timer
            mouse_start_time = time.time()
            # Reset pause timer
            pause = time.time() - pause_start_time
            # round at 3 decimals
            pause = round(pause, 3)
            print("Pause: ", pause)
            # Add the pause time to the list
            list_pressed_inputs.append(pause)
        else:
            print(f"Currently pressed mouse_key : {button}")
            pressed_time = time.time() - mouse_start_time
            # round at 3 decimals
            pressed_time = round(pressed_time, 3)
            print("Time pressed:", pressed_time)
            list_pressed_inputs.append((button, pressed_time))
            # Start pause timer
            pause_start_time = time.time()




# Create listeners for keyboard and mouse events
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
mouse_listener = mouse.Listener(on_click=on_click)

# Start the listeners
keyboard_listener.start()
mouse_listener.start()

# Create a threading Event to signal the stop of the recording
stop_event = threading.Event()

# Function to stop the recording and the listeners
def stop_recording():
    global recording
    recording = False
    stop_event.set()
    keyboard_listener.stop()
    mouse_listener.stop()

def format_list(list_pressed_inputs):
    # Delete the first pause time and the last key/mouse event
    list_pressed_inputs.pop(0)
    list_pressed_inputs.pop()

    # if there is two or more pause in a row sum them and only keep the sum
    i = 0
    while i < len(list_pressed_inputs) - 1:
        if isinstance(list_pressed_inputs[i], float) and isinstance(list_pressed_inputs[i + 1], float):
            list_pressed_inputs[i + 1] += list_pressed_inputs[i]
            list_pressed_inputs.pop(i)
        else:
            i += 1

    # if the last event is a pause, delete it
    if isinstance(list_pressed_inputs[-1], float):
        list_pressed_inputs.pop()

    # if the first event is a pause, delete it
    if isinstance(list_pressed_inputs[0], float):
        list_pressed_inputs.pop(0)


# Start a thread to wait for the 'Esc' key and stop the recording
stop_thread = threading.Thread(target=stop_event.wait)
stop_thread.start()

# Wait for the stop thread to finish
stop_thread.join()

print('Recording stopped.')

# Format the list
format_list(list_pressed_inputs)

# Print the list of pressed keys and mouse events
print(list_pressed_inputs)

# Print the list in a .txt file
with open('input_records.txt', 'w', encoding="UTF-8") as f:
    for item in list_pressed_inputs:
        f.write(f"{item}\n")

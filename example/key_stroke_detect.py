from sshkeyboard import listen_keyboard, stop_listening
import threading

# Global flag and lock to control input and key handling
i_key_pressed = False
input_lock = threading.Lock()

def press(key):
    global i_key_pressed
    with input_lock:
        if key == 'space':
            i_key_pressed = True
            stop_listening()  # Stop listening to the keyboard after 'i' is pressed
        else:
            print(f"'{key}' pressed")

def release(key):
    with input_lock:
        print(f"'{key}' released")

def listen_keys():
    listen_keyboard(
        on_press=press,
        on_release=release,
    )

# Run the keyboard listener in a separate thread
listener_thread = threading.Thread(target=listen_keys)
listener_thread.start()

# Wait for the listener thread to finish
listener_thread.join()

# Check if 'i' was pressed and then ask for input
if i_key_pressed:
    with input_lock:
        user_input = input("Enter something: ")
        print(f"User entered: {user_input}")


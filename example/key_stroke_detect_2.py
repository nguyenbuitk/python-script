from sshkeyboard import listen_keyboard, stop_listening
import threading

key_pressed = None  # Variable to store the key pressed

def press(key):
    global key_pressed
    key_pressed = key
    print(f"'{key}' pressed")
    if key == 'esc':
        stop_listening()
    elif key == 'enter':
        print("You pressed 'enter'.")
        stop_listening()
    elif key == 'n':
        print("Skipping user input.")
        stop_listening()

def release(key):
    print(f"'{key}' released")

def listen_keys():
    listen_keyboard(on_press=press, on_release=release)

while True:
    key_pressed = None  # Reset the key pressed variable
    key_listener = threading.Thread(target=listen_keys)
    key_listener.start()
    key_listener.join()

    if key_pressed == 'enter':
        break  # Exit the loop when 'enter' is pressed
    elif key_pressed == 'n':
        continue  # Skip user input and continue to listen for the next keystroke

    # If no 'n' key is pressed, listen for user input
    user_input = input("Enter some text: ")
    print(f"You entered: {user_input}")

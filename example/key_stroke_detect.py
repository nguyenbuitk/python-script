from sshkeyboard import listen_keyboard, stop_listening

pressed_keys = []

def press(key):
    print(f"'{key}' pressed")
    pressed_keys.append(key)
    handle_key_press(key)
    if key == 'esc':
        stop_listening()

def release(key):
    print(f"'{key}' released")

def count_key_presses(key):
    return pressed_keys.count(key)

def print_pressed_keys():
    print("Keys pressed during the session: ")
    for key in pressed_keys:
        print(key, end=' ')
    print()

def handle_key_press(key):
    # New function with if-else condition to handle different keys
    if key == 'a':
        print("You pressed 'a', which is the first letter of the alphabet.")
    elif key == 'b':
        print("You pressed 'b', which is the second letter of the alphabet.")
    elif key.isdigit():
        print(f"You pressed the number '{key}', which is a digit.")
    else:
        print(f"You pressed '{key}', which is another key.")

if __name__ == "__main__":
    print("Press 'esc' to stop.")
    listen_keyboard(on_press=press, on_release=release)
    print_pressed_keys()
    specific_key = input("Enter a key to count its presses: ")
    count = count_key_presses(specific_key)
    print(f"The key '{specific_key}' was pressed {count} times.")

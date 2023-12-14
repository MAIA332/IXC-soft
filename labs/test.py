import threading
import sys
import curses

def get_user_input(window):
    user_input = ""
    while True:
        char = window.getch()

        with open('test.txt', 'a+') as file:
            file.write(chr(char))

        sys.stdout.write(chr(char))
        sys.stdout.flush()

        if char == 10:  # Enter key
            break

        user_input += chr(char)

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

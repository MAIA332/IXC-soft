import datetime
from colorama import Fore, Back, Style, init
import platform
import json
import os
import keyboard
import threading
import time


with open('data/comandos.json') as file:
    comandos = json.load(file)

osParams ={
    "SO":platform.system()
}


def key_listener():
    while True:
        try:
            if keyboard.is_pressed('up'):
                print("KEY UP")
                
            time.sleep(0.1)
        except:
            break


def console():
    

    def now(flag):
        print(datetime.datetime.now())

    def help(flag):
        print(f"---------------------------------------------\n{Fore.GREEN}Command of user Mode:{Style.RESET_ALL}\n---------------------------------------------\n")
        for i in comandos:
            print(f"{Fore.RED}{i}{Style.RESET_ALL}: {comandos[i]['desc']}\n")

    def clear(flag):
        if osParams["SO"] == "Linux":
            os.system("clear")
        else:
            os.system("cls")

    def display(flag):
    
        def interfaces_():
            print("interfaces")
        
        t_display={
            "interfaces":interfaces_
        }

        
        try:
            if flag != "":
                print(f"{flag}:")
            else:
                flag = input("~display flag: ")
            

            t_display[flag]()

        except Exception as e:
            print(f"Comando {flag} é desconhecido ou inválido neste contexto {Fore.RED}{type(e)}{Style.RESET_ALL}")
            return

    t = {
        "clear":clear,
        "display":display,
        "now":now,
        "help":help
    }


    while True:
        try:
            clear("")
            cmd = input("~Lk: ") + " "
            
            if cmd == " ":
                pass
            else:
                flags = cmd.split(" ")

                with open('data/history.txt','a+') as file:
                    file.write(" ".join(flags)+"\n")
                    file.close()

                t[flags[0]](flags[1])

        except Exception as e:
            print(f"Comando {cmd}é desconhecido ou inválido neste contexto {Fore.RED}{type(e)}{Style.RESET_ALL}")

key_listener_thread = threading.Thread(target=key_listener)
key_listener_thread.start()
console()
key_listener_thread.join()

import datetime
from colorama import Fore, Back, Style, init
import platform
import json
import os
import keyboard
import threading
import time
from visual import graph

basedir = os.getcwd()
with open('data/comandos.json') as file:
    comandos = json.load(file)

osParams ={
    "SO":platform.system()
}


def key_listener():
    while True:
        try:
            char = window.getch()
            if keyboard.is_pressed('up'):

                with open('data/history.txt','r') as file:
                    lines = file.readlines()
                
                last_line = lines[-1].strip()
                print(last_line)
                
            time.sleep(0.1)
        except:
            break


def console():
    

    def now(flag):
        a=datetime.datetime.now()
        print(a)

    def help(flag):

        def complete():
            command = input("~Lk (Comando): ")
            print(f"---------------------------------------------\n{Fore.GREEN}Detalhes do comando {command}:{Style.RESET_ALL}\n---------------------------------------------\n")
            
            for i in comandos[command]["details"]:
                print(f"{Fore.RED}{i}{Style.RESET_ALL}{Style.RESET_ALL}: {comandos[command]['details'][i]}")

        f = {
            "-a":complete
        }

        if flag != "":
            f[flag]()
        else:
            print(f"---------------------------------------------\n{Fore.GREEN}Command of user Mode:{Style.RESET_ALL}\n---------------------------------------------\n")
            for i in comandos:
                print(f"{Fore.RED}{i}{Style.RESET_ALL}: {comandos[i]['desc']}\n")

    def clear(flag):
        def clear_history():
            with open('data/logs/log_comands.txt','w') as file:
                file.write("")

            print("Histórico limpo")

        f ={
            "-h":clear_history
        }

        if flag !="":
            f[flag]()
        else:
            if osParams["SO"] == "Linux":
                os.system("clear")
            else:
                os.system("cls")

    def history(flag):
        with open('data/logs/log_comands.txt','r') as file:
            for line in file:
                print(line)
            print("\n")

    def display(flag):
    
        def sample_():
            with open('data/sample.json') as file:
                data = json.load(file)
                print(data)
        
        t_display={
            "sample":sample_
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

    def build(flag):

        def graph_():

            amostra = input("~Lk (Amostra): ")
            vs = graph.graphs(basedir,amostra)


            def bar():
                vs.bar()

            print(f"Build para {amostra} concluído \n")
            
            while True:

                t_graph ={
                    "bar":bar
                }

                cmd =  input(f"~Lk ({amostra}): ")
                if cmf == "quit":
                    return
                else:
                    t_graph[cmd]()


        t_build = {
            "graph":graph_,
        }

        if flag != "":
            pass
        else:
            flag = input("~display flag: ")
        
        t_build[flag]()



    t = {
        "clear":clear,
        "display":display,
        "now":now,
        "help":help,
        "history":history,
        "build":build
    }


    while True:
        try:
            cmd = input("~Lk: ") + " "
            
            if cmd == " ":
                pass
            else:
                flags = cmd.split(" ")

                with open('data/history.txt','a+') as file:
                    file.writelines("\n"+f" ".join(flags))
                    file.close()

                with open('data/logs/log_comands.txt','a+') as file:
                    file.writelines("\n"+f":{datetime.datetime.now()} ".join(flags))
                    file.close()

                t[flags[0]](flags[1])

        except Exception as e:
            print(f"Comando {cmd}é desconhecido ou inválido neste contexto {Fore.RED}{type(e)}{Style.RESET_ALL}")

key_listener_thread = threading.Thread(target=key_listener)
key_listener_thread.start()
console()
key_listener_thread.join()

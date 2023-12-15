# ========================= imports ======================
import datetime
from colorama import Fore, Back, Style, init
import platform
import json
import os
import threading
import time
from visual import graph
import readline

# ========================= Classe para manipulação de histórico ======================
class CommandHistory:
    def __init__(self):
        self.history = []
        self.index = 0

    def add_command(self, command):
        self.history.append(command)
        self.index = len(self.history)

    def get_previous_command(self):
        if self.index > 0:
            self.index -= 1
        return self.history[self.index] if self.history else ""

    def get_next_command(self):
        if self.index < len(self.history):
            self.index += 1
        return self.history[self.index] if self.history else ""

# ========================= Configurações de sistema ======================
basedir = os.getcwd() ## Diretorio Base
with open('data/comandos.json') as file: # Pega a lista de comandos
    comandos = json.load(file)

osParams ={ # Parametros do S.O
    "SO":platform.system()
}

# ========================= Função principal ======================

def console():
    history_ = CommandHistory() # Instancia a classe que manipula o histórico de comandos
    

    def now(flag): # Imprime data e hora atual
        a=datetime.datetime.now()
        print(a)

    def help(flag): # Exibe uma lista de comandos para verificar quais estão disponíveis

        def complete():
            command = input("~Lk (Comando): ")
            print(f"---------------------------------------------\n{Fore.GREEN}Detalhes do comando {command}:{Style.RESET_ALL}\n---------------------------------------------\n")
            
            for i in comandos[command]["details"]:
                print(f"{Fore.RED}{i}{Style.RESET_ALL}: {comandos[command]['details'][i]}")

        f = {
            "-a":complete
        }

        if flag != "":
            f[flag]()
        else:
            print(f"---------------------------------------------\n{Fore.GREEN}Command of user Mode:{Style.RESET_ALL}\n---------------------------------------------\n")
            for i in comandos:
                print(f"{Fore.RED}{i}{Style.RESET_ALL}: {comandos[i]['desc']}\n")

    def clear(flag): # Função para limpeza da tela e limpeza de arquivos e cache
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

    def history(flag): # Função para olhar o histórico de comandos
        with open('data/logs/log_comands.txt','r') as file:
            for line in file:
                print(line)
            print("\n")

    def display(flag): # Função de exibição de dados, que estão na pasta data
    
        def sample_():
            with open('data/sample.json') as file:
                data = json.load(file)
                print(data)
        
        def Boards():
            with open('data/amostras.json') as file:
                data = json.load(file)
                for i in data:
                    print(f"\n{Fore.GREEN}{i}{Style.RESET_ALL}: {data[i]}")

        t_display={
            "sample":sample_,
            "boards":Boards
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

    def build(flag): # Função que instância o contrutor de gráficos, baseado na amostra indicada no comando

        def feedback_():

            amostra = input("~Lk (Amostra): ")
            vs = graph.graphs(basedir,amostra)


            def pie():
                vs.pie()

            print(f"Build para {amostra} concluído \n")
            
            while True:

                try:

                    t_graph ={
                        "notas":pie,
                        
                    }

                    cmd =  input(f"~Lk ({amostra}): ")
                    if cmd == "quit":
                        return
                    else:
                        try:
                            t_graph[cmd]()
                        except:
                            a=t[cmd]("")

                            if a == False:
                                return
                
                except Exception as e:
                    print(f"Não foi possível identificas os parametros passados: {e}")
                    

        try:
            t_build = {
                "feed":feedback_,
            }

            if flag != "":
                pass
            else:
                flag = input("~display flag: ")
            
            try:
                t_build[flag]()
            except:
                a = t[flag]("")

                if a == False:
                    return
                
        except Exception as e:
            print(f"Não foi possível identificas os parametros passados: {e}")
            return
    
    def quit(flag):
        return False

    t = { # Lista de comandos disponíveis
        "clear":clear,
        "display":display,
        "now":now,
        "help":help,
        "history":history,
        "build":build,
        "quit":quit
    }

    def completer(text, state): # Definição dos dados utilizados na função tab, para autocompletar
        options = [key for key in t.keys() if key.startswith(text)]
        return options[state] if state < len(options) else None

    readline.set_completer(completer) # Define o completer da função tab
    readline.parse_and_bind("tab: complete")

    while True: #Loop principal, para pegar os comandos e separar as flags, bem como registrar nos históricos a interação do usuário
        
        try:
            user_input = input("~Lk: ") + " "

            if user_input == "exit":
                break

            if user_input:
                history_.add_command(user_input)

            if user_input == "up":
                command = history_.get_previous_command()
            elif user_input == "down":
                command = history_.get_next_command()
            else:
                command = user_input

            flags = command.split(" ") 

            with open("data/history.txt","a+") as file:
                file.writelines("\n"+flags[0])       

            with open('data/logs/log_comands.txt','a+') as file:
                file.writelines("\n"+f":{datetime.datetime.now()} ".join(flags))
                file.close()

            a = t[flags[0]](flags[1])
            if a == False:
                return
        
        except Exception as e:
            print(f"Não foi possível identificas os parametros passados: {e}")

       
if __name__ == "__main__": # Executa o arquivo se for chamado
    console()
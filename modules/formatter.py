class former:
    def __init__(self,basedir,data) -> None:
        self.json = __import__("json")
        self.pd = __import__("pandas")
        self.name = data

        with open(f"{basedir}/data/{self.name}.json") as file:
            data_ = self.json.load(file)

        self.df = self.pd.DataFrame(data_)
        self.features = self.df.drop(["Endereço","ID_Fechamento","ID","ID_Assunto_BD","Mensagem","Assunto","Horario_Fechamento"],axis=1)
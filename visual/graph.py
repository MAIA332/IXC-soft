class graphs:
    def __init__(self,basedir,data) -> None:
        import matplotlib.pyplot as plt

        self.plt = plt
        self.numpy = __import__("numpy")
        self.os = __import__("os")
        self.json = __import__("json")
        self.name = data
        self.time = __import__("datetime")
        self.directory = "data/images/"
        self.pandas = __import__("pandas")
        self.sns = __import__("seaborn")
        
        self.functions ={
            "Pie":self.pie
        }

        
        with open(f"{basedir}/data/{self.name}.json") as file:
            self.data_ = self.json.load(file)


        self.os.makedirs(self.directory, exist_ok=True)
        self.filepath = self.os.path.join(self.directory, f"{self.name}.png")

        
    def pie(self):

        a=[i["Nota_telefone"] for i in self.data_]
        b= []
        for i in a:
            if i not in b: 
                b.append(i)

        d = [int((a.count(i)*100)/len(a)) for i in b]
        d = sorted(d,reverse=True)

        z = [0.1]
        for i in range(0,len(d)-1):
            z.append(0)

        explode = tuple(z)
    

        colors = ['gold', 'lightcoral', 'lightskyblue', 'orange']

        self.plt.pie(d, explode=explode, labels=b, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)


        self.plt.title('Distribuição de notas x feedback')


        self.plt.axis('equal')  # Para certificar que seja circular
        self.plt.ioff()
        
        self.plt.savefig(self.filepath)

        self.plt.pause(0.001)

    def hist(self):
        df = self.pandas.DataFrame(self.data_)

        # Converter a coluna 'Horario_Fechamento' para formato de data e criar um campo separado para hora
        df['Horario_Fechamento'] = self.pandas.to_datetime(df['Horario_Fechamento'], format='%d-%m-%Y:%H:%M')
        df['Hora_Fechamento'] = df['Horario_Fechamento'].dt.time
        df["Data_Fechamento"] = df['Horario_Fechamento'].dt.date
        features = df.drop(["Endereço","ID_Fechamento","ID","ID_Assunto_BD","Mensagem","Assunto","Horario_Fechamento"],axis=1)

        self.plt.figure(figsize=(12, 6))
        self.sns.barplot(x='Data_Fechamento', y='Nota_telefone', hue='Assunto BD', data=features)
        self.plt.title('Time Series Plot of Nota_telefone Over Time')
        self.plt.xlabel('Date')
        self.plt.ylabel('Nota_telefone')
        self.plt.xticks(rotation=45)
        self.plt.tight_layout()
        self.plt.savefig(self.filepath)

        self.plt.pause(0.001)
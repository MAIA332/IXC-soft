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
        a=[i["Assunto BD"] for i in self.data_]
        b= []
        for i in a:
            if i not in b: 
                b.append(i)

        self.plt.figure(figsize=(12, 10))

        self.plt.hist(a, bins=range(0, 11), edgecolor='black', rwidth=0.8,align='mid')

        self.plt.xlabel('Assuntos')
        self.plt.ylabel('Frequency')
        self.plt.title('Histograma de assuntos')
        self.plt.xticks(rotation=50)

        self.plt.savefig(self.filepath)

        self.plt.pause(0.001)
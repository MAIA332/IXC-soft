class graphs:
    def __init__(self,basedir,data) -> None:
        self.numpy = __import__("numpy")
        self.os = __import__("os")
        self.json = __import__("json")
        self.name = data
        self.time = __import__("datetime")
        
        self.functions ={
            "Pie":self.pie
        }

        
        with open(f"{basedir}/data/{self.name}.json") as file:
            self.data_ = self.json.load(file)

        self.a=[i["Nota_telefone"] for i in self.data_]
        self.b= []
        for i in self.a:
            if i not in self.b: 
                self.b.append(i)

        self.d = [int((self.a.count(i)*100)/len(self.a)) for i in self.b]

        
    def pie(self):
        import matplotlib.pyplot as plt

        now = self.time.datetime.now()
        directory = "data/images/"

        colors = ['gold', 'lightcoral', 'lightskyblue', 'orange']
        explode = (0.1, 0, 0,0)  # Destaca o setor analisado


        plt.pie(self.d, explode=explode, labels=self.b, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)


        plt.title('Distribuição de notas x feedback')


        plt.axis('equal')  # Para certificar que seja circular
        plt.ioff()
        self.os.makedirs(directory, exist_ok=True)

        filepath = self.os.path.join(directory, f"{self.name}.png")

        plt.savefig(filepath)

        plt.pause(0.001)

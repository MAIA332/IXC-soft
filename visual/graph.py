class graphs:
    def __init__(self,basedir,data) -> None:
        self.numpy = __import__("numpy")
        self.os = __import__("os")
        self.json = __import__("json")
        
        self.functions ={
            "Bar":self.bar
        }

        
        with open(f"{basedir}/data/{data}.json") as file:
            self.data_ = self.json.load(file)

        self.x = [i["Assunto BD"] for i in self.data_]
        self.y = [i["Nota_telefone"] for i in self.data_]
        
    def bar(self):
        import matplotlib.pyplot as plt

        pfig, ax = plt.subplots(figsize=(12, 10))
        ax.bar(self.x,self.y, width=0.7, alpha=0.7, linewidth=0.7)
        ax.grid(True, linestyle='--', alpha=0.7)

        """ ax.set(xlim=(0, 8), xticks=self.numpy.arange(1, 8),
            ylim=(0, 8), yticks=self.numpy.arange(1, 8)) """
        

        plt.show()
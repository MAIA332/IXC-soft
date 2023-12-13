class graphs:
    def __init__(self) -> None:
        self.matplotlib = __import__("matplotlib")
        self.numpy = __import__("numpy")
        
        self.functions ={
            "Bar":self.bar
        }

    def bar(self,data):
        pfig, ax = self.matplotlib.pyplot.subplots()

        ax.bar(data["x"], data["y"], width=1, edgecolor="white", linewidth=0.7)

        ax.set(xlim=(0, 8), xticks=self.numpy.arange(1, 8),
            ylim=(0, 8), yticks=self.numpy.arange(1, 8))

        self.matplotlib.pyplot.show()
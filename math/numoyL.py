import numpy as np
import matplotlib.pyplot as plt
'''
Python numpy and matplotlib are libraries inside custom mde classes to
- perofrm basic algebra and geometry
Plot graphs
- Solve simple equations
- Visualize math problems wit real data

'''

class LinePlotter:
    def __init__(self,slope,intercept):
        self.slope = slope
        self.intercept = intercept

    def generate_data(self, x_range):
        self.x = np.array(x_range)
        self.y = self.slope * self.x + self.intercept

    def plot(self):
        plt.plot(self.x,self.y,label=f'y= {self.slope}x + {self.intercept}')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Line Plot")
        plt.legend()
        plt.grid(True)
        plt.show()



line = LinePlotter(2,1)
line.generate_data(range(-10,11))
line.plot()
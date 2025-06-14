🟦 **Activity 1: NumPy Array Challenge – “Math with Magic Lists”**

### Goal:

Practice using NumPy arrays to perform operations like a calculator, but with entire lists at once.

### Instructions:

1. Create two arrays:
   ```python
   import numpy as np

   a = np.array([2, 4, 6, 8, 10])
   b = np.array([1, 3, 5, 7, 9])
   ```
2. Print the result of:
   * `a + b`
   * `a - b`
   * `a * 2`
   * `b / 2`
3. Use `np.mean()` to find the average of array `a`.

### Stretch Challenge:

* Use `np.max()` and `np.min()` to find the biggest and smallest number in each array.

---

## **Activity 2: Graphing with a Line Class – “Draw Your Equation!”**

### Goal:

Use OOP to graph a straight line with any slope and y-intercept.

### Instructions:

1. Copy or write the `LinePlotter` class:

```python
import numpy as np
import matplotlib.pyplot as plt

class LinePlotter:
    def __init__(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept

    def generate_data(self, x_range):
        self.x = np.array(x_range)
        self.y = self.slope * self.x + self.intercept

    def plot(self):
        plt.plot(self.x, self.y, label=f"y = {self.slope}x + {self.intercept}")
        plt.title("My Line Graph")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.show()
```

2. Use the class:

```python
line = LinePlotter(2, 1)  # You can change this!
line.generate_data(range(-10, 11))
line.plot()
```

3. Try different slopes (positive, negative, zero) and describe how the line changes.

🟩 **Activity 2: Graph Your Name (with Math!)**

### 📌 Goal:

Use a class and matplotlib to create a graph with dots in the shape of your  **first initial** .

### 🧠 Instructions:

1. Use this starter class:

```python
import matplotlib.pyplot as plt
import numpy as np

class LetterGrapher:
    def __init__(self, points):
        self.points = np.array(points)

    def plot(self):
        x = self.points[:, 0]
        y = self.points[:, 1]

plt.plot(x,y, marker='o', linestyle='-',color='blue')
        #plt.scatter(x, y, c='blue')
        plt.title("My Letter")
        plt.grid(True)
        plt.gca().set_aspect('equal')
        plt.show()
```

2. Create your own letter shape:

```python
# Example: The letter E
my_points = [
    [0, 0], [0, 1], [0, 2], [1, 2], [0, 1], [1, 1], [0, 0], [1, 0]
]

letter = LetterGrapher(my_points)
letter.plot()
```

3. Modify the coordinates to draw **your own first initial** (like S, M, A, J, etc.)

---

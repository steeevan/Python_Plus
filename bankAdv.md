
---

## 🐶 Python OOP Project: **Virtual Pet Simulator**

### 📌 Project Description:

Create your own **Virtual Pet Simulator** using Python and Object-Oriented Programming (OOP). Your pet will have stats like hunger, happiness, and energy. You’ll build methods to feed, play with, and rest your pet while keeping track of its well-being.

---

### 🎯 Objectives:

* Learn how to define and use Python classes
* Practice object instantiation and interaction
* Implement logic using `if`, `elif`, and `while` loops
* Simulate state changes with method calls
* Improve modular thinking and code design

---

### 🧱 Part 1: Define the Pet Class

Create a class called `Pet`. Inside it, define:

* Attributes:

  * `name` (string)
  * `hunger` (integer from 0–10)
  * `happiness` (integer from 0–10)
  * `energy` (integer from 0–10)
* Constructor (`__init__`) to initialize all attributes

---

### 🧱 Part 2: Create the Pet Methods

Add these methods to your class:

* `feed()`: decreases hunger
* `play()`: increases happiness, decreases energy
* `rest()`: increases energy
* `status()`: prints all current stats
* `update()`: simulates time passing by increasing hunger and reducing happiness

---

### 🧱 Part 3: Build the Game Loop

Write a loop that:

* Greets the user
* Asks for their pet's name
* Repeatedly asks:

  > "What would you like to do? (feed/play/rest/status/exit)"
* Calls the appropriate method based on the input
* Calls `update()` after each action

---

### 🔍 Example Output:

```
Welcome to Virtual Pet!
What is your pet's name? > Fluffy

[Options: feed, play, rest, status, exit]
What would you like to do? > feed
You fed Fluffy. Hunger decreased!

What would you like to do? > play
You played with Fluffy! Happiness increased, but energy dropped.

What would you like to do? > status
Fluffy's Status:
Hunger: 3
Happiness: 7
Energy: 4

What would you like to do? > exit
Goodbye!
```

---

### 💡 Hints and Advice:

* Keep attributes between 0 and 10 using `max()` and `min()`
* Use print statements to inform the user what their action did
* Make your loop user-friendly by formatting the messages nicely
* Start small, then improve your program over time

---


## 🎨 Problem: **AI Story Customizer**

### 📋 Objective:

Write a Python program that prompts the user for a  **main character** , a  **setting** , and a  **plot element** , then sends that input to Gemini to generate a creative short story using those elements.

---

### ✅ Functional Requirements:

1. Ask the user for:
   * A main character (e.g., “a brave robot named Zeno”)
   * A setting (e.g., “on Mars during a dust storm”)
   * A plot twist or challenge (e.g., “must solve a riddle to escape”)
2. Create a custom prompt:
   > `"Write a fun short story (5-7 sentences) that includes the following elements:   Main Character: {user_character}   Setting: {user_setting}   Plot Element: {user_plot}"`
   >
3. Send the prompt to Gemini and display the story.
4. Save the prompt and story in a file `story_log.txt`.

---

### 🧪 Example:

**Input:**

```
Main character: A brave robot named Zeno
Setting: On Mars during a dust storm
Plot: Must solve a riddle to escape
```

**Gemini Output:**

```
Zeno, the brave robot, trudged across the red sands of Mars, his sensors barely functioning in the blinding dust storm. As he reached the abandoned Martian outpost, a holographic riddle flickered to life: “I speak without a mouth and hear without ears. What am I?” Zeno calculated quickly, “An echo!” The door hissed open, revealing a hidden chamber. Inside, he found blueprints for a weather shield to survive the storm. Zeno's circuits buzzed with pride. Mars would not defeat him today.
```

---

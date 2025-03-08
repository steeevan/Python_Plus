# **📌 Discord Bot Project: Build Interactive Commands**

## **🚀 Project Overview**

In this project, you will build a **Discord bot** that can respond to user commands. You will create four different commands that will help users interact with the bot in fun and useful ways. By completing this project, you will gain experience with  **handling user input, working with APIs, formatting messages, and using reactions for engagement** .

---

## **🔹 Project Requirements**

### **📜 What You’ll Need**

✅ **Python 3.8+ (Python 12 recommended)**

✅ A **Discord account & server**

✅ A bot registered in the **Discord Developer Portal**

✅ **API access** to OpenWeatherMap for weather data

✅ Basic understanding of **functions, API requests, error handling, and message formatting**

### **🎯 What You Will Build**

✅ **`!reverse`** → The bot reverses a user’s input.

✅ **`!avatar`** → The bot fetches and displays a user's profile picture.

✅ **`!weather`** → The bot fetches real-time weather data.

✅ **`!poll`** → The bot creates an interactive reaction-based poll.

---

# **📌 Step 1: Setting Up Your Discord Bot**

### **1️⃣ Create a New Bot on Discord API**

1. **Go to the Discord Developer Portal** → [https://discord.com/developers/applications](https://discord.com/developers/applications)
2. Click **"New Application"** → Give it a name.
3. Click on the **"Bot"** tab → Click **"Add Bot"** → Click **"Yes, do it!"**

### **2️⃣ Get Your Bot Token**

1. Under the **Bot** section, find  **“TOKEN”** .
2. Click  **“Reset Token”** , then **copy the token** (keep it secret!).

### **3️⃣ Invite the Bot to Your Server**

1. Go to **OAuth2** →  **URL Generator** .
2. Check **"bot"** and  **"applications.commands"** .
3. Copy the generated **invite link** and add your bot to your server.

---

# **📌 Step 2: Setting Up Your Project Directory**

Organizing your files properly helps keep your project clean.

### **📁 Recommended Folder Structure**

```
📂 discord-bot-project
 ┣ 📂 cogs             # Stores command files
 ┃ ┣ 📜 fun.py        # Handles fun commands
 ┣ 📜 bot.py          # Main bot file
 ┣ 📜 config.py       # Stores API keys & settings
 ┣ 📜 requirements.txt # Lists dependencies
 ┣ 📜 README.md       # Project description
```

### **1️⃣ Install Required Dependencies**

Run the following command:

```bash
pip install discord.py aiohttp
```

---

# **📌 Step 3: Implementing Commands (With Hints & Guidance)**

---

## **🟢 1️⃣ `!reverse` - Reversing Text**

### **📌 What This Command Does**

This command will take a message from the user and return it  **reversed** .

### **🛠️ Functions & Methods You Will Need**

* `ctx.send()` → Sends a message in the channel.
* `[::-1]` → A Python trick to reverse a string.

### **🔹 Steps to Implement**

1. Capture the **user’s message** as input.
2. **Check if the user provided text** . If no text was provided, send an error message.
3. Use **string slicing (`[::-1]`)** to reverse the text.
4. Send the reversed text as a response.

### **💡 Helpful Hints**

* You can use an `if` condition to check if the user  **didn’t enter any text** .
* Ensure the bot **doesn't accidentally reverse command names** by capturing only the message.

### **🎯 Example Usage**

```
User: !reverse Hello world!
Bot: 🔄 !dlrow olleH
```

---

## **🟢 2️⃣ `!avatar` - Fetching a User’s Profile Picture**

### **📌 What This Command Does**

This command fetches and displays a **user’s profile picture** in an embed.

### **🛠️ Functions & Methods You Will Need**

* `ctx.author` → Accesses the user who ran the command.
* `discord.Embed()` → Creates a formatted message with an image.
* `.set_image(url=...)` → Sets an image inside the embed.

### **🔹 Steps to Implement**

1. Get the **user object** (if no user is mentioned, default to the command sender).
2. Extract the **profile picture URL** from the user object.
3. Create an **embed message** using `discord.Embed()`.
4. Attach the **user’s avatar URL** to the embed.
5. Send the embed in chat.

### **💡 Helpful Hints**

* If a user has  **no profile picture** , Discord provides a  **default avatar** .
* You can allow users to **mention someone else** to fetch  **their avatar instead** .

### **🎯 Example Usage**

```
User: !avatar
Bot: [Sends user's profile picture]
```

---

## **🟡 3️⃣ `!weather` - Fetching Real-Time Weather**

### **📌 What This Command Does**

This command fetches the **current weather** for a city using an API.

### **🛠️ Functions & Methods You Will Need**

* `aiohttp.ClientSession()` → Allows API requests.
* `.json()` → Converts API response into Python data.
* `discord.Embed()` → Formats the weather response.

### **🔹 Steps to Implement**

1. Capture the **city name** from the user.
2. Make an **API request** to OpenWeatherMap using `aiohttp`.
3. Extract relevant **weather details** (temperature, weather condition, etc.).
4. Format the response using  **an embed message** .
5. Send the weather data back to the user.

### **💡 Helpful Hints**

* If the city  **is not found** , handle errors by sending a  **user-friendly message** .
* Convert **Kelvin to Celsius** using `temp - 273.15` (or use `units=metric` in API requests).

### **🎯 Example Usage**

```
User: !weather New York
Bot: Weather in New York - 22°C, Clear Sky
```

---

## **🔴 4️⃣ `!poll` - Creating a Reaction-Based Poll**

### **📌 What This Command Does**

This command allows users to  **create a poll** , and others can vote using  **reactions** .

### **🛠️ Functions & Methods You Will Need**

* `discord.Embed()` → Creates a poll message.
* `.add_field(name=..., value=...)` → Adds voting options.
* `.add_reaction(emoji)` → Adds reactions for voting.

### **🔹 Steps to Implement**

1. Capture the **poll question and two options** from the user.
2. Create an **embed message** containing the poll question.
3. Add two options (e.g., `1️⃣`, `2️⃣`) as choices.
4. Send the poll message to the chat.
5. Add reaction emojis  **so users can vote** .

### **💡 Helpful Hints**

* Ensure the user  **enters exactly two options** , otherwise send an error message.
* You can **extend** this later to support  **more than two options** .

### **🎯 Example Usage**

```
User: !poll "Cats or Dogs?" "Cats" "Dogs"
Bot: 📊 Poll: Cats or Dogs?
(Users vote with reactions)
```

---

# **📌 Step 4: Running & Testing Your Bot**

Once all commands are implemented:

✅ Run your bot with:

```bash
python bot.py
```

✅ Test all four commands:

```
!reverse Hello world!
!avatar
!weather New York
!poll "Favorite color?" "Red" "Blue"
```

---

## **🚀 Final Challenge**

Now that you’ve built the core commands, try improving them:
✅  **Allow `!poll` to accept more than two options** .

✅  **Handle errors gracefully (e.g., missing input)** .

✅  **Expand `!weather` to show a weekly forecast** .



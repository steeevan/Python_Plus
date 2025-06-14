import google.generativeai as genai

# set up API KEY
genai.configure(api_key="AIzaSyBU_ZdYgXuK0gPKjxwUMZfF0UoWmrwrQqE")

# ✅ Step 2: Prompt user for story elements
print("📖 Welcome to the AI Story Customizer!")
character = input("👤 Enter the main character (e.g., 'a brave robot named Zeno'): ")
setting = input("🌍 Enter the setting (e.g., 'on Mars during a dust storm'): ")
plot = input("🎯 Enter the plot twist or challenge (e.g., 'must solve a riddle to escape'): ")

# ✅ Step 3: Craft the Gemini prompt
prompt = f"""
Write a fun short story (5-7 sentences) that includes the following elements:
Main Character: {character}
Setting: {setting}
Plot Element: {plot}
"""

# ✅ Step 4: Send prompt to Gemini
model = genai.GenerativeModel("models/gemini-1.5-flash")

try:
    print("\n🤖 Generating story...\n")
    response = model.generate_content(prompt)
    story = response.text.strip()

    print("✨ Your AI-Generated Story:\n")
    print(story)

    # ✅ Step 5: Save everything to a log file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("story_log.txt", "a", encoding="utf-8") as f:
        f.write("\n==============================\n")
        f.write(f"🕒 {timestamp}\n")
        f.write(f"👤 Character: {character}\n")
        f.write(f"🌍 Setting: {setting}\n")
        f.write(f"🎯 Plot: {plot}\n")
        f.write("📖 Story:\n")
        f.write(story + "\n")

    print("\n✅ Story saved to story_log.txt")

except Exception as e:
    print("❌ An error occurred:", e)
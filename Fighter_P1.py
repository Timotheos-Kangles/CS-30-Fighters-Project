# --- TASK 1 ---
MyFighter = {
    "name": "Nightshade",
    "class": "Shadowmancer",
    "weapons": ["Obsidian Dagger", "Shadow Whip", "Phantom Bow"],
    "health": 95,
    "description": "A master of the dark arts, capable of summoning shadows to confuse enemies and strike from the darkness. She harnesses the power of the void to manipulate and control the night."
}

# Print weapons separately
print(f"{MyFighter['name']} has the following weapons!", *MyFighter['weapons'], sep="\n - ")
print(f"My fighter's name is {MyFighter['name']}, they're a {MyFighter['class']} type fighter!")

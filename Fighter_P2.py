# Fighter Assignment Part 2
# Hargun & Harmin & Timo
# ----------------------------------------------
# Database of fighters
fighters = {
    "ironfighter": {
        "name": "Steve",
        "class": "Army Soldier",
        "weapons": ["Gun", "Shield", "TNT"],
        "health": 100,
        "description": "Strongest soldier in the US army, taught to fight since birth.",
        "weakness": "Fire",
        "superpowers": ["Super Speed", "Super Strength", "Agility"]
    }, #Hargun’s fighter
    "thor": {
        "name": "Thor Odinson",
        "class": "God of Thunder",
        "weapons": ["Mjolnir", "Stormbreaker", "Lightning Bolts"],
        "weaknesses": ["Overconfidence", "Worthiness to wield Mjolnir", "Emotional vulnerability"],
        "super_powers": ["Godly Strength", "Flight", "Weather Manipulation", "Immortality"]
    },
    "blackwidow": {
        "name": "Natasha Romanoff",
        "class": "Spy",
        "weapons": ["Guns", "Knives", "Widow's Bite"],
        "weakness": "Emotional vulnerability",
        "superpowers": ["Master Martial Artist", "Master Spy", "Master Acrobat"]
    },
}












# 2) Create at least four unique sentences using values from your database.
def PrintSentences():
    print(f"My Fighter's name is {fighters['blackwidow']['name']}, their weakness is {fighters['blackwidow']['weakness']}") # Timo
    print(f" {fighters['thor']['name'].upper()} is the {fighters['thor']['class']}, his super powers are  {fighters['thor']['super_powers']} ") # Hargun
    print(f"{fighters['ironfighter']['name']} is an {fighters['ironfighter']['class']} armed with a {fighters['ironfighter']['weapons'][1]}, always ready for battle.")
    print(f"{fighters['thor']['super_powers']}, {fighters['thor']['name']} struggles with {fighters['thor']['weaknesses']}, making him vulnerable in critical moments.") #harmin




# 3) Print out all available weapons in your database in a numbered list.
def WeaponAvailability():
    count = 1
    print("\nBelow you may find a list of available weapons: ")
    for fighter in fighters:
        for i in fighters[fighter]['weapons']:
            print(f"{count}. {i}")  # Use count for numbering
            count += 1  # Adds count after each loop

PrintSentences()
WeaponAvailability()

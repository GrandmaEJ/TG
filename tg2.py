# i put some anime details 
anime_details = {
    "naruto": {
        "plot": "Naruto Uzumaki, a young ninja, seeks recognition and dreams of becoming the Hokage, the village leader.",
        "story": "Follows Naruto's journey as he grows from an underdog to a powerful ninja, facing various challenges and foes.",
        "genre": "Action, Adventure, Fantasy",
        "details": "Naruto is a long-running series with complex character development and epic battles."
    },
    "opm": {
        "plot": "Saitama, a hero for fun, can defeat any opponent with a single punch but struggles with boredom and a lack of recognition.",
        "story": "The series satirizes superhero tropes, focusing on Saitama's existential crisis and the vibrant cast of supporting characters.",
        "genre": "Action, Comedy, Superhero",
        "details": "One Punch Man combines humor with high-octane action, offering a unique take on the superhero genre."
    },
    "db": {
        "plot": "Follows the adventures of Goku as he trains in martial arts and explores the world in search of the seven orbs known as Dragon Balls.",
        "story": "From fighting powerful foes to participating in tournaments, Goku's journey spans multiple sagas and dimensions.",
        "genre": "Action, Adventure, Martial Arts",
        "details": "Dragon Ball is a classic anime known for its iconic battles, humor, and memorable characters."
    },
    "fmab": {
        "plot": "Follows two brothers, Edward and Alphonse Elric, who use alchemy in their quest to find the Philosopher's Stone to restore their bodies.",
        "story": "Explores themes of sacrifice, redemption, and the consequences of tampering with life's natural order in a richly developed world.",
        "genre": "Action, Adventure, Drama, Fantasy",
        "details": "Fullmetal Alchemist Brotherhood is renowned for its deep storyline, intricate world-building, and emotional depth."
    }
}

# and here i put some Alice key for shortcut or long search 
alias_mapping = {
    "one punch man": "opm",
    "dragon ball" : "db",
    "full metal alchemist brotherhood": "fmab"
}


message = input("Enter your query: ").lower()


if message in anime_details:
    anime_key = message
elif message in alias_mapping:
    anime_key = alias_mapping[message]
else:
    anime_key = None



#-------------------Main Func--------------------#
def main():
    if anime_key:
        anime_info = anime_details[anime_key]
        print(f"Plot: {anime_info['plot']}")
        print(f"Story: {anime_info['story']}")
        print(f"Genre: {anime_info['genre']}")
        print(f"Details: {anime_info['details']}")
        
    else:
        print("No matching data found.")
        
#--------------- Define a Loop ---------------#
#def loop():

#--------------------- Run ----------------#
if __name__ == "__main__":
    main()

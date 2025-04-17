from flask import Flask, render_template, request, redirect, url_for, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/start', methods=["POST"])
def start():
    name = request.form["name"]
    session["character"] = {
        "name": name,
        "level": 0,
        "monster": ["Slime", "Goblin", "Orc", "Troll", "Stampede of Monsters", "Dragon", "Demon God"],
        "position": ["Traveller", "Villager", "Village Hero", "Noble", "King", "SSS Rank Adventurer", "Demi-God"],
        "weapon": ["Wooden Sword", "Iron Sword", "Steel Sword", "Mithril Sword", "Excalibur", "Soul Sword", "Sword of Light"]
    }
    return redirect(url_for('game'))

@app.route('/game', methods=["GET", "POST"])
def game():
    character = session.get("character")
    animate = ""
    message = ""

    if request.method == "POST":
        guess = request.form["guess"]
        monster_attack = random.randint(0, 2 ** character["level"])
      
        print(f"Monster Attack Value: {monster_attack}")  
        
        if int(guess) == monster_attack:
            character["level"] += 1
            message = f"{character['name']} hit the monster and leveled up!"
            animate = "victory-flash"
            if character["level"] >= len(character["monster"]) - 1:
                return redirect(url_for('game_over'))
        else:
            message = f"{character['name']} missed the attack! The monster counterattacked!"
            animate = "blackout"

        session["character"] = character 

    return render_template('game.html', character=character, message=message, animate=animate)

@app.route('/game_over')
def game_over():
    character = session.get("character")
    return render_template('game_over.html', character=character)

if __name__ == '__main__':
    app.run(debug=True)

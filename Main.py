from flask import url_for,Flask, render_template, request, jsonify, redirect
import random
import logging

app = Flask(__name__, template_folder="templates")
# app.config["DEBUG"] = True  

def generate_random(name = None):
    if name:
        name = name.title()
        choices = [
            f"No {name}, Makan patty itu spongebob",
            f"No {name}, Berdansalah, Patrick",
            f"No {name}, Bikini Bottom safest place eaa",
            f"No {name}, Squidward, auratmu yang mana sih?!",
            f"No {name}, Plankton kenapa gak jadi developer aja",
            f"No {name}, Gary, lap dulu lendirmu awowkwkwwo",
            f"No {name}, Sandy ilmuwan keren",
            f"No {name}, PoV Mr. Krabs: duit, duit, duit! wkwkwk",
            f"No {name}, Squidward kulbett",
            f"No {name}, Spongebob koki terhebat sekabupaten wkwkwk"
        ]    

    else:
        choices = [
            "No spongebob, Makan patty itu spongebob",
            "No spongebob, Berdansalah, Patrick",
            "No spongebob, Bikini Bottom safest place eaa",
            "No spongebob, Squidward, auratmu yang mana sih?!",
            "No spongebob, Plankton kenapa gak jadi developer aja",
            "No spongebob, Gary, lap dulu lendirmu awowkwkwwo",
            "No spongebob, Sandy ilmuwan keren",
            "No spongebob, PoV Mr. Krabs: duit, duit, duit! wkwkwk",
            "No spongebob, Squidward kulbett",
            "No spongebob, Spongebob koki terhebat sekabupaten wkwkwk"
        ]

    return random.choice(choices)

@app.route("/<name>")
def random_heresy(name = None):
    return render_template("kerangajaib.html", kerangAjaib = f"{generate_random((name))}")

@app.route('/success/<name>')
def success(name):
    return render_template("kerangajaib.html", kerangAjaib = f"{generate_random((name))}")

@app.route("/login/", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get("nm")
        return redirect(url_for('success',name = user))
    
@app.route("/form/")
def form():
    return render_template("indeks.html")
    



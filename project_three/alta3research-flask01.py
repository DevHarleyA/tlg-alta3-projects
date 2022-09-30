#!/usr/bin/env python3

"""
Flask Library Proficiency Assignment
Tasks:
- at least two endpoints
- at least one of your endpoints should return JSON
- one additional feature (chose jinja2 logic)
"""

# import Flask: Web application framework
from flask import Flask
# import render_template to show html home page
from flask import render_template
# import josnify to retrun legal JSON text
from flask import jsonify

# create an instance of the Flask object
app = Flask(__name__)

# JSON data for application
masterwonders = [
    {
        "wonder": "Mount Everest",
        "location": "China-Nepal border",
        "type": "natural wonder"
    },
    {
        "wonder": "Harbor of Rio de Janiero",
        "location": "Rio de Janiero, Brazil",
        "type": "natural wonder"
    },
    {
        "wonder": "The Great Barrier Reef",
        "location": "Eastern Aulstralia Coast (Queensland)",
        "type": "natural wonder"
    },
    {
        "wonder": "Victoria Falls",
        "location": "Zambia-Zimbabwe border",
        "type": "natural wonder"
    },
    {
        "wonder": "Paricutin Volcano",
        "location": "Uruapan, Michoacan, Mexico",
        "type": "natural wonder"
    },
    {
        "wonder": "The Grand Canyon",
        "location": "Arizona",
        "type": "natural wonder"
    },
    {
        "wonder": "Aurora Borealis (The Northern Lights)",
        "location": "High Latitude Regions",
        "type": "natural wonder"
    },
    {
        "wonder": "The Great Pyramids of Giza",
        "location": "Cairo, Egypt",
        "type": "wonder"
    },
    {
        "wonder": "Petra",
        "location": "Jordan SE Desert",
        "type": "wonder"
    },
    {
        "wonder": "Great Wall of China",
        "location": "Northern China",
        "type": "wonder"
    },
    {
        "wonder": "Chichen Itza",
        "location": "Yucatan, Mexico",
        "type": "wonder"
    },
    {
        "wonder": "Machu Picchu",
        "location": "Peru",
        "type": "wonder"
    },
    {
        "wonder": "Christ the Redeemer",
        "location": "Rio de Janiero, Brazil",
        "type": "wonder"
    },
    {
        "wonder": "Colosseum",
        "location": "Rome, Italy",
        "type": "wonder"
    },
    {
        "wonder": "Taj Mahal",
        "location": "Agra, India",
        "type": "wonder"
    }
]

# function to return content
# route() tells the application which URL should call the home function
@app.route("/")
def home():
    # Sends back the greeting page
    return render_template("index.html")

@app.route("/sevenwonders")
def seven_wonders():
    wonders = []
    for wonder in masterwonders:
        if wonder["type"] == "wonder":
            wonders.append(wonder)

    return render_template("seven.html", list = wonders)


@app.route("/naturalwonders")
def natural_wonders():
    wonders = []
    for wonder in masterwonders:
        if wonder["type"] == "natural wonder":
            wonders.append(wonder)

    return render_template("natural.html", list = wonders)

# endpoint that returns JSON
@app.route("/all")
def all_wonders():
    # josnify returns legal JSON
    return jsonify(masterwonders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000) # runs the application at port 3000